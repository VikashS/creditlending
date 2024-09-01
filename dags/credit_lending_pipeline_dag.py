from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'credit_lending_pipeline',
    default_args=default_args,
    description='Credit Lending pipeline with all layer for Bronze, Silver, Gold layers',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
) as dag:

    bronze_layer_flow = KubernetesPodOperator(
        namespace='default',
        image='creditbronzeacr.azurecr.io/bronze:latest',
        name='bronze_layer_flow-job',
        task_id='bronze_layer_flow_task',
        get_logs=True,
        env_vars={
            'AZURE_STORAGE_ACCOUNT': 'credit_storage',
            'AZURE_STORAGE_KEY': '{{ var.value.azure_storage_key }}',
        },
        is_delete_operator_pod=True,
    )

    silver_layer_flow = KubernetesPodOperator(
        namespace='default',
        image='creditsilveracr.azurecr.io/silver:latest',
        name='silver_layer_flow-job',
        task_id='bronze_layer_flow_task',
        get_logs=True,
        env_vars={
            'AZURE_STORAGE_ACCOUNT': 'credit_storage',
            'AZURE_STORAGE_KEY': '{{ var.value.azure_storage_key }}',
        },
        is_delete_operator_pod=True,
    )

    gold_layer_flow = KubernetesPodOperator(
        namespace='default',
        image='creditgoldacr.azurecr.io/gold:latest',
        name='gold_layer_flow-job',
        task_id='bronze_layer_flow_task',
        get_logs=True,
        env_vars={
            'AZURE_STORAGE_ACCOUNT': 'credit_storage',
            'AZURE_STORAGE_KEY': '{{ var.value.azure_storage_key }}',
        },
        is_delete_operator_pod=True,
    )

    bronze_layer_flow >> silver_layer_flow >> gold_layer_flow
