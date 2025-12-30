import os
import pandas as pd
import requests
from tabulate import tabulate


async def read_csv():
    try:
        script_dir = os.path.dirname(__file__)
        rel_path = "../csv/device_id.csv"
        abs_file_path = os.path.join(script_dir, rel_path)
        df = pd.read_csv(abs_file_path)
        return df
    except NameError:
        print(NameError)

async def get_CPU_usage(df):
    try:
        CPU_usage = df.get(["hostname", "cpu_id"])
        for _ in CPU_usage.itertuples(index=False):
            # make API req
            r = requests.get(f'https://jsonplaceholder.typicode.com/users/9')
            if r.status_code == 200:
                print(r)

                # print results
                print(tabulate([
                    [_[0], _[1], 'Done']
                ],
                    headers=['hostname', 'cpu_id', 'status'],
                    tablefmt="github"
                    )
                )

                print('\n')
            else:
                print(f'Error occurred with status code: {r.status_code}')
                break
    except NameError:
        print(NameError)
        

async def get_temperature_records(df):
    try:
        print(df)
    except NameError:
        print(NameError)
    else:
        print("Getting Temperature Records: Done")


async def get_memory_usage(df):
    try:
        print("get_memory_usage")
    except NameError:
        print(NameError)
    else:
        print("Getting Memory Usage: Done")