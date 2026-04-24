#!/usr/bin/python3
import logging

logging.basicConfig(level=logging.DEBUG)

logger=logging.getLogger(__name__)

logger.info("This is from a module")

"""
    logging>python loggers.py
INFO:__main__:This is from a module

"""
