import pandas as pd
import requests
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()

"""
1 = CPU Data
2 = Memory Data
3 = Ping Data
4 = Temperature Data
5 = Traffic Data
"""

async def read_csv():
    try:
        df = pd.read_csv('csv/device_id_dev.csv')
        print(df)
        return df
    except NameError:
        print(NameError)

async def get_CPU_usage(df, user_input):
    try:
        print(f'User chose: {user_input}')
        # my_token = os.getenv("API_KEY")
        # r = requests.get(url, verify=False)
        # print(r.status_code)
        # print(r.encoding)
        # avg_str = r.text.find('Averages')
        # print(r.text[avg_str::])

        # with open('output_csv/ping.csv', 'w') as f:
        #     f.write(r.text)
        rows = df.get(["hostname"])
        rows = rows.size
        count = 1
        CPU_usage = df.get(["hostname", "cpu_id"])
        # print(f'{count}/{rows}')
        table = []
        headers = ['hostname', 'cpu_id', 'status']
        for _ in CPU_usage.itertuples(index=False):
            # make API req
            # url = f'https://10.164.1.101/api/historicdata.csv?id={_[1]}&avg=86400&sdate=2025-12-01-00-00-00&edate=2025-12-30-23-59-59&apitoken={my_token}'
            # r = requests.get(url, verify=False)
            r = requests.get(f'https://jsonplaceholder.typicode.com/users/9')
            if r.status_code == 200:
                # print(r)
                table.append([_[0], _[1], 'Done'])
                print(tabulate(table, headers, tablefmt='simple_grid'))
                print(f'{count} of {rows}')
                count += 1
                print('\n')
            elif r.status_code != 200:
                count += 1
                print(f'The sensor ID: {_[1]} is not right.')
                print('\n')
                table.append([_[0], _[1], 'Skipped'])
                print(tabulate(table, headers, tablefmt='simple_grid'))
                print('\n')
                continue
            else:
                print(f'Error occurred with status code: {r.status_code}')
                break
    except NameError:
        print(NameError)
    else:
        print('All Done')
        

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