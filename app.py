import sys
sys.path.append('my_modules')
import asyncio
import myModule
from myModule import read_csv

df = read_csv()
print(df)
# async def test():
#     await satu()
#     await dua() 

# asyncio.run(test())


