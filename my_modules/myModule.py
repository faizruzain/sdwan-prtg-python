import os
import pandas as pd

def read_csv():
    try:
        script_dir = os.path.dirname(__file__)
        rel_path = "../csv/device_id.csv"
        abs_file_path = os.path.join(script_dir, rel_path)
        # print(abs_file_path)
        df = pd.read_csv(abs_file_path)
        return df
    except error:
        print(error)
    finally:
        print("Reading csv file: Done")
    # print(df)
    # print("\n")
    # print(df.get(["hostname", "ping_id"]))
    # for _ in df.itertuples(index=False):
    #     print(_[0]) #kalau mau mulai dari index 0, tambahkan argumen index=False pada .itertuples()



   


class PRTG():
    def __init__(self,csv_file):
        self.csv_file = csv_file



# async def satu():
#     print('satu')
#     await asyncio.sleep(1)
#     print('done')

# async def dua():
#     print('dua')
#     await asyncio.sleep(1)
#     print('done')