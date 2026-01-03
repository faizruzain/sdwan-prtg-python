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

# Temp
# files = listdir('output_csv')
# print(len(files))
# for file in files:
#     df = pd.read_csv(f'output_csv/{file}', index_col=False, encoding='unicode_escape')
#     df.to_csv(f'cleaned_csv/{file}', index_label=None, index=False, encoding='utf-8')
#     print(f'file name: {file}')
#     print(df)
#     print('\n')