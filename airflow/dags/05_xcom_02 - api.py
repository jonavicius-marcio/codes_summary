from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
from datetime import timedelta

#Notice here that we are using the task instance object that is ti to do an xcom push with a desired key name.
def _transform(ti):
   import requests
   resp = requests.get('https://swapi.dev/api/people/1').json()
   print(resp)
   my_character = {}
   my_character["height"] = int(resp["height"]) - 20
   my_character["mass"] = int(resp["mass"]) - 50
   my_character["hair_color"] = "black" if resp["hair_color"] == "blond" else "blond"
   my_character["eye_color"] = "hazel" if resp["eye_color"] == "blue" else "blue"
   my_character["gender"] = "female" if resp["gender"] == "male" else "female"

   ti.xcom_push("character_info", my_character)

#Now we shall instantiate our DAG object, and create dependencies between our two tasks
def _load(ti):
   print(ti.xcom_pull(key = 'character_info',task_ids = '_transform'))

with DAG(
    dag_id='xcoms_02',
    description="DAG de exemplo",
    schedule_interval = timedelta(minutes=5),
    start_date = pendulum.datetime(2023,3,1),
    catchup = False
) as dag:

    t1 = PythonOperator(
        task_id = '_transform',
        python_callable = _transform
    )

    t2 = PythonOperator(
        task_id = 'load',
        python_callable = _load
    )
    t1 >> t2