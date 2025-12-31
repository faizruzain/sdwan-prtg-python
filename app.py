import asyncio
import sys
sys.path.append('my_modules')
import requests
import pandas as pd
import json
import csv
import os
from dotenv import load_dotenv
from myModule import read_csv, get_CPU_usage, get_temperature_records, get_memory_usage

load_dotenv()

# async def main():
#     df = await read_csv()
#     await get_CPU_usage(df)
#     # await get_temperature_records(df)
#     # await get_memory_usage(df)

# asyncio.run(main())
my_token = os.getenv("API_KEY")
id = '59358'
url = f'https://10.164.1.101/api/historicdata.csv?id={id}&avg=86400&sdate=2025-12-01-00-00-00&edate=2025-12-30-23-59-59&apitoken={my_token}'
# r = requests.get(url, verify=False)
# print(r.status_code)
# print(r.encoding)
# avg_str = r.text.find('Averages')
# print(r.text[avg_str::])

# with open('output_csv/ping.csv', 'w') as f:
#     f.write(r.text)

# df = pd.read_csv('output_csv/traffic.csv')
# print(df)
# print(r.text)
# with open('cuki.json', 'w') as f:
#     json.dump(r, f)