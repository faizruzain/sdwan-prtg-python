import asyncio
import sys
sys.path.append('my_modules')
import pandas as pd
import requests
import random
from os import listdir
from myModule import read_csv, get_things_done_fast
from io import StringIO

# async def main():
#     print('Choose one of them!:')
#     print("""
# 1 = CPU Data
# 2 = Memory Data
# 3 = Ping Data
# 4 = Temperature Data
# 5 = Traffic Data
# """)
#     user_input = int(input('Choose 1 to 5: '))
#     df = await read_csv()
#     await get_things_done_fast(df, user_input)

# asyncio.run(main())
hostname_df = pd.read_csv('csv/device_id_new.csv', index_col=False)
hostname_df = hostname_df.get(['hostname', 'cpu_id'])
# rows = hostname_df.size
# temporary = []

# for row in range(rows):
#     temporary.append(0)

# print(temporary)
# hostname_df.insert(1, 'temporary', temporary)
hostname_df.loc[[0],['temporary', 'qwerty']] = [12312, 'polo']
# hostname_df.to_csv('output_csv/temporary.csv', index=False)
print(hostname_df)
# print('\n')
# df = pd.read_csv('cleaned_csv/traffic.csv', index_col=False)
# df = df.get(['Traffic Total (Volume)(RAW)', 'Traffic Total (Speed)(RAW)', 'Traffic In (Volume)(RAW)', 'Traffic Out (Volume)(RAW)'])
# df = df.mean()
# print(df)
