#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2024/7/4 上午1:27 
# ide： PyCharm
# file: __init__.py.py
from rcon.source import Client

with Client('127.0.0.1', 5000, passwd='mysecretpassword') as client:
    response = client.run('some_command', 'with', 'some', 'arguments')

print(response)