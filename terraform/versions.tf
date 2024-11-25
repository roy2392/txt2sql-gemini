terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
  required_version = ">= 0.12"
}

terraform {
  backend "s3" {
    bucket = "your-terraform-state-bucket"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}
