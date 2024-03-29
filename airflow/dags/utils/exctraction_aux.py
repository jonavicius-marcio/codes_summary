import requests
import json
from pathlib import Path
import os

DIR = 'data/extraction/'

# main_path = Path().absolute().parent
main_path = '/home/marcio/projects/study/airflow/'

base_path = os.path.join(main_path, DIR)
print('###########')
print(base_path)


def _exctraction(id):
    resp = requests.get(f'https://swapi.dev/api/people/{id}').json()
    my_character = {}
    my_character["height"] = int(resp["height"]) - 20
    my_character["mass"] = int(resp["mass"]) - 50
    my_character["hair_color"] = "black" if resp["hair_color"] == "blond" else "blond"
    my_character["eye_color"] = "hazel" if resp["eye_color"] == "blue" else "blue"
    my_character["gender"] = "female" if resp["gender"] == "male" else "female"
    return my_character


def _save(file, name):
    d_object = json.dumps(file, indent=4)
    with open(f"{base_path}{name}.json", "w") as outfile:
        outfile.write(d_object)


def extract_aux():
    d_4 = _exctraction(3)

    _save(d_4, 'd_4')
    print('data saved')


if __name__ == '__main__':
    extract_aux()
