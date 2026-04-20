resource "aws_s3_bucket" "search_bucket" {
  bucket        = var.s3_bucket_name
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "search_bucket_access_block" {
  bucket = aws_s3_bucket.search_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  restrict_public_buckets = true
  ignore_public_acls      = true
}

data "aws_iam_policy_document" "s3_policy" {
  statement {
    actions   = ["s3:GetObject"]
    resources = ["${aws_s3_bucket.search_bucket.arn}/*"]

    principals {
      type        = "AWS"
      identifiers = [aws_cloudfront_origin_access_identity.origin_access_identity.iam_arn]
    }
  }
}

resource "aws_s3_bucket_policy" "search" {
  bucket = aws_s3_bucket.search_bucket.id
  policy = data.aws_iam_policy_document.s3_policy.json
}

# Versioned corpora accumulate on every release rebuild because each
# publishes at a new /docsearch/corpus_<sha>.json key. They DO need
# cleanup eventually, but a naive prefix-only expiration rule would
# delete the currently-live corpus whenever we skip a 30-day deploy
# window — at that point meta.json still points at an object S3 just
# reaped, and every client 404s.
#
# Fix: tag-based filter. scripts/upload.sh tags each corpus as
# state=stale *after* it has been superseded by a subsequent deploy.
# The current corpus is never tagged, so it's never eligible for
# expiration — no matter how long until the next release.
#
# 30 days after creation is the upper bound on "any client could
# still be mid-fetch": meta has max-age=60, and the skill's local
# cache is keyed by sha, so a stale sha is never re-requested from
# this origin. In practice an unreferenced corpus lives 0–30 days
# depending on when the next deploy re-tagged it; that's fine.
#
# The `and { }` block is required when combining prefix + tags into
# one filter (S3 lifecycle's intersection semantics).
resource "aws_s3_bucket_lifecycle_configuration" "search" {
  bucket = aws_s3_bucket.search_bucket.id

  rule {
    id     = "expire-stale-tagged-corpora"
    status = "Enabled"

    filter {
      and {
        prefix = "docsearch/corpus_"
        tags = {
          state = "stale"
        }
      }
    }

    expiration {
      days = 30
    }
  }
}
