#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2024/7/2 下午5:26
# ide： PyCharm
# file: exceptions.py
class Banned(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class AlreadyIn(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class OpenidAlreadyIn(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ServerConnectionFailed(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ConfigFileNotFound(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class PlayerIdNotExist(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class CDKeyNotFound(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class CDKeyNoLeft(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
