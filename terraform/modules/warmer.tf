# Keeps the docsearch Lambda container warm by invoking it on a 5-min
# EventBridge schedule. Without this, the first query after a 10-15 min
# idle period pays a 15-60s cold-start cost that exceeds CloudFront's
# 30s origin_read_timeout — the viewer sees a 503 before the Lambda
# finishes initializing.
#
# server/handler.py detects the scheduled-event envelope and
# short-circuits before Mangum, so the invocation is cheap — the
# value comes from AWS treating "a recent successful invocation" as
# a reason to keep the container alive. 5 minutes is comfortably under
# the observed reap window (~10-15 min) with margin for AWS scheduling
# jitter.
#
# Why the scheduled-invoke pattern rather than Provisioned Concurrency:
#
#   - Traffic level: ~1 concurrent request at peak. Keeping one
#     container warm handles the realistic load; we don't need N > 1.
#   - Cost: EventBridge + 288 warmup invocations/day fits inside AWS
#     free tier. Provisioned Concurrency for a 2GB function is ~$21/mo
#     per instance, 24/7.
#   - Deploy simplicity: Provisioned Concurrency requires publishing a
#     Lambda version + alias and updating PC config on each deploy.
#     scripts/deploy_lambda.sh would need 10+ extra lines. The
#     scheduled warmer is indifferent to image updates.
#
# When to upgrade to Provisioned Concurrency:
#
#   - Sustained traffic > ~10 req/sec, where one warm container can't
#     absorb the flow and cold-start concurrency starts hurting viewers.
#   - SLA / zero-cold-start guarantee becomes a real requirement (the
#     scheduled warmer is a workaround, not an AWS-backed contract).
#   - Multi-AZ availability concerns — Provisioned Concurrency can be
#     split across zones; the scheduled warmer hits whichever
#     container happens to be up.

resource "aws_cloudwatch_event_rule" "warmer" {
  name                = "docsearch-warmer-${replace(var.domainName, ".", "-")}"
  description         = "Invoke docsearch Lambda every 5 min to keep the container warm (avoids cold-start 503s)."
  schedule_expression = "rate(5 minutes)"
}

resource "aws_cloudwatch_event_target" "warmer" {
  rule      = aws_cloudwatch_event_rule.warmer.name
  target_id = "docsearch-lambda"
  arn       = aws_lambda_function.docsearch.arn

  # No input override: we want EventBridge's default envelope
  # ("source":"aws.events", "detail-type":"Scheduled Event", ...) to
  # reach the handler so the branch in server/handler.py recognizes it.
}

# EventBridge needs explicit permission to invoke the function; scoped
# to this rule's ARN so no other rule can invoke on its behalf.
resource "aws_lambda_permission" "allow_eventbridge_invoke" {
  statement_id  = "AllowEventBridgeWarmerInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.docsearch.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.warmer.arn
}
