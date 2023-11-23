import google.oauth2.id_token
import json

import google.auth.transport.requests as google_requests

from airflow import DAG
from airflow.models.param import Param
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator,
)
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.utils.dates import days_ago

# Cloud Function Link
xlsx_to_csv_function = "https://us-central1-gcp-practice-project-aman.cloudfunctions.net/xlsx-to-csv-function"

# authenticating for cloud function call
request = google_requests.Request()
id_token = google.oauth2.id_token.fetch_id_token(request, xlsx_to_csv_function)

# parameters to pass to task
params = {
    "source_excel_bucket": Param("placeholder", type="string"),
    "source_excel_file": Param("placeholder", type="string"),
    "target_csv_bucket": Param("placeholder", type="string"),
    "target_csv_file": Param("placeholder", type="string"),
    "job_source": "Airflow",
}


# default arguments for DAG
default_args = {
    "catchup": False,
    "depends_on_past": False,
    "location": "us-central1",
    "owner": "Aman",
    "params": params,
    "project_id": "gcp-practice-project-aman",
    "retries": 0,
    "start_date": days_ago(0),
    "tags": ["csv", "excel", "gcs", "bigquery", "cloud_function"],
}

# defining the DAG
with DAG(
    "excel_to_bigquery",
    default_args=default_args,
    description="Reads an Excel file from GCS and exports it to BigQuery",
    schedule_interval=None,
) as dag:
    # Add the task to trigger the xlsx-to-csv-function cloud function
    trigger_cf = SimpleHttpOperator(
        task_id="trigger_cloud_function",
        method="POST",
        http_conn_id="cf_xlsx_to_csv_function",
        endpoint="xlsx-to-csv-function",
        headers={
            "Authorization": f"Bearer {id_token}",
            "Content-Type": "application/json",
        },
        data=json.dumps(
            {
                "source_excel_bucket": "{{ params.source_excel_bucket }}",
                "source_excel_file": "{{ params.source_excel_file }}",
                "target_csv_bucket": "{{ params.target_csv_bucket }}",
                "target_csv_file": "{{ params.target_csv_file }}",
                "job_source": "{{ params.job_source }}",
            }
        ),
        dag=dag,
    )

    # Add the task to load the CSV into BigQuery
    gcs_to_bq = GCSToBigQueryOperator(
        task_id="gcs_to_bq",
        bucket="{{ params.target_csv_bucket }}",
        source_objects=["{{ params.target_csv_file }}"],
        destination_project_dataset_table="raw_layer.xlxs_to_csv_pipeline",
        write_disposition="WRITE_APPEND",
        autodetect=True,
        location="US",
        dag=dag,
    )

    trigger_cf >> gcs_to_bq

# this will only work with Gen 1 Cloud Functions
# invoke_cf = CloudFunctionInvokeFunctionOperator(
#     task_id="execute_cloud_function",
#     project_id=,
#     location="us-central1",
#     gcp_conn_id="google_cloud_default",
#     function_id="xlsx-to-csv-function",
#     input_data={
#         "data": json.dumps(
#             {
#                 "source_excel_bucket": "data-bucket-gcp-practice-project-aman",
#                 "source_excel_file": "raw-excel-airflow/sample_data_1.xlsx",
#                 "target_csv_bucket": "data-bucket-gcp-practice-project-aman",
#                 "target_csv_file": "raw-excel-airflow/sample_data_1.csv",
#                 "job_source": "Airflow",
#             }
#         )
#     },
#     dag=dag,
# )
