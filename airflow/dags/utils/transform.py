import pandas as pd
import json
from pathlib import Path
import os


DIR_READ = 'data/extraction/'
DIR_SAVE = 'data/transform/'

# main_path = Path().absolute().parent
main_path = '/home/marcio/projects/study/airflow/'

base_path = os.path.join(main_path, DIR_READ)
save_path = os.path.join(main_path, DIR_SAVE)


def _read(file_name):
    df = pd.read_json(f"{base_path}{file_name}.json",
                      orient='index').transpose()
    return df


def transform(arg):
    d_1 = _read('d_1')
    d_2 = _read('d_2')
    d_3 = _read('d_3')

    df = pd.concat([d_1, d_1, d_2])

    df['bmi'] = df['mass'] / (df['height']**2)

    df.to_csv(f'{save_path}/people_data.csv')
    print(arg)


if __name__ == '__main__':
    transform()
