resource "google_composer_environment" "default" {
  name   = var.environment_name
  region = var.gcp_region
  config {
    software_config {
      image_version = var.image_version
    }

    node_config {
      service_account = var.service_account_email
    }

    environment_size = var.environment_size
  }
}
