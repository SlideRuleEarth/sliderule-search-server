# ECR repository that holds the Lambda container image. Built + pushed
# by scripts/deploy_lambda.sh; the Lambda function ignores subsequent
# image_uri changes from terraform (see lambda.tf) so routine image
# updates don't require a plan/apply cycle.

resource "aws_ecr_repository" "docsearch" {
  # Name uses the sanitized full domain so test and prod don't collide —
  # var.domain_root is the first label ("search") and is the same in both
  # environments. Mirrored in scripts/deploy_lambda.sh as ${DOMAIN//./-}.
  name                 = "docsearch-${replace(var.domainName, ".", "-")}"
  image_tag_mutability = "MUTABLE"
  force_delete         = true

  image_scanning_configuration {
    scan_on_push = true
  }
}

# Keep only the last handful of images. The live Lambda always reads
# :latest, so older tagged snapshots are for audit / rollback only.
resource "aws_ecr_lifecycle_policy" "docsearch" {
  repository = aws_ecr_repository.docsearch.name

  policy = jsonencode({
    rules = [{
      rulePriority = 1
      description  = "keep last 10 images"
      selection = {
        tagStatus   = "any"
        countType   = "imageCountMoreThan"
        countNumber = 10
      }
      action = { type = "expire" }
    }]
  })
}
