#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2025/1/8 17:14 
# ide： PyCharm
# file: mc_server_connection.py
from weauth.mc_server.mcsm_connect import MCSM
from weauth.mc_server.rcon_connect import RCON


class MCServerConnection:
    def __init__(self,*args,server_type='MCSM'):
        self.params = args
        self.server_type:str = server_type


        pass

    # @staticmethod
    def test_connection(self) -> (int,str):
        server_type = self.server_type
        # print(self.params)
        # print(type(self.params))
        if server_type.upper() == "MCSM":
            return_code = MCSM.test_connection(mcsm_adr=self.params[0],
                                               mcsm_api=self.params[1],
                                               uuid=self.params[2],
                                               remote_uuid=self.params[3])
            return return_code, None
        elif server_type.upper() == "RCON":
            return_code = RCON.test_connection(host_add=self.params[0],
                                               port=int(self.params[1]),
                                               passwd=self.params[2])
            return return_code


    def push_command(self,command:str) -> (int,str):
        server_type = self.server_type
        if server_type.upper() == "MCSM":
            return_code = MCSM.push_command(adr=self.params[0],
                                            api=self.params[1],
                                            uuid=self.params[2],
                                            remote_uuid=self.params[3],
                                            command=command)
            return return_code, None


        elif server_type.upper() == "RCON":
            return RCON.push_command(host_add=self.params[0],
                                     port=int(self.params[1]),
                                     passwd=self.params[2],
                                     command=command)