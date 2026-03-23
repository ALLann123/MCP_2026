#!/usr/bin/python3
import requests
import time

start_time=time.time()

def fetch(url):
    return requests.get(url).text

page1=fetch('http://example.com')
page2=fetch('http://example.org')

print(f"Done in {time.time() - start_time} seconds")

"""
    cmd>> python synchronous_url_fetching.py
Done in 0.736382246017456 seconds
"""