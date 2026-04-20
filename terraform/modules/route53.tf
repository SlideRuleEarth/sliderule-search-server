data "aws_route53_zone" "public" {
  name         = var.domainApex
  private_zone = false
}

resource "aws_acm_certificate" "search" {
  domain_name       = var.domainName
  validation_method = "DNS"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route53_record" "cert_validation" {
  allow_overwrite = true
  name            = tolist(aws_acm_certificate.search.domain_validation_options)[0].resource_record_name
  records         = [tolist(aws_acm_certificate.search.domain_validation_options)[0].resource_record_value]
  type            = tolist(aws_acm_certificate.search.domain_validation_options)[0].resource_record_type
  zone_id         = data.aws_route53_zone.public.id
  ttl             = 60
}

resource "aws_acm_certificate_validation" "cert" {
  certificate_arn         = aws_acm_certificate.search.arn
  validation_record_fqdns = [aws_route53_record.cert_validation.fqdn]
}

resource "aws_route53_record" "search" {
  zone_id = data.aws_route53_zone.public.id
  name    = var.domainName
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.search.domain_name
    zone_id                = aws_cloudfront_distribution.search.hosted_zone_id
    evaluate_target_health = false
  }
}

# IPv6 alias. The CloudFront distribution has is_ipv6_enabled = true but
# that's only half the story — without an AAAA record, IPv6-only clients
# can't resolve the hostname to a CloudFront edge. AWS recommends
# matching A + AAAA alias records whenever IPv6 is enabled on the
# distribution.
resource "aws_route53_record" "search_ipv6" {
  zone_id = data.aws_route53_zone.public.id
  name    = var.domainName
  type    = "AAAA"

  alias {
    name                   = aws_cloudfront_distribution.search.domain_name
    zone_id                = aws_cloudfront_distribution.search.hosted_zone_id
    evaluate_target_health = false
  }
}
