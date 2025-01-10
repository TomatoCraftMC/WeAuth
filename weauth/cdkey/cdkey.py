#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/9 20:36 
# ide： PyCharm
# file: cdkey.py
import sys
from weauth.constants.core_constant import CDKEY_LENGTH_ONE_PIECE
import string
import secrets
import yaml
import hashlib
from weauth.mc_server import MCServerConnection
from weauth.exceptions import *

class CDKey:
    def __init__(self, cdkey: str):
        self.cdkey = cdkey

    @staticmethod
    def cdkey_cli(cdkey: str, player_id: str, game_server: MCServerConnection) -> str:
        return_code, msg = game_server.test_connection()
        if return_code != 200:
            return '无法连接到游戏服务器,请联系管理员。\n您的CDKey暂未核销。'
        try:
            gift_hash = CDKey.check_gift_hash(cdkey=cdkey)
            gift_arg, gift_num = CDKey.check_gift_arg_and_num(gift_hash=gift_hash)
        except CDKeyNotFound:
            return 'CDKey无效'
        except FileNotFoundError:
            return 'CDKey无效'
        except CDKeyNoLeft:
            return 'CDKey已无剩余礼物可供兑换'

        try:
            return_code, msg = game_server.push_command(command=f'give {player_id} {gift_arg} {gift_num}')
            if return_code != 200:
                return '礼物发送失败'
            return '礼物已发送, 若未在线则无法收到礼物'
        except Exception as e:
            return '礼物发送失败'

    @staticmethod
    def check_gift_hash(cdkey: str) -> str:
        with open('cdkey.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        for key in result.keys():
            if cdkey in result[key]:
                result[key].remove(cdkey)
                with open('cdkey.yaml', 'w+') as f:
                    yaml.dump(data=result, stream=f, allow_unicode=True, sort_keys=False)
                return key
        raise CDKeyNotFound('未找到该CDKey')

    @staticmethod
    def check_gift_arg_and_num(gift_hash: str) -> (str, int):
        with open('gift_list.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        try:
            if result[gift_hash]['gift_total'] <= 0:
                raise CDKeyNoLeft('CDKey已无剩余礼物可供兑换')

            gift_arg = result[gift_hash]['gift_arg']
            gift_num = result[gift_hash]['gift_num']
            result[gift_hash]['gift_total'] -= 1
            with open('gift_list.yaml', 'w+') as f:
                yaml.dump(data=result, stream=f, allow_unicode=True, sort_keys=False)
            return gift_arg, int(gift_num)
        except KeyError:
            raise CDKeyNotFound('hash无对应礼物')
        except FileNotFoundError:
            raise CDKeyNotFound('无gift_list_yaml文件')









    @staticmethod
    def create_gift_entrypoint() -> None:
        gift_comment: str = input('-请输入礼物注释,并按回车确认。例如: 火把/钻石/给小张的礼物\n> ')
        gift_num: int = int(input('-请输入单次兑换所给予的数量,并按回车确认。例如: 6\n> '))
        gift_arg: str = input('-请输入礼物,可以带有NBT标签。例如：\n'
                              r'minecraft:torch 或minecraft:netherite_pickaxe{CanDestroy:[&#34;minecraft:stone&#34;]}'
                              '\n> ')
        gift_total: int = int(input('-请输入生成CDKey数量\n> '))
        try:
            gift_hash = CDKey.create_gift(gift_arg=gift_arg,
                                          gift_num=gift_num,
                                          gift_total=gift_total,
                                          gift_comment=gift_comment)
            CDKey.generate_cdkey(gift_hash=gift_hash,
                                 gift_total=gift_total)
            print('-CDKey生成成功! 保存在./cdkey.yaml当中')
            sys.exit(0)
        except Exception:
            print('-生成失败')
            sys.exit(0)


    @staticmethod
    def create_gift(gift_arg: str, gift_num: int, gift_total: int, gift_comment='无礼物注释') -> str:
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
                    print(f'-已存在相同礼物 {gift_hash},将增加其总数量')
                except KeyError:
                    result.update(context)
                    print(f'-已生成新的礼物 {gift_hash}')
            with open('gift_list.yaml', 'w+') as f:
                yaml.dump(data=result, stream=f, allow_unicode=True, sort_keys=False)
            return gift_hash
        except FileNotFoundError:
            with open('gift_list.yaml', 'w+') as f:
                yaml.dump(data=context, stream=f, allow_unicode=True, sort_keys=False)
            print(f'-已生成新的礼物 {gift_hash},礼物列表保存在./gift_list.yaml中')
            return gift_hash

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

    @staticmethod
    def generate_cdkey(gift_hash: str, gift_total: int) -> None:
        cdkey_list: list[str] = []
        for i in range(gift_total):
            cdkey_list.append(CDKey.generate_cdkey_one())
        new_dict = {gift_hash: cdkey_list}
        try:
            with open('cdkey.yaml', 'r', encoding='utf-8') as f:
                result = yaml.load(f.read(), Loader=yaml.FullLoader)
            try:
                result[gift_hash].extend(cdkey_list)
                with open('cdkey.yaml', 'w+') as f:
                    yaml.dump(data=result, stream=f, allow_unicode=True, sort_keys=False)
            except KeyError:
                result.update(new_dict)
                with open('cdkey.yaml', 'w+') as f:
                    yaml.dump(data=result, stream=f, allow_unicode=True, sort_keys=False)

        except FileNotFoundError:
            with open('cdkey.yaml', 'w+') as f:
                yaml.dump(data=new_dict, stream=f, allow_unicode=True, sort_keys=False)


if __name__ == '__main__':
    gift = r'IDf7-HzyM-FgVT-4jj5'
    CDKey.check_gift_hash(gift)
