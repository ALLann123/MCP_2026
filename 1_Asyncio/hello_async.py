#!/usr/bin/env python3

import asyncio
async def say_hello_async():
    await asyncio.sleep(2)
    print("Hello, Async World!")

asyncio.run(say_hello_async())
