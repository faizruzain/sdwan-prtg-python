import asyncio
import sys
import requests
import pandas as pd
import json
sys.path.append('my_modules')
from myModule import read_csv, get_CPU_usage, get_temperature_records, get_memory_usage

async def main():
    df = await read_csv()
    await get_CPU_usage(df)
    # await get_temperature_records(df)
    # await get_memory_usage(df)

asyncio.run(main())

# r = requests.get(f'https://jsonplaceholder.typicode.com/users/').json()
# # print(r)
# with open('cuki.json', 'w') as f:
#     json.dump(r, f)