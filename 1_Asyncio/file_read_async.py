#!/usr/bin/python3
import asyncio
import aiofiles
import time

start_time=time.time()

# Asynchronously reading a single file
async def read_file_async(filepath):
    """
    Asynchronously reads the entire contents of a single file

    Args:
        filepath(str) : Path to the file to read
    
    Returns:
        str: The complete contents of the file as a string
    """
    # Use aiofiles to open the file asynchronously in read mode
    # The 'async with' context manager ensures proper cleanup even if errors occur
    async with aiofiles.open(filepath, 'r') as file:
        # Asynchronously read the entire file contents
        # This doesnt block the event loop while waiting for I/O operations
        return await file.read()
    
async def read_all_async(filepaths):
    """
    Asynchronously reads multiple files concurrently

    Args:
        filepaths(list): List of file paths to read

    Returns: 
        List: List of file contents in the same order as input filepaths
    """
    # Create a list of coroutine tasks, one for each file to read
    # Each task will run read_file_asnc() for its respective file
    tasks = [read_file_async(filepath) for filepath in filepaths]

    # Run all tasks concurrently and wait for all to complete
    # asyncio.gather() runs tasks in parallel and returns results in order
    # This is more efficient than reading files sequentially
    return await asyncio.gather(*tasks)

# Running the async function
async def main():
    """
    Main entry point for the async program.
    Orchestrates reading multiple files asynchronously
    """
    # Define the list of files to read
    filepaths=['file1.txt', 'file2.txt']

    # Read all files concurrently using the async function
    # This will execute both file reads in parallel
    data =  await read_all_async(filepaths)

    # Print the contents of all files (list of strings)
    print(data)

# Call the entry point of our script
asyncio.run(main())
print("\n")
print(f"Time taken: {time.time()-start_time} seconds")

"""
    cmd>> python file_read_async.py
['"hello world" \n', '"Welcome to New York" \n']


Time taken: 0.0610048770904541 seconds

"""
