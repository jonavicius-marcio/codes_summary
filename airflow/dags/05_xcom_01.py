from airflow import DAG
from airflow.decorators import task
import pendulum
from datetime import timedelta

from airflow.operators.python import PythonOperator


with DAG(
    dag_id="xcom_01",
    description="DAG de exemplo",
    schedule_interval = timedelta(minutes=5),
    start_date = pendulum.datetime(2023, 3, 4, tz="UTC"),
    catchup=False,
) as dag:

    # envia o arquivo para ser compartihado
    @task()
    def carlos_taks(ti= None):
        ti.xcom_push(key='mobile_phone', value = 'iphone')

    @task()
    def maria_taks(ti= None):
        ti.xcom_push(key='mobile_phone', value = 'iphone')



    @task()
    def fabio_taks(ti= None):
        phone = ti.xcom_pull(task_ids = ['carlos_taks', 'maria_taks'],  key='mobile_phone')
        print(phone)

    carlos_taks() >> maria_taks() >> fabio_taks()
    
    
    

