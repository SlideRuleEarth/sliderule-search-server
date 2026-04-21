# Per-IP rate limit in front of CloudFront. The docs-search endpoint is
# intentionally open (no auth, no API keys), so the only backstop against
# a runaway or malicious looping client is this rule.
#
# WAF v2 rate-based statement:
#   - Aggregated by source IP.
#   - `limit` is requests per trailing 5-minute window. 2000 ~= 6.6 r/s
#     sustained, which is well above what a human demo or a reasonable
#     agent eval run would produce, and stingy enough to blunt a tight
#     loop. Raise if real traffic ever pushes up against it.
#   - `scope = "CLOUDFRONT"` is required for distributions; the resource
#     lives in us-east-1 (we already declare that provider in main.tf).
resource "aws_wafv2_web_acl" "search" {
  name  = "${replace(var.domainName, ".", "-")}-ratelimit"
  scope = "CLOUDFRONT"

  default_action {
    allow {}
  }

  rule {
    name     = "rate-limit-per-ip"
    priority = 1

    action {
      block {}
    }

    statement {
      rate_based_statement {
        limit              = 2000
        aggregate_key_type = "IP"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "rate-limit-per-ip"
      sampled_requests_enabled   = true
    }
  }

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "${replace(var.domainName, ".", "-")}-waf"
    sampled_requests_enabled   = true
  }
}
