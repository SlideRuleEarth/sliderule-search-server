variable "domainApex" {
  description = "Apex domain, e.g. testsliderule.org"
  default     = "testsliderule.org"
}

variable "domainName" {
  description = "Full domain of the search distribution, e.g. search.testsliderule.org"
  default     = "search.testsliderule.org"
}

variable "domain_root" {
  description = "Domain label used in tags, e.g. testsliderule"
  default     = "testsliderule"
}

variable "cost_grouping" {
  description = "Cost tag grouping"
  type        = string
  default     = "search-server"
}
