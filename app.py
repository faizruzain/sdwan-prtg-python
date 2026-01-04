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

# t = []
# df = pd.read_csv('cleaned_csv/temp.csv')
# size = df.get('Temperature Slot 6 - Temp: CP-CPU(RAW)').size
# print(size, type(size))
# columns = df.columns
# for _ in range(size):
#     t.append(_+100)
# print(t)
# df.insert(2, 'cuki', t)
# print(df)
# print(len(columns))