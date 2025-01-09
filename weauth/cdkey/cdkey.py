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
import hashlib

class CDKey:
    def __init__(self, cdkey: str):
        self.cdkey = cdkey

    @staticmethod
    def create_gift(gift_arg: str, gift_num: int, gift_total: int, gift_comment='无礼物注释') -> int:
        sha1_hash = hashlib.sha1()
        gift_str = gift_arg + gift_comment + str(gift_num)
        sha1_hash.update(gift_str.encode('utf-8'))
        gift_hash = sha1_hash.hexdigest()[-7:]  # 用来区别礼物的唯一标识

        context = {gift_hash: {'gift_arg': gift_arg,  # 礼物 如 minecraft:command_block  可以带NBT标签
                               'gift_num': gift_num,  # 礼物数   单次给予的礼物的数量
                               'gift_total': gift_total,  # 赠礼次数   这个礼物一共可以兑换多少次
                               'valid': True,  # 是否有效   默认为True  若停用礼物,改成False
                               'gift_comment': gift_comment  # 注释
                               }}
        try:
            with open('gift_list.yaml', 'r', encoding='utf-8') as f:
                result = yaml.load(f.read(), Loader=yaml.FullLoader)
                try:
                    result[gift_hash]['gift_total'] += gift_total
                    print('-已存在相同礼物,将增加其总数量')
                except KeyError:
                    result.update(context)
            with open('gift_list.yaml', 'w+') as f:
                yaml.dump(data=result, stream=f, allow_unicode=True, sort_keys=False)
        except FileNotFoundError:
            with open('gift_list.yaml', 'w+') as f:
                yaml.dump(data=context, stream=f, allow_unicode=True, sort_keys=False)

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


if __name__ == '__main__':
    text = r'minecraft:grass_blck'
    CDKey.create_gift(gift_arg=text, gift_num=6, gift_total=1, gift_comment='草方块')
