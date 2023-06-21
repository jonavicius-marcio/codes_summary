from airflow import DAG
#from airflow.operators.empty import EmptyOperator
import pendulum

from custom_operator.hello_operator import HelloOperator
from datetime import timedelta

""" default_args = {
    'retry': 2,
    'reatry_delay': timedelta(minutes=5)
} """
    
with DAG(
    dag_id="simple_dag",
    description="DAG de exemplo para o conceito de Branching",
    #start_date=airflow.utils.dates.days_ago(14),
    #schedule_interval='*/5 * * * *',
    #schedule_interval=None
    schedule_interval = timedelta(minutes=5),
    start_date = pendulum.datetime(2023, 3, 4, tz="UTC"),
    catchup=False, # run the dag from stared date until atcual day.


) as dag: 
    
    hello_task_1 = HelloOperator(
        task_id="sample-task_1",
        name="marcio lindo",
         )
    
    hello_task_2 = HelloOperator(
        task_id = "sample-task_2",
        name = "marcio lindo",
         )
    
    hello_task_3 = HelloOperator(
        task_id="sample-task_3",
        name="marcio lindo",
            )


 # https://crontab.guru/ 