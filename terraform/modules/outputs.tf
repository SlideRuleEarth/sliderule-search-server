output "cloudfront_distribution_id" {
  value = aws_cloudfront_distribution.search.id
}

output "cloudfront_domain_name" {
  value = aws_cloudfront_distribution.search.domain_name
}

output "ecr_repository_url" {
  value = aws_ecr_repository.docsearch.repository_url
}

output "lambda_function_name" {
  value = aws_lambda_function.docsearch.function_name
}

output "lambda_function_url" {
  value = aws_lambda_function_url.docsearch.function_url
}
