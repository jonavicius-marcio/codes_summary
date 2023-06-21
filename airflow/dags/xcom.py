from airflow import DAG
#from airflow.operators.empty import EmptyOperator
import pendulum

from airflow.operators.python import PythonOperator
from datetime import timedelta

def _downloading_data():
    print('teste marcio')

dag_python = DAG(
    dag_id="xcom",
    description="DAG de exemplo",
    schedule_interval = timedelta(minutes=5),
    start_date = pendulum.datetime(2023, 3, 4, tz="UTC"),
    catchup=False,
)   

downloading_data = PythonOperator(
    task_id="downloading_data",
    python_callable = _downloading_data
        )
python_task = PythonOperator(task_id='python_task', python_callable=_downloading_data, dag=dag_python)
