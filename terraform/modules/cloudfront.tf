# CloudFront distribution fronting the docsearch Lambda. One origin
# (Lambda Function URL via OAC), one default behavior forwarding all
# HTTP verbs to it, no caching (the Lambda maintains its own LRU).

# Managed policies referenced by the default cache behavior below.
#
# AllViewerExceptHostHeader (NOT AllViewer) is load-bearing for OAC +
# Lambda Function URL: CloudFront signs each origin request with SigV4
# over the *origin's* Host header (the lambda-url.*.on.aws hostname).
# If the origin request policy also forwards the viewer's Host header
# (search.testsliderule.org), that viewer Host clobbers the signed one
# and the Lambda URL returns 403 "The request signature we calculated
# does not match the signature you provided." Using the "ExceptHost"
# variant drops Host from the forward set so SigV4 keeps control of
# it. See:
#   https://aws.amazon.com/blogs/networking-and-content-delivery/restrict-access-to-your-aws-lambda-function-url-to-amazon-cloudfront/
data "aws_cloudfront_origin_request_policy" "all_viewer_except_host" {
  name = "Managed-AllViewerExceptHostHeader"
}

data "aws_cloudfront_cache_policy" "caching_disabled" {
  name = "Managed-CachingDisabled"
}

# OAC for Lambda Function URLs: CloudFront signs the origin request
# with SigV4 so the AWS_IAM-restricted URL accepts the call.
resource "aws_cloudfront_origin_access_control" "lambda" {
  name                              = "${replace(var.domainName, ".", "-")}-lambda-oac"
  origin_access_control_origin_type = "lambda"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# CORS response headers policy. `access_control_allow_methods`
# advertises to browsers which verbs are legal cross-origin; the
# distribution's cache behavior below is what actually gates which
# verbs reach the origin at all.
resource "aws_cloudfront_response_headers_policy" "cors" {
  name = "${replace(var.domainName, ".", "-")}-cors"

  cors_config {
    access_control_allow_credentials = false

    access_control_allow_headers {
      items = ["*"]
    }

    access_control_allow_methods {
      items = ["GET", "HEAD", "OPTIONS", "POST"]
    }

    access_control_allow_origins {
      items = ["*"]
    }

    origin_override = true
  }
}

resource "aws_cloudfront_distribution" "search" {
  depends_on      = [aws_lambda_function_url.docsearch]
  enabled         = true
  is_ipv6_enabled = true
  aliases         = [var.domainName]
  comment         = "SlideRule docsearch (${var.domainName})"

  origin {
    domain_name              = local.lambda_url_host
    origin_id                = "lambda-${replace(var.domainName, ".", "-")}"
    origin_access_control_id = aws_cloudfront_origin_access_control.lambda.id

    custom_origin_config {
      http_port              = 80
      https_port             = 443
      origin_protocol_policy = "https-only"
      origin_ssl_protocols   = ["TLSv1.2"]
    }
  }

  default_cache_behavior {
    target_origin_id       = "lambda-${replace(var.domainName, ".", "-")}"
    allowed_methods        = ["GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"]
    cached_methods         = ["GET", "HEAD", "OPTIONS"]
    viewer_protocol_policy = "redirect-to-https"
    compress               = true

    # Forward everything EXCEPT the viewer's Host header (see the data
    # blocks at the top of this file for the rationale), cache nothing.
    # The Lambda does its own per-query LRU caching.
    cache_policy_id          = data.aws_cloudfront_cache_policy.caching_disabled.id
    origin_request_policy_id = data.aws_cloudfront_origin_request_policy.all_viewer_except_host.id

    response_headers_policy_id = aws_cloudfront_response_headers_policy.cors.id
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn      = aws_acm_certificate_validation.cert.certificate_arn
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2021"
  }

  price_class = "PriceClass_100"
}
