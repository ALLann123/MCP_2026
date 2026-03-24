#!/usr/bin/python3
import asyncio

# A function to simulate an asynchronous operatiion using a Future
async def async_operation(future, data):
    await asyncio.sleep(1) # Simulate some async work with a delay

    # Set the result exception based on the input data
    if data == "success":
        future.set_result("Operation succeeded")
    else:
        future.set_exception(RuntimeError("Operation failed"))

# A callback function to be called when the Future is done
def future_callback(future):
    try:
        print("Callback: ", future.result()) # Attempt to print the result
    except Exception as exc:
        print("Callback: ", exc)  #Print the excetion if there was one


async def main():
    # Create a Future object
    future = asyncio.Future()

    # Add a callback to the future
    future.add_done_callback(future_callback)

    # start the synchronous operation and pass the future
    await async_operation(future, "success") # Try changing "success" to anything else to simulate a failure

    # check if the future is done and print its result
    if future.done():
        try:
            print("Main:", future.result)
        except Exception as exc:
            print("Main: ", exc)

# Run the main coroutine
asyncio.run(main())

"""
    cmd>> python future_asyncio.py
Main: <built-in method result of _asyncio.Future object at 0x00000157E2B457F0>
Callback:  Operation succeeded

"""