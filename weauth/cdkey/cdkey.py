#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/9 20:36 
# ide： PyCharm
# file: cdkey.py
from weauth.constants.core_constant import CDKEY_LENGTH_ONE_PIECE
import string
import secrets
import yaml


class CDKey:
    def __init__(self, cdkey: str):
        self.cdkey = cdkey

    @staticmethod
    def create_gift(gift_name: str, gift_num_total: int, gift_comment: str) -> int:
        context = {gift_comment: {'gift_name': gift_name, 'gift_num_total': gift_num_total, 'valid': True}}

        try:
            with open('gift_list.yaml', 'r', encoding='utf-8') as f:
                result = yaml.load(f.read(), Loader=yaml.FullLoader)
                print(repr(result))
        except FileNotFoundError:
            with open('gift_list.yaml', 'w+') as f:
                yaml.dump(data=context, stream=f, allow_unicode=True)

        return 0
        pass

    @staticmethod
    def generate_cdkey_one() -> str:
        try:
            if CDKEY_LENGTH_ONE_PIECE <= 0:
                return ''

            parts = [
                ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(CDKEY_LENGTH_ONE_PIECE))
                for _ in range(4)]
            return '-'.join(parts)
        except NameError:
            raise ValueError("CDKEY_LENGTH_ONE_PIECE must be defined and should be a positive integer")


CDKey.create_gift('测试', 1, '测试')
