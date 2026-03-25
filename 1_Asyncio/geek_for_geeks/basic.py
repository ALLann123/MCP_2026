#!/usr/bin/python3
import asyncio

async def fn():
    print('This is')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')

asyncio.run(fn())

"""
    cmd> python basic.py
This is
asynchronous programming
and not multi-threading

"""