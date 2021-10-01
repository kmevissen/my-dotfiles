#!/usr/bin/env python
# encoding: utf-8

from pprint import pformat, pprint
import logging


logger = logging.getLogger('bi-logger')
logger.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)

payload = {"payload": {"origin": "AMS", "destination": "BCN", "passengers": {"adults": 2, "children": 2}}}
payload2 = {"payload": {"origin": "AMS", "destination": "BCN", "time": '%(asctime)s' ,"passengers": {"adults": 2, "children": 2}}}


# 'application' code for logging statements

# this adds payload dict in the message, but doesn't use the extra at all - this would require a custom formatter
logger.debug('debug message %(payload)s', payload, extra={'payload': payload})

# this includes payload2, but not the asctime field inside the payload dict
logger.debug('debug message %(payload)s', payload2)
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')