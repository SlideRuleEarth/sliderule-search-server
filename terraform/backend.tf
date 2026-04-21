terraform {
  # Tracked floor: the AWS provider 6.x line (locked in .terraform.lock.hcl)
  # requires protocol v6, which in turn requires Terraform >= 1.5. Without
  # this constraint older terraform binaries fail with a confusing provider
  # protocol error before schema loading.
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source = "hashicorp/aws"
      # Upper bound prevents an unreviewed major-version bump.
      # Lower bound is where Lambda Function URL OAC landed.
      version = ">= 5.50.0, < 7.0.0"
    }
  }

  backend "s3" {
    bucket               = "sliderule"
    key                  = "tf-states/search-server.tfstate"
    workspace_key_prefix = "tf-workspaces"
    encrypt              = true
    profile              = "default"
    region               = "us-west-2"
  }
}
