import asyncio
import sys
sys.path.append('my_modules')
import pandas as pd
import requests
from myModule import read_csv, get_CPU_usage, get_temperature_records, get_memory_usage

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
#     await get_CPU_usage(df, user_input)
#     # await get_temperature_records(df)
#     # await get_memory_usage(df)

# asyncio.run(main())


# r = requests.get('https://cdn.wsform.com/wp-content/uploads/2020/06/color_srgb.csv')
# print(r.status_code)
# print(r.content)
url = 'https://cdn.wsform.com/wp-content/uploads/2020/06/color_srgb.csv'
url2 = 'https://afr-sdwan.free.beeceptor.com/api/prtg-csv'
df = pd.read_csv(url2)
print(df)
df.to_csv('output_csv/beeceptor.csv')

# df = pd.read_csv('cleaned_csv/temp.csv')
# print(df)
# df.to_csv('output_csv/traffic.csv')
# print(r.text)
# with open('cuki.json', 'w') as f:
#     json.dump(r, f)
# encoding='unicode_escape'