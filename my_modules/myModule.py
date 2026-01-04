import pandas as pd
import requests
import random
import os
import datetime
from dotenv import load_dotenv
from tabulate import tabulate
from io import StringIO

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
        df = pd.read_csv('csv/device_id_dev.csv', header=None)
        # df = pd.read_csv('csv/device_id_new.csv', header=None)
        df = df.drop(index=[0])
        df = df.reset_index(drop=True)
        print(df)
        return df
    except NameError:
        print(NameError)

async def get_things_done_fast(df, user_input):
    try:
        print(f'User chose: {user_input}')
        my_token = os.getenv("API_KEY")
        # r = requests.get(url, verify=False)
        hostnames = df.get([0])
        print(hostnames)
        rows = hostnames.size
        count = 1
        task_lists = df.get([0, user_input])
        # print(f'{count}/{rows}')
        what_to_get = ''
        file_name = ''
        table = []
        headers = ['hostname', 'status']
        if user_input == 1:
            what_to_get = 'CPU 7(RAW)'
            file_name = f'cpu_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'cpu_id')
            headers.insert(2, 'average_cpu')
        elif user_input == 2:
            what_to_get = 'Percent Available Memory 1 (Processor)(RAW)'
            file_name = f'memory_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'mem_id')
            headers.insert(2, 'average_memory')
        elif user_input == 3:
            what_to_get = ['Ping Time(RAW)', 'Minimum(RAW)', 'Maximum(RAW)', 'Packet Loss(RAW)']
            file_name = f'ping_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'ping_id')
            headers.insert(2, 'average_ping')
        elif user_input == 4:
            what_to_get = 'Temperature Slot 6 - Temp: CP-CPU(RAW)'
            file_name = f'temperature_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'temp_id')
            headers.insert(2, 'average_temperature')
            headers.insert(3, 'min')
            headers.insert(4, 'max')
        elif user_input == 5:
            what_to_get = ['Traffic Total (Volume)(RAW)', 'raffic Total (Speed)(RAW)', 'Traffic In (Volume)(RAW)', 'Traffic Out (Volume)(RAW)']
            file_name = f'traffic_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'traffic_id')
            headers.insert(2, 'average_traffic')
        gathered_val = []

        for _ in task_lists.itertuples(index=False):
            # make API req
            url2 = f'https://afr-sdwan.free.beeceptor.com/api/prtg?id={_[1]}'
            url1 = f'https://10.164.1.101/api/historicdata.csv?id={_[1]}&avg=86400&sdate=2025-12-01-00-00-00&edate=2025-12-30-23-59-59&apitoken={my_token}'
            url3 = f'https://jsonplaceholder.typicode.com/users/9'
            # r = requests.get(url, verify=False)
            r = requests.get(url2, timeout=10)
            r_f = StringIO(r.text)
            r_df = pd.read_csv(r_f)
            # what_to_get
            r_df = r_df.get('cpu_usage')
            r_df = round(r_df.mean())
            gathered_val.append(r_df)

            if r.status_code == 200:
                table.append([_[0], _[1], r_df, 'Done'])
                print(tabulate(table, headers, tablefmt='simple_grid'))
                print(f'{count} of {rows}')
                count += 1
                print('\n')
            elif r.status_code != 200:
                count += 1
                print(f'Something is not right')
                print('\n')
                table.append([_[0], _[1], r_df, 'Skipped'])
                print(tabulate(table, headers, tablefmt='simple_grid'))
                print('\n')
                continue
            else:
                print(f'Error occurred with status code: {r.status_code}')
                break
        # df.insert(2, headers[1], gathered_val)
        print(f'{headers[2]} {gathered_val}')
        # final data to save
        # hostnames.insert(1, headers[2], gathered_val)
    except NameError:
        print(NameError)
    else:
        print('All Done')
    finally:
        # saving data to csv regardless success or error
        hostnames.insert(1, headers[2], gathered_val)
        hostnames.to_csv(f'output_csv/{file_name}.csv', index_label=None)