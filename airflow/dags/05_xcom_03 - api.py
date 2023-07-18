from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
import pendulum
from datetime import timedelta


with DAG(
    dag_id='xcoms_03',
    description="DAG de exemplo",
    schedule_interval = timedelta(minutes=5),
    start_date = pendulum.datetime(2023,3,1),
    catchup = False
) as dag:
    #Notice here that we are using the task instance object that is ti to do an xcom push with a desired key name.
    @task()
    def _transform():
        import requests
        resp = requests.get('https://swapi.dev/api/people/1').json()
        print(resp)
        my_character = {}
        my_character["height"] = int(resp["height"]) - 20
        my_character["mass"] = int(resp["mass"]) - 50
        my_character["hair_color"] = "black" if resp["hair_color"] == "blond" else "blond"
        my_character["eye_color"] = "hazel" if resp["eye_color"] == "blue" else "blue"
        my_character["gender"] = "female" if resp["gender"] == "male" else "female"

        return my_character

    #Now we shall instantiate our DAG object, and create dependencies between our two tasks
    @task()
    def _load(character_info: str):
       print(character_info)


    _load(_transform())
    #_transform() >> (_load)