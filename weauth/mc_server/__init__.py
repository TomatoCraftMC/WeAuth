#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2024/7/2 下午5:26 
# ide： PyCharm
# file: __init__.py.py
from abc import ABC
from weauth.mc_server.mcsm_connect import MCSM
from weauth.mc_server.rcon_connect import RCON


class MCServerConnection:
    def __init__(self):
        pass

    @staticmethod
    def test_connection(parameter:list,server_type:str) -> (int,str):
        if server_type.upper() == "MCSM":
            return_code = MCSM.test_connection(mcsm_adr=parameter[0],
                                               mcsm_api=parameter[1],
                                               uuid=parameter[2],
                                               remote_uuid=parameter[3])
            return return_code, None
        elif server_type.upper() == "RCON":
            return_code = RCON.test_connection(host_add=parameter[0],
                                               port=int(parameter[1]),
                                               passwd=parameter[2])
            return return_code


    @staticmethod
    def push_command(adr, api, uuid, remote_uuid, command) -> int:
        pass





