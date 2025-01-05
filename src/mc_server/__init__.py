#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2024/7/2 下午5:26 
# ide： PyCharm
# file: __init__.py.py

from abc import ABC


class MCServerConnection(ABC):
    def __init__(self):
        pass

    @staticmethod
    def test_connection(mcsm_adr, mcsm_api, uuid, remote_uuid) -> int:
        pass

    @staticmethod
    def push_command(adr, api, uuid, remote_uuid, command) -> int:
        pass





