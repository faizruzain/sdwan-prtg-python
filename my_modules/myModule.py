import os
import pandas as pd
import requests

async def read_csv():
    try:
        script_dir = os.path.dirname(__file__)
        rel_path = "../csv/device_id.csv"
        abs_file_path = os.path.join(script_dir, rel_path)
        df = pd.read_csv(abs_file_path)
        print(df)
    except NameError:
        print(NameError)
    else:
        print("Reading csv file: Done")
    # print(df)
    # print("\n")
    # print(df.get(["hostname", "ping_id"]))
    # for _ in df.itertuples(index=False):
    #     print(_[0]) #kalau mau mulai dari index 0, tambahkan argumen index=False pada .itertuples()

async def coba():
    try:
        # r = requests.get("https://dummyjson.com/PRTG?delay=1000")
        r = requests.get("https://api.github.com")
        print(r.json())
    except NameError:
        print(NameError)
    else:
        print("HTTP Get Request: Done")
   





# async def satu():
#     print('satu')
#     await asyncio.sleep(1)
#     print('done')

# async def dua():
#     print('dua')
#     await asyncio.sleep(1)
#     print('done')