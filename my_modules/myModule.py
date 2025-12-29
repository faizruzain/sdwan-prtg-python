import asyncio
import os

dir_name = 'csv'

async def list_dir():
    await print(os.listdir(dir_name))

class PRTG():
    def __init__(self,csv_file):
        self.csv_file = csv_file



async def satu():
    print('satu')
    await asyncio.sleep(1)
    print('done')

async def dua():
    print('dua')
    await asyncio.sleep(1)
    print('done')