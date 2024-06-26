variable "environment" {
  description = "Environment name"
  type        = string

  default = ""
}

variable "region" {
  description = "AWS Region where resources will be deployed"
  type        = string

  default = ""
}

variable "tags" {
  description = "Tags to be applied to resources"
  type        = map(string)

  default = {}
}