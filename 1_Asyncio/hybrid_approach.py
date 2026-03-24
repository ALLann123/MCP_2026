#!/usr/bin/python3
import asyncio
import time

def sync_task():
    """
    Synchronous Function simulates a long-running task
    This function will block the thread it runs on for 5 seconds

    NOTe: In an async application, running this directly would block
    the event loop, 
    preventing other async tasks from running concurrently
    """
    print("Starting a slow sync task...")
    time.sleep(5)  #Simulates a long-running I/O operation or CPU intensive task
    # This is a blocking call
    print("Finished the slow task.")

async def async_wrapper():
    """
    Async wrapper that offloads thhe synchronous blocking function 
    to a separate thread.
    This allows the blocking operation to run without blocking 
    the async event loop

    How it works:
    1. Gets the current running event loop
    2. Uses run_in_executor() to execute the synchronous function
    in thread pool
    3. The 'await' yields control back to the event loop while the
    thread runs
    4. The event loop can continue running other async tasks during the 5-second
    sleep
    """
    # Get the currently running asyncio event loop
    # This is the loop that manages all async tasks
    loop = asyncio.get_running_loop()

    # Run the Synchronous function in a thread pool executor
    # -First Parameter: executor(None= Use default ThreadPool executor)
    # -Second Paramter: Function to execute (sync_task)
    # -Additional arguments can be passed to sync_task after the function name
    # Creates a thread, runs sync_task() there and returns a future that
    # will complete when the thread finishes. The 'await' makes this coroutine
    # wait for the thread to complete without blocking the event loop
    await loop.run_in_executor(None, sync_task)

async def main():
    """
    Main async entry point that orchestrates concurrent execution
    Uses asyncio.gather() to run multiple async tasks concurrently
    """
    # asyncio.gather() runs multiple awaitable objects concurrently
    # It returns when all tasks are complete
    # Even though we only have one wrapper here, this pattern allows easily
    # adding mmore concurrent tasks in the future(e.g.m network requests, file I/O)
    await asyncio.gather(
        async_wrapper(),  #Offloads the blocking sync_task to a thread
        # Additional async tasks can be added here to run concurrently
        # For example:
        # async_network_request(),
        # async_file_operation(),
    )

# Entry point to the script
# asyncio.run() creates a new event loop, runs the main() coroutine, and cleans uo
asyncio.run(main())

"""
    cmd>>python hybrid_approach.py
Starting a slow sync task...
Finished the slow task.

"""