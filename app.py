import sys
import asyncio
sys.path.append('my_modules')

import myModule
from myModule import satu,dua,list_dir

async def test():
    await satu()
    await dua()
    await list_dir()


asyncio.run(test())


