import asyncio
import sys
sys.path.append('my_modules')
from myModule import read_csv, get_things_done_fast

async def main():
    print('Choose one of them!:')
    print("""
1 = CPU Data
2 = Memory Data
3 = Ping Data
4 = Temperature Data
5 = Traffic Data
6 = DUDUK MANIS ONGKANG - ONGKANG KAKI
""")
    user_input = int(input('Choose 1 to 6: '))
    sdate = input('Start Date [yyyy-mm-dd-hh-mm-ss]: ')
    print(sdate)
    edate = input('End Date [yyyy-mm-dd-hh-mm-ss]: ')
    print(edate)
    df = await read_csv()
    if user_input == 6:
        for i in range(5):
            await get_things_done_fast(df, i+1)
    else:
        await get_things_done_fast(df, user_input)

asyncio.run(main())