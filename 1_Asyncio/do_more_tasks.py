#!/usr/bin/env python3
import asyncio

async def say_hello_async():
    await asyncio.sleep(2)    #simulate a delay of 2 seconds
    print("Hello, Async World!")    

async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)    #simulate doing something else for 1 second 
    print("Finished another task!")

async def main():
    #schedule both tasks to run concurrently
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )

asyncio.run(main())

"""
    cmd> python do_more_tasks.py
Starting another task...
Finished another task!
Hello, Async World!

"""