import functions_framework
import google.auth
import requests
import yaml

from google.auth.transport.requests import AuthorizedSession
from typing import Any


AUTH_SCOPE = "https://www.googleapis.com/auth/cloud-platform"
CREDENTIALS, _ = google.auth.default(scopes=[AUTH_SCOPE])


@functions_framework.cloud_event
def get_file_details(cloudevent):
    # Getting payload data from the Cloud Storage event
    payload = cloudevent.data.get("protoPayload")
    resource_name = payload.get("resourceName")

    # extracting full gcs path from resource name
    full_gcs_path = "gs://" + resource_name.split("/", maxsplit=3)[-1].replace(
        "/objects", ""
    )
    gcs_bucket_name = full_gcs_path.split("/", maxsplit=3)[2]
    excel_source = full_gcs_path.split("/", maxsplit=3)[-1]
    csv_target = excel_source.replace(".xlsx", ".csv")

    # parsing configuration
    with open("config.yaml", "r") as yaml_file:
        config_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

    web_server_url = config_data["AIRFLOW_SERVER_URL"]
    dag_id = config_data["DAG_ID"]

    function_data = {
        "source_excel_bucket": gcs_bucket_name,
        "source_excel_file": excel_source,
        "target_csv_bucket": gcs_bucket_name,
        "target_csv_file": csv_target,
    }

    return trigger_dag(web_server_url=web_server_url, dag_id=dag_id, data=function_data)


def make_composer2_web_server_request(
    url: str, method: str = "GET", **kwargs: Any
) -> google.auth.transport.Response:
    authed_session = AuthorizedSession(CREDENTIALS)

    # Set the default timeout, if missing
    if "timeout" not in kwargs:
        kwargs["timeout"] = 90

    return authed_session.request(method, url, **kwargs)


def trigger_dag(web_server_url: str, dag_id: str, data: dict) -> str:
    endpoint = f"api/v1/dags/{dag_id}/dagRuns"
    request_url = f"{web_server_url}/{endpoint}"
    json_data = {"conf": data}

    response = make_composer2_web_server_request(
        request_url, method="POST", json=json_data
    )

    if response.status_code == 403:
        raise requests.HTTPError(
            "You do not have a permission to perform this operation. "
            "Check Airflow RBAC roles for your account."
            f"{response.headers} / {response.text}"
        )
    elif response.status_code != 200:
        response.raise_for_status()
    else:
        return response.text
