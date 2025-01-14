#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/11 08:35 
# ide： PyCharm
# file: admin_cli.py
import sys
from weauth.database import DB
from weauth.constants.core_constant import VERSION, GITHUB_URL, BUILD_TIME
from weauth.utils.add_op import add_op, add_super_op
from weauth.cdkey import CDKey
from weauth.exceptions import *
from typing import Optional

class AdminCLI:
    def __init__(self):
        pass

    @staticmethod
    def admin_cli_entry(command: str, player_id: str) -> (int, str):

        pass

    @staticmethod
    def admin_cli(command: str) -> (int, str):
        command_list = command.split()
        if command_list[0] == 'op':
            op_id = command_list[1]
            if add_op(op_id=op_id) == 0:
                return 0, f'已成功添加 {op_id} 为WeAuth管理员'
            else:
                return 0, '添加失败'
        elif command_list[0] == 'sop':
                op_id = command_list[1]
                if add_super_op(op_id=op_id) == 0:
                    return 0, f'已成功添加 {op_id} 为WeAuth超级管理员'
                else:
                    return 0, '添加失败'
        elif command_list[0] == 'v':
            msg = f'WeAuth version {VERSION}\nBuild time: {BUILD_TIME}z\nLICENSE: GPLv3\nProject Homepage: {GITHUB_URL}'
            return 0, msg
        elif command_list[0] == 'g':
            if len(command_list) != 5:
                return 0, '参数错误，正确用法:\n!g [mineID] [mineNum] [CDKeyNum] [Comment]'
            mine_id, mine_num, cdkey_num, comment = command_list[1], command_list[2], command_list[3], command_list[4]
            if mine_num.isdigit() and cdkey_num.isdigit():
                pass
            else:
                return 0, '参数错误，正确用法:\n!g [mineID] [mineNum] [CDKeyNum] [Comment]'

            try:
                gift_hash = CDKey.create_gift(gift_arg=mine_id,
                                              gift_num=int(mine_num),
                                              gift_total=int(cdkey_num),
                                              gift_comment=comment)
                cdkey_list = CDKey.generate_cdkey(gift_hash=gift_hash,
                                                  gift_total=int(cdkey_num), is_feedback=True)
            except Exception:
                return 0, '生成失败，请联系管理员'

            msg = "\n".join(cdkey_list)
            return 0, msg
        elif command_list[0] == 'd':
            if len(command_list) != 2:
                return 0, '参数错误，正确用法:\n!d [player_id]'
            return 0, AdminCLI.remove_by_player_id(play_id_from_wechat=command_list[1])

        else:
            text = (f'错误命令！\n'
                    f'WeAuth v{VERSION}\n【使用指南】\n'
                    f'!v # 查看版本号\n\n'
                    f'!op [ID] # 添加普通管理员\n\n'
                    f'!sop [ID] # 添加超级管理员\n\n'
                    f'!g [mineID] [mineNum] [CDKeyNum] [Comment]\n'
                    f'# 生成CDKey')
            return 0, text

    @staticmethod
    def remove_by_player_id(play_id_from_wechat=None) -> Optional[str]:
        if play_id_from_wechat is None:
            player_id = input("-请输入您要删除的玩家ID\n>")
            try:
                DB.remove_player_id(player_id)
            except PlayerIdNotExist:
                print("-玩家ID不存在")
                sys.exit(0)
            finally:
                print(f"-玩家 {player_id} 成功删除")
                sys.exit(0)
        else:
            player_id = play_id_from_wechat
            try:
                DB.remove_player_id(player_id)
            except PlayerIdNotExist:
                print("-玩家ID不存在")
                return '玩家ID不存在'
            finally:
                print(f"-玩家 {player_id} 成功删除")
                return f"玩家 {player_id} 成功删除"






if __name__ == '__main__':
    AdminCLI.admin_cli('g d 1 2 te')
