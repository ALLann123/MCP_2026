#!/usr/bin/python3
import time

start_time=time.time()

#synchronously reading multiple files
def read_file_sync(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
#the function expects a list of files and uses a for loop to iterate through it
def read_all_sync(filepaths):
    return [read_file_sync(filepath) for filepath in filepaths]


filepaths=['file1.txt', 'file2.txt']
data=read_all_sync(filepaths)
print(data)

#get the final time the exectuion was complete
print(f"Time Taken is: {time.time()- start_time} seconds")

"""
    cmd>> python file_read_sync.py
['"hello world" \n', '"Welcome to New York" \n']
Time Taken is: 0.0017499923706054688 seconds
"""