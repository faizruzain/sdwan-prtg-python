import sys
sys.path.append('my_modules')
import asyncio
import myModule
from myModule import read_csv, coba

async def main():
    await read_csv()
    await coba()

asyncio.run(main())












# async def test():
#     await satu()
#     await dua() 

# asyncio.run(test())


