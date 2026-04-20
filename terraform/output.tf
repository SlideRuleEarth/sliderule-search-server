output "domain_apex" {
  value = var.domainApex
}

output "domain_name" {
  value = var.domainName
}

output "domain_root" {
  value = var.domain_root
}

output "cloudfront_distribution_id" {
  value = module.cloudfront.cloudfront_distribution_id
}

output "cloudfront_domain_name" {
  value = module.cloudfront.cloudfront_domain_name
}

output "ecr_repository_url" {
  value = module.cloudfront.ecr_repository_url
}

output "lambda_function_name" {
  value = module.cloudfront.lambda_function_name
}

output "lambda_function_url" {
  value = module.cloudfront.lambda_function_url
}
