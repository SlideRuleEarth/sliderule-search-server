# Lambda function (container image) + Function URL that serves
# /docsearch/search. CloudFront fronts the Function URL via OAC
# (see cloudfront.tf); the URL itself is AWS_IAM-restricted so only
# CloudFront can invoke it.
#
# Image updates are driven out-of-band by scripts/deploy_lambda.sh
# (docker build → ECR push → aws lambda update-function-code). The
# `lifecycle.ignore_changes = [image_uri]` block prevents terraform
# from reverting those deploys on the next plan.

resource "aws_iam_role" "lambda" {
  name = "docsearch-lambda-${replace(var.domainName, ".", "-")}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/docsearch-${replace(var.domainName, ".", "-")}"
  retention_in_days = 30
}

resource "aws_lambda_function" "docsearch" {
  function_name = "docsearch-${replace(var.domainName, ".", "-")}"
  role          = aws_iam_role.lambda.arn
  package_type  = "Image"
  image_uri     = "${aws_ecr_repository.docsearch.repository_url}:latest"
  architectures = ["arm64"]
  memory_size   = 2048
  timeout       = 30

  image_config {
    command = ["server.handler.lambda_handler"]
  }

  lifecycle {
    ignore_changes = [image_uri]
  }

  depends_on = [
    aws_iam_role_policy_attachment.lambda_basic_execution,
    aws_cloudwatch_log_group.lambda,
  ]
}

resource "aws_lambda_function_url" "docsearch" {
  function_name      = aws_lambda_function.docsearch.function_name
  authorization_type = "AWS_IAM"
}

# Let CloudFront (signed by the OAC in cloudfront.tf) invoke the URL.
#
# As of October 2025 AWS requires BOTH actions on new Function URL
# resource policies: lambda:InvokeFunctionUrl (the URL-scoped action)
# AND lambda:InvokeFunction (the function-scoped action that backs it).
# Prior to that change InvokeFunctionUrl alone was enough; new deploys
# 403 without the second grant. aws_lambda_permission takes exactly
# one action so we emit two resources. See:
#   https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html
#   https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-lambda.html
resource "aws_lambda_permission" "allow_cloudfront_invoke_url" {
  statement_id           = "AllowCloudFrontInvokeUrl"
  action                 = "lambda:InvokeFunctionUrl"
  function_name          = aws_lambda_function.docsearch.function_name
  principal              = "cloudfront.amazonaws.com"
  source_arn             = aws_cloudfront_distribution.search.arn
  function_url_auth_type = "AWS_IAM"
}

resource "aws_lambda_permission" "allow_cloudfront_invoke" {
  statement_id  = "AllowCloudFrontInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.docsearch.function_name
  principal     = "cloudfront.amazonaws.com"
  source_arn    = aws_cloudfront_distribution.search.arn
}

# Hostname portion of the Function URL — CloudFront's origin.domain_name
# expects just the host, no scheme or trailing slash.
locals {
  lambda_url_host = regex("^https?://([^/]+)/?$", aws_lambda_function_url.docsearch.function_url)[0]
}
