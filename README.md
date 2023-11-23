# gcs-to-bigquery-via-cloud-composer

## References

- Airflow

  - https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/sensors.html
  - https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html
  - https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/transfers/gcs_to_bigquery/index.html

- Articles/Blogs/StackOverflow/Videos

  - https://dxhero.io/a-centralised-approach-to-cicd-of-dags-on-google-cloud-composer-with-google-cloud-build-part-1/
  - https://www.youtube.com/watch?v=ZgTf523XM0g&ab_channel=ApacheAirflow
  - https://www.youtube.com/watch?v=RrKXZcKOz4A&ab_channel=GoogleCloudTech
  - https://www.youtube.com/watch?v=ueBKItTJ5eg&ab_channel=GoogleOpenSource
  - https://www.youtube.com/watch?v=0bbxf7fpZiQ
  - https://programmaticponderings.com/2021/12/14/devops-for-dataops-building-a-ci-cd-pipeline-for-apache-airflow-dags/
  - https://stackoverflow.com/questions/54110539/cloud-composer-missing-variables-file
  - https://stackoverflow.com/questions/71293807/composer-doesnt-use-imported-variable
  - https://stackoverflow.com/questions/54237270/import-variables-using-json-file-in-google-cloud-composer
  - https://notebook.community/GoogleCloudPlatform/training-data-analyst/courses/machine_learning/deepdive/10_recommend/labs/composer_gcf_trigger/composertriggered
  - https://lakefs.io/blog/airflow-lakefs-integration-guide/
  - https://stackoverflow.com/questions/69131840/how-to-invoke-a-cloud-function-from-google-cloud-composer

- GitHub

  - https://github.com/jaketf/ci-cd-for-data-processing-workflow/tree/master/composer/dags
  - https://github.com/GoogleCloudPlatform/professional-services/tree/main/examples/cloud-composer-cicd
  - https://github.com/kevenpinto/composer_cicd
  - https://github.com/garystafford/tickit-data-lake-demo/tree/main
  - https://github.com/jw-ng/airflow-dynamic-dags/tree/main

- Google Cloud Platform

  - https://cloud.google.com/composer/docs/concepts/overview
  - https://cloud.google.com/composer/docs/triggering-dags
  - https://cloud.google.com/composer/docs/dag-cicd-integration-guide
  - https://cloud.google.com/composer/docs/configure-email
  - https://www.googlecloudcommunity.com/gc/Data-Analytics/Changing-cloud-composer-variables-with-ci-cd/m-p/648555
  - https://cloud.google.com/sdk/gcloud/reference/composer/environments/run
  - https://cloud.google.com/composer/docs/composer-2/triggering-with-gcf

- Terraform

  - https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/composer_environment

- Troubleshooting

  - https://github.com/twosixlabs/armory/issues/156
  - https://github.com/apache/airflow/discussions/32688
