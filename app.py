import asyncio
import sys
sys.path.append('my_modules')
import pandas as pd
import requests
import random
from os import listdir
from myModule import read_csv, get_things_done_fast
from io import StringIO

async def main():
    print('Choose one of them!:')
    print("""
1 = CPU Data
2 = Memory Data
3 = Ping Data
4 = Temperature Data
5 = Traffic Data
""")
    user_input = int(input('Choose 1 to 5: '))
    df = await read_csv()
    await get_things_done_fast(df, user_input)

asyncio.run(main())

# loc = [['Ping Time(RAW)', 'Minimum(RAW)', 'Maximum(RAW)', 'Packet Loss(RAW)']]
# hostnames_df = pd.read_csv('csv/device_id_new.csv', index_col=False)
# hostnames_df = hostnames_df.get(['hostname', 'cpu_id'])
# print(hostnames_df)
# for _ in hostnames_df.itertuples():
#     print(_[0])

# data_df = pd.read_csv('cleaned_csv/ping.csv', index_col=False)
# data_s = round(data_df.get(['Ping Time(RAW)', 'Minimum(RAW)', 'Maximum(RAW)', 'Packet Loss(RAW)']).mean())
# print(data_s)
# data=[]
# for _ in data_s:
#     data.append(_)
# print(data)
# hostnames_df.loc[[0], loc[0]] = data
# print(data_s)
# print(hostnames_df)
