#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2024/7/2 下午5:26 
# ide： PyCharm
# file: __init__.py.py

from abc import ABC


class TencentServerConnection(ABC):
    def __init__(self):
        pass

    @staticmethod
    def get_access_token(appid, apps):
        pass

    @staticmethod
    def message_encode(openid, weid, message):
        pass

