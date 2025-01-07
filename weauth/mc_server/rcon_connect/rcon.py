#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/7 22:57 
# ide： PyCharm
# file: rcon.py
from rcon.source import Client
class RCON:
    def __init__(self):
        super().__init__()
        ...

    @staticmethod
    def test_connection(host_add:str, port:int, passwd:str) -> (int,str):
        response = '-1'
        try:
            with Client(host_add, port, passwd=passwd) as client:
                response = client.run('some_command', 'with', 'some', 'arguments')
        except ConnectionError:
            response = -200
        return response,None


    @staticmethod
    def push_command(adr, api, uuid, remote_uuid, command) -> int:
        pass



