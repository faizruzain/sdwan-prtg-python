import asyncio
import sys
sys.path.append('my_modules')
import pandas as pd
import requests
import random
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

headers = ['hostname', '','', 'status']
headers[1] = 'temp_id'
headers[2] = 'average_temperature'
headers.insert(3, 'min')
headers.insert(4, 'max')

print(headers)

# print(pd.read_csv('csv/device_id_new.csv'))
# df = pd.read_csv('csv/device_id_new.csv', header=None)
# df = df.drop(index=[0])
# df = df.reset_index(drop=True)
# print(df)


# r = requests.get('https://drive.google.com/uc?id=107Sqmt1sk6oGcKL_TwNVqz5wMJBavsoq&export=download')
# r = requests.get('https://afr-sdwan.free.beeceptor.com/api/prtg?id={_[1]}')
# f = StringIO(r.text)
# df = pd.read_csv(f).get('Name')
# print(df)



# url = 'https://cdn.wsform.com/wp-content/uploads/2020/06/color_srgb.csv'
# url2 = 'https://afr-sdwan.free.beeceptor.com/api/prtg-csv'
# df = pd.read_csv(url2)
# print(df)
# df.to_csv('output_csv/beeceptor.csv')
# for index, int in enumerate(range(5)):
#     randint = []
#     for _ in range(29):
#         randint.append(random.randint(18, 21))
#         randint_df = pd.DataFrame(randint, columns=['cpu_usage'])
#         randint_df.to_csv(f'random_csv/random{index}.csv')
# device_id = pd.read_csv('csv/device_id_dev.csv').get(['hostname', 'cpu_id'])
# df = pd.read_csv('cleaned_csv/cpu.csv')
# average = df.get(['CPU 7(RAW)']).mean().round()
# device_id.insert(2, 'average_cpu_usage', average)
# print(device_id)
