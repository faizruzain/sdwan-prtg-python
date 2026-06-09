import pandas as pd
import requests
import os
import datetime
import urllib3
from dotenv import load_dotenv
from tabulate import tabulate
from io import StringIO

load_dotenv()
urllib3.disable_warnings()

"""
1 = CPU Data
2 = Memory Data
3 = Ping Data
4 = Temperature Data
5 = Traffic Data
"""

async def read_csv(user_input):
    try:
        if user_input == 7:
            df = pd.read_csv('csv/dwdm-per-port.csv')
            return df
        elif user_input == 8:
            pass
        else:
            df = pd.read_csv('csv/device_id_dev.csv', header=None)
            # df = pd.read_csv('csv/device_id_new.csv', header=None)
            df = df.drop(index=[0])
            df = df.reset_index(drop=True)
            return df
    except NameError:
        print(NameError)

async def get_things_done_fast(df, user_input, sdate, edate):
    try:
        print(f'User chose: {user_input}')
        my_token = os.getenv("API_KEY")
        hostnames = df.get([0])
        print(hostnames)
        rows = hostnames.size
        count = 1
        task_lists = df.get([0, user_input])
        what_to_get = []
        file_name = ''
        table = []
        headers = ['hostname', 'status']
        loc = []
        if user_input == 1:
            loc.insert(0, ['average_cpu'])
            what_to_get.append(['CPU 7(RAW)'])
            file_name = f'cpu_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'cpu_id')
            headers.insert(2, 'average_cpu')
        elif user_input == 2:
            loc.insert(0, ['average_memory'])
            what_to_get.append(['Percent Available Memory 1 (Processor)(RAW)'])
            file_name = f'memory_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'mem_id')
            headers.insert(2, 'average_memory')
        elif user_input == 3:
            loc.insert(0, ['Ping Time(RAW)', 'Minimum(RAW)', 'Maximum(RAW)', 'Packet Loss(RAW)'])
            what_to_get.append(['Ping Time(RAW)', 'Minimum(RAW)', 'Maximum(RAW)', 'Packet Loss(RAW)'])
            file_name = f'ping_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'ping_id')
            headers.insert(2, 'average_ping')
        elif user_input == 4:
            loc.insert(0, ['min', 'max', 'average_temperature'])
            what_to_get.append(['Temperature Slot 6 - Temp: CP-CPU(RAW)'])
            file_name = f'temperature_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'temp_id')
            headers.insert(2, 'average_temperature')
            headers.insert(3, 'min')
            headers.insert(4, 'max')
        elif user_input == 5:
            loc.insert(0, ['Traffic Total (Volume)(RAW)', 'Traffic Total (Speed)(RAW)', 'Traffic In (Volume)(RAW)', 'Traffic Out (Volume)(RAW)'])
            what_to_get.append(['Traffic Total (Volume)(RAW)', 'Traffic Total (Speed)(RAW)', 'Traffic In (Volume)(RAW)', 'Traffic Out (Volume)(RAW)'])
            file_name = f'traffic_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}'
            headers.insert(1, 'traffic_id')
            headers.insert(2, 'average_traffic')
            
        for _ in task_lists.itertuples():
            # make API req
            url2 = f'https://afr-sdwan.free.beeceptor.com/api/prtg/id/{_[2]}'
            url1 = f'https://10.164.1.101/api/historicdata.csv?id={_[2]}&avg=86400&sdate={sdate}&edate={edate}&apitoken={my_token}'
            url3 = f'https://jsonplaceholder.typicode.com/users/9'
            # r = requests.get(url, verify=False)
            r = requests.get(url1, timeout=60, verify=False)
            if r.status_code == 200 and 'csv' in r.headers['Content-Type'].lower():
                data = []
                r_f = StringIO(r.text)
                r_df = pd.read_csv(r_f)
                r_df = r_df.get(what_to_get[0])
                if user_input == 4: # Temperature
                    min = r_df.min().iloc[0]
                    max = r_df.max().iloc[0]
                    data.append(min)
                    data.append(max)
                r_df = round(r_df.mean())                
                for d in r_df:
                    data.append(d)
                hostnames.loc[_[0], loc[0]] = data
                table.append([_[1], _[2], r_df, 'Done'])
                print(tabulate(table, headers, tablefmt='simple_grid'))
                print(f'{count} of {rows}')
                count += 1
                print('\n')
            elif r.status_code != 200 or 'csv' in r.headers['Content-Type'].lower():
                table.append([_[1], _[2], 'NaN', 'Skipped'])
                print(tabulate(table, headers, tablefmt='simple_grid'))
                print(f'{count} of {rows}')
                count += 1
                print('\n')
                continue
            else:
                print(f'Error occurred with status code: {r.status_code} and Content-Type: {r.headers['Content-Type']}')
                break
    except NameError:
        print(NameError)
    else:
        print('All Done')
    finally:
        # saving data to csv regardless success or error
        # print(hostnames)
        hostnames.to_csv(f'output_csv/{file_name}.csv', index=False)

async def dwdm_telkom(df):
    try:
        print(df)

    except NameError:
        print(NameError)