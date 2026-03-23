#!/usr/bin/python3
import aiohttp
import asyncio
import time

async def fetch_async(url, session):
    """
    Asynchronously fetches the content of a given URL

    Args:
        url(str): The URL to fetch
        session(aiohttp.ClientSession):The HTTP session to use for the request
    
    Returns: 
        str: The reposnse text content
    """
    # Use the session to make an asynchronous GET request
    # 'async with' ensures the reponse is properly closed after use
    async with session.get(url) as response:
        # Returns the response body as text(waits for the response to be fully received)
        return await response.text()
    

async def main():
    """
    Main asynchronous function that coordinates fetching multiple web pages concurrently
    """
    # Create an HTTP session that will be used for all requests.
    # The session handles connection pooling and other optimazation.
    async with aiohttp.ClientSession() as session:
        # create two sesisons that will run fetch_async concurrently
        # asyncio.create_task schedules the coroutine to run in the background
        page1= asyncio.create_task(fetch_async('http://example.com', session))
        page2= asyncio.create_task(fetch_async('http://example.org', session))

        #Wait for bth tasks to complete simulataneously
        #asyncio.gather runs multiple coroutines concurrently and returns their results
        await asyncio.gather(page1, page2)


#record the start time before running the asynchronous operations
start_time=time.time()

# Run main asynchronous function
#asyncio.run() creates a new event loop, runs the coroutine and closes the loop
asyncio.run(main())

#Total execution time
print(f"Done in {time.time()-start_time} seconds")

"""
    cmd>> python asynchio_url_fetching.py
Done in 0.40828752517700195 seconds
"""