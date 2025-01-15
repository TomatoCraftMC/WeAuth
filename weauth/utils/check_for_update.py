#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2024/7/2 下午12:50 
# ide： PyCharm
# file: check_for_update.py
import requests
from weauth.constants.core_constant import *

def check_for_update(version : str) -> bool:
    """
    检查更新
    :param version: 版本号
    :return: 检查结果
    """
    x = requests.get(GITEE_VERSION_URL)
    if version == str(x.text):
        return True
    else:
        return False
