from airflow import DAG
from task_group import (create_task_group as create_bi_task_group,)
from utils.exctraction_aux import extract_aux
from airflow.operators.python import PythonOperator

'''
essa dag importa a função o modulo task_group que agrupa tasks.
Já o modulo extract_aux serve para ler uma api e salvar o dado
'''

import pendulum
from datetime import timedelta


dag = DAG(
    dag_id='boa_praticas_task_group',
    description="DAG groups",
    schedule_interval=timedelta(minutes=5),
    start_date=pendulum.datetime(2023, 3, 1),
    max_active_runs=1,
)

    
with dag:

    task2 = PythonOperator(
        task_id='extract_aux',
        python_callable=extract_aux,
        dag=dag
    )

    bi_task_group = create_bi_task_group('passe_argumento')
    extract_aux_task = task2

    # dependencies
    bi_task_group >> extract_aux_task
