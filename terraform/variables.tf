variable "domainApex" {
  description = "Apex domain, e.g. slideruleearth.io"
  default     = "slideruleearth.io"
}

variable "domainName" {
  description = "Full domain of the search distribution, e.g. search.slideruleearth.io"
  default     = "search.slideruleearth.io"
}

variable "domain_root" {
  description = "Domain label used in tags, e.g. slideruleearth"
  default     = "slideruleearth"
}

variable "cost_grouping" {
  description = "Cost tag grouping"
  type        = string
  default     = "search-server"
}
