# airflow/dags/etl_dag.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.etl_pipeline import main as run_etl_pipeline

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id="etl_pipeline_mock_dag",
    default_args=default_args,
    description="A mock DAG to run the PySpark ETL pipeline",
    schedule_interval="@daily",  # or '0 0 * * *'
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_etl_pipeline
    )
