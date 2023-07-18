from airflow import DAG
from airflow.sensors.filesystem import FileSensor
import pendulum

from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import chain, cross_downstream
from datetime import timedelta

# Access the context of the diagram
def _downloading_data(**kwargs):
    print('teste marcio')
    print(kwargs)

def _parans(my_param):
    print(my_param)

def _sensor(my_param):
    with open('/tmp/my_file.txt', w) as f:
        f.write('mydata')

dag_python = DAG(
    dag_id="python_operator",
    description="DAG de exemplo",
    schedule_interval = timedelta(minutes=5),
    start_date = pendulum.datetime(2023, 3, 4, tz="UTC"),
    catchup=False,
)   

downloading_data = PythonOperator(
    task_id = "downloading_data",
    python_callable = _downloading_data,
    dag = dag_python)


downloading_data_2 = PythonOperator(
    task_id = "downloading_data_2",
    python_callable = _downloading_data,
    dag = dag_python)

python_task = PythonOperator(
    task_id = 'python_task', 
    python_callable = _parans, 
    #send parameter
    op_kwargs={'my_param': 45},
    dag = dag_python)

## Função
def _funcao_tosca(context):
    print("deu erro aqui!")
    print(context)
...
## Task chamando a função no caso de falha:
processando_dados = BashOperator(
    task_id='processando_dados',
    bash_command='exit 1',
    on_failure_callback=_funcao_tosca,
    dag = dag_python
    )

""" 
python_task = FileSensor(
    task_id = 'file_sensor', 
    fs_conn_id='fs_defualt2',
    filepath='my_data.txt',
    dag = dag_python) """




#Defininng the sequence 

#downloading_data >> python_task >> processando_dados
#downloading_data << python_task << processando_dados

# mesmo que 
#downloading_data.set_downstream(python_task)
#python_task.set_downstream(processando_dados)

#processando_dados.set_upstream(python_task)
#python_task.set_upstream(downloading_data)

# Chain e cross_downstream

#chain([downloading_data, python_task, processando_dados])

#downloading_data >> [python_task, processando_dados]

cross_downstream([downloading_data, downloading_data_2], [python_task, processando_dados])




