#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2025/1/7 22:57 
# ide： PyCharm
# file: rcon.py
from tcping import Ping
from rcon.source import Client
import socket
class RCON:
    def __init__(self):
        super().__init__()
        ...

    @staticmethod
    def test_connection(host_add:str, port:int, passwd:str) -> (int,str):
        return_code = 200
        ping = Ping(host_add, port, 2)
        try:
            ping.ping(2)
        except socket.gaierror:
            print('-rcon地址无法解析')
            return -200, None
        except ConnectionRefusedError:
            print('-rcon地址无法访问')
            return -200, None
        res =ping.result.raw
        retlist = list(res.split('\n'))
        loss = retlist[2].split(',')[3].split(' ')[1]  # 获取丢包率
        print(loss)
        if float(loss.strip('%')) / 100 <= 0.1:  # 0.1为自定义丢包率阈值，可修改
            return -200, None
        try:
            with Client(host_add, port, passwd=passwd) as client:
                response = client.run('list')
            return 200,None
        except socket.gaierror:
            print('-rcon地址无法解析')
            return_code = -200
        except ConnectionError:
            print('-rcon连接失败')
            return_code = -200
        except Exception:
            return_code = -200
        return return_code,None


    @staticmethod
    def push_command(host_add:str, port:int, passwd:str, command:str) -> (int,str):
        command_tuple = tuple(command.split(' '))

        try:
            with Client(host_add, port, passwd=passwd) as client:
                response = client.run(command=command)
                return 200,response
        except ConnectionError:
            print('-rcon连接失败')
            return -200,None

        # return -200,None




