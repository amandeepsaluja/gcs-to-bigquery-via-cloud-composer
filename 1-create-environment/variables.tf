
variable "gcp_project_id" {
  type        = string
  description = "Google project ID"
  default     = "gcp-practice-project-aman"
}

variable "gcp_region" {
  type        = string
  description = "Google project region"
  default     = "us-central1"
}

variable "environment_name" {
  type        = string
  description = "Name of the Composer environment"
  default     = "cloud-composer-dev-env"
}

variable "image_version" {
  type        = string
  description = "Composer image version"
  default     = "composer-2-airflow-2"
}

variable "environment_size" {
  type        = string
  description = "Size of the Composer environment"
  default     = "ENVIRONMENT_SIZE_MEDIUM"
}

variable "service_account_email" {
  description = "Service account email to be used by cloud function to access other GCP resources passed via Github secrets"
  type        = string
}
