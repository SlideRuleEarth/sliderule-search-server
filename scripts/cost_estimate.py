#!/usr/bin/env python3
"""Estimate Lambda compute + request cost in hourly buckets over a window.

Queries CloudWatch via `aws cloudwatch get-metric-data` (one call, two
metrics joined by timestamp), applies public Lambda pricing, emits
tab-separated rows that compose with scripts/utc_to_local.py:

    timestamp            UTC ISO-8601 bucket start
    invocations          Sum of Lambda Invocations in the bucket
    duration_ms          Sum of Lambda Duration in the bucket (ms)
    cost_usd             Computed compute+request cost for the bucket

Architecture + memory are hardcoded to match terraform/modules/lambda.tf.
If those change, update the constants below.

Rates per AWS Lambda pricing page (verified 2026-04, us-east-1):
    - $0.20 per 1M requests           = 0.0000002 per request
    - $0.0000166667 per GB-second     (x86_64; arm64 would be 0.0000133334)

Estimates compute + request cost only. Does NOT include data transfer,
CloudFront requests/bandwidth, ECR storage. Compute+requests dominate
this Lambda's bill in practice.

Usage:
    python3 cost_estimate.py <function-name> [--region us-east-1] [--hours 24]

Pipe the output through scripts/utc_to_local.py for local-time display
(the Makefile targets already do this).
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone

PRICE_PER_REQUEST = 0.0000002
PRICE_PER_GB_SECOND = 0.0000166667
MEMORY_GB = 2.0  # = 2048 MB, matching terraform/modules/lambda.tf memory_size


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n\n")[0])
    parser.add_argument("function_name", help="Lambda function name, e.g. docsearch-search-testsliderule-org")
    parser.add_argument("--region", default="us-east-1")
    parser.add_argument("--hours", type=int, default=24, help="Lookback window in hours (default 24)")
    parser.add_argument("--period", type=int, default=3600, help="Bucket size in seconds (default 3600)")
    args = parser.parse_args()

    end = datetime.now(timezone.utc).replace(microsecond=0)
    start = end - timedelta(hours=args.hours)

    dims = [{"Name": "FunctionName", "Value": args.function_name}]
    queries = [
        {"Id": "inv", "MetricStat": {"Metric": {"Namespace": "AWS/Lambda", "MetricName": "Invocations", "Dimensions": dims}, "Period": args.period, "Stat": "Sum"}},
        {"Id": "dur", "MetricStat": {"Metric": {"Namespace": "AWS/Lambda", "MetricName": "Duration", "Dimensions": dims}, "Period": args.period, "Stat": "Sum"}},
    ]

    cmd = [
        "aws", "cloudwatch", "get-metric-data",
        "--region", args.region,
        "--start-time", start.strftime("%Y-%m-%dT%H:%M:%S"),
        "--end-time", end.strftime("%Y-%m-%dT%H:%M:%S"),
        "--metric-data-queries", json.dumps(queries),
        "--output", "json",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        return result.returncode

    payload = json.loads(result.stdout)
    by_id = {
        r["Id"]: dict(zip(r["Timestamps"], r["Values"]))
        for r in payload.get("MetricDataResults", [])
    }
    inv = by_id.get("inv", {})
    dur = by_id.get("dur", {})

    # Union of timestamps. Empty response still prints the header + total row
    # (both zeros) so the target's output shape is stable.
    timestamps = sorted(set(inv) | set(dur))
    total_cost = 0.0
    total_inv = 0
    total_dur_ms = 0.0

    print("timestamp\tinvocations\tduration_ms\tcost_usd")
    for ts in timestamps:
        i = int(inv.get(ts, 0))
        d_ms = float(dur.get(ts, 0.0))
        cost = i * PRICE_PER_REQUEST + (d_ms / 1000.0) * MEMORY_GB * PRICE_PER_GB_SECOND
        total_inv += i
        total_dur_ms += d_ms
        total_cost += cost
        print(f"{ts}\t{i}\t{d_ms:.0f}\t{cost:.6f}")
    print(f"total\t{total_inv}\t{total_dur_ms:.0f}\t{total_cost:.6f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
