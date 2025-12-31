import asyncio
import sys
sys.path.append('my_modules')
import pandas as pd

from myModule import read_csv, get_CPU_usage, get_temperature_records, get_memory_usage

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
    await get_CPU_usage(df, user_input)
    # await get_temperature_records(df)
    # await get_memory_usage(df)

asyncio.run(main())


# df = pd.read_csv('cleaned_csv/temp.csv')
# print(df)
# df.to_csv('cleaned_csv/traffic.csv')
# print(r.text)
# with open('cuki.json', 'w') as f:
#     json.dump(r, f)
# encoding='unicode_escape'