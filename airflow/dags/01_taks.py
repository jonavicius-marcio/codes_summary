from airflow.decorators import task
from airflow import DAG
from datetime import datetime

with DAG(
        dag_id="task",
        start_date=datetime(2022, 1, 1),
        schedule_interval="@daily",
        catchup=False,
) as dag:
    @task()
    def get_name():
        return {
            'first_name': 'Hongbo',
            'last_name': 'Miao',
        }

    get_name()