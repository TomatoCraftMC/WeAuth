#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/5 20:29
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# ide： PyCharm
# file: core_constant.py
# modified from MCDReforged https://mcdreforged.com/zh-CN
import os

__CI_BUILD_NUM = None
BUILD_TIME = None

NAME_SHORT = 'WeAuth'
NAME = 'WeAuth'
PACKAGE_NAME = 'weauth'
CLI_COMMAND = PACKAGE_NAME

# WeAuth Version Storage
VERSION_PYPI: str = '1.5.6'
VERSION: str = '1.5.6'


# URLs
GITHUB_URL = r'https://github.com/TomatoCraftMC/WeAuth'
GITEE_VERSION_URL = r'https://gitee.com/NHJ2001/WeAuth/raw/main/VERSION'
DOCUMENTATION_URL = r'https://github.com/TomatoCraftMC/WeAuth/blob/main/README.md'

# CDKey
CDKEY_LENGTH_ONE_PIECE = 4

if isinstance(__CI_BUILD_NUM, str) and __CI_BUILD_NUM.isdigit():
	VERSION += '+dev.{}'.format(__CI_BUILD_NUM)
	VERSION_PYPI += '.dev{}'.format(__CI_BUILD_NUM)
