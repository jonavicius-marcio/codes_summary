from airflow import DAG
from airflow.utils.task_group import TaskGroup
from airflow.operators.python_operator import PythonOperator

# import business rules
from utils.exctraction import extract
from utils.transform import transform

'''
Esse modulo faz a extração de informações de uma api e depois outra função faz uma tranformação
'''

def create_task_group(argumento):
    with TaskGroup("bi") as bi_task_group:

        extract_raw_task = PythonOperator(
            task_id="extract_fact_raw",
            provide_context=True,
            python_callable=extract,
            op_kwargs={
                "exemplo de argumento",
            },
        )

        transform_task = PythonOperator(
            task_id="transform",
            provide_context=True,
            python_callable=transform,
            # op_kwargs={
            #    "region": region,
            # },
        )

        extract_raw_task >> transform_task

    return bi_task_group
