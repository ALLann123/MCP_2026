#!/usr/bin/python3
import asyncio

async def say_hello():
    print("Hello...")
    #pause execution until result is ready
    await asyncio.sleep(2)
    print("WOrld")

asyncio.run(say_hello())


