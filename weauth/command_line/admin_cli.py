#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2025/1/11 08:35 
# ide： PyCharm
# file: admin_cli.py
import sys
import os
from weauth.database import DB
from weauth.constants.core_constant import VERSION, GITHUB_URL, BUILD_TIME
from weauth.utils.add_op import add_op, add_super_op
from weauth.cdkey import CDKey
from weauth.exceptions import *
from typing import Optional
from weauth.mc_server import MCServerConnection
import prettytable

class AdminCLI:
    def __init__(self):
        pass

    @staticmethod
    def admin_cli_entry(command: str, player_id: str) -> (int, str):

        pass

    @staticmethod
    def admin_cli(command: str, game_server: MCServerConnection) -> (int, str):
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
            msg = AdminCLI.remove_by_player_id(game_server=game_server,
                                               play_id_from_wechat=command_list[1])
            if msg is None:
                return 0, '删除失败，请联系管理员'
            return 0, msg
        elif command_list[0] == 'l':
            return 0, AdminCLI.list_all_player_id()
        elif command_list[0] == 's':
            if len(command_list) != 2:
                return 0, '参数错误，正确用法:\n!s [player_id]'
            msg = AdminCLI.search_db(player_id=command_list[1], from_admin_cli=True)
            return 0, msg
        elif command_list[0] == 'u':
            if len(command_list) != 4:
                return 0, '参数错误，正确用法:\n!u [player_id] [is_ban] [is_sub]'
            player_id = DB.search_player_id(player_id=command_list[1])
            if player_id is None:
                return 0, '数据库无该玩家ID'
            if command_list[2] != '0' and command_list[2] != '1':
                return 0, '[is_ban]只能输入1或0，请重新输入'
            if command_list[3] != '0' and command_list[3] != '1':
                return 0, '[is_sub]只能输入1或0，请重新输入'
            DB.update_item_by_player_id(player_id=player_id,
                                        ban=command_list[2],
                                        sub=command_list[3])
            return_code = -200
            if command_list[2] == '0':
                return_code, msg = DB.push_to_server_ban(player_id=player_id, game_server=game_server, mode=0)
            elif command_list[2] == '1':
                return_code, msg = DB.push_to_server_ban(player_id=player_id, game_server=game_server, mode=1)
            if return_code != 200:
                return 0, f'{player_id} 的封禁与订阅信息已更新，但推送游戏服务器失败。'
            return 0, f'{player_id} 的封禁与订阅信息已更新！\n您可以使用!s {player_id}进行查看。'
        elif command_list[0] == 'b':
            if len(command_list) != 2:
                return 0, '参数错误，正确用法:\n!b [player_id]'
            msg = AdminCLI.ban_db(player_id=command_list[1], game_server=game_server)
            return 0, msg
        elif command_list[0] == 'ub':
            if len(command_list) != 2:
                return 0, '参数错误，正确用法:\n!ub [player_id]'
            msg = AdminCLI.unban_db(player_id=command_list[1], game_server=game_server)
            return 0, msg
        else:
            text = (f'错误命令！\n'
                    f'WeAuth v{VERSION}\n【使用指南】\n'
                    f'!v # 查看版本号\n\n'
                    f'!op [ID] # 添加普通管理员\n\n'
                    f'!sop [ID] # 添加超级管理员\n\n'
                    f'!g [mineID] [mineNum] [CDKeyNum] [Comment]\n'
                    f'# 生成CDKey\n'
                    f'!l # 打印所有玩家ID\n'
                    f'!s [player_id]  # 显示该用户ID的封禁、订阅情况\n'
                    f'!d [ID]\n'
                    f'# 在数据库和游戏服务器删除ID，会自动移出白名单\n'
                    f'!b [player_id]  # 封禁该用户，同时会移出白名单\n'
                    f'!ub [player_id]  # 移出封禁\n'
                    f'!u [player_id] [is_ban] [is_sub]\n'
                    f'# 手动更新玩家封禁与订阅信息')
            return 0, text

    @staticmethod
    def remove_by_player_id(game_server: MCServerConnection = None, play_id_from_wechat=None) -> Optional[str]:
        if play_id_from_wechat is None:
            player_id = input("-请输入您要删除的玩家ID\n>")
            try:
                DB.remove_player_id(player_id)
            except PlayerIdNotExist:
                print("-玩家ID不存在")
                sys.exit(0)
            print(f"-玩家 {player_id} 成功删除")
            sys.exit(0)
        else:
            player_id = play_id_from_wechat
            try:
                DB.remove_player_id(player_id)
            except PlayerIdNotExist:
                print("-玩家ID不存在")
                return '玩家ID不存在'
            return_code, msg = DB.push_to_server_whitelist(player_id=player_id,
                                                           game_server=game_server,
                                                           mode=0)
            if return_code != 200:
                print(f"-玩家 {player_id} 在数据库成功删除，但推送至游戏服务器时出现异常")
                return f"-玩家 {player_id} 在数据库成功删除，但推送至游戏服务器时出现异常"
            print(f"-玩家 {player_id} 成功删除")
            return f"玩家 {player_id} 成功删除"

    @staticmethod
    def list_all_player_id() -> str:
        if not os.path.exists('WeAuth.db'):
            return '数据库丢失！'
        player_id_list = DB.get_all_player_ids()
        if len(player_id_list) <= 0:
            return '数据库无数据！'
        player_list = '\n'.join(player_id_list)
        title = '=====玩家ID=====\n'
        end = f'\n=====玩家ID=====\n共有{len(player_id_list)}位玩家'
        return title + player_list + end

    @staticmethod
    def search_db(player_id: str = None, from_admin_cli=False) -> Optional[str]:
        if from_admin_cli is True:
            player_item = DB.get_item(player_id=player_id)
            if player_item is None:
                print(f'-数据库中找不到 {player_id}')
                return f'-数据库中找不到 {player_id}'
            msg = (f'玩家ID: {player_item[0]}\n'
                   f'OpenID: {player_item[1]}\n'
                   f'是否封禁: {player_item[2]}\n'
                   f'正在订阅公众号: {player_item[3]}\n')
            return msg
        else:
            player_item = DB.get_item(player_id=player_id)
            if player_item is None:
                print(f'-数据库中找不到 {player_id}')
                sys.exit(0)
            print(f'-找到玩家 {player_item[0]}\n==================================')
            table = prettytable.PrettyTable()
            table.field_names = ['玩家ID', 'OpenID', '是否封禁', '正在订阅公众号']
            table.add_row(player_item[:4])
            print(table)
            sys.exit(0)

    @staticmethod
    def ban_db(player_id: str, game_server: MCServerConnection = None) -> Optional[str]:
        if game_server is not None:
            player_id_ = DB.search_player_id(player_id=player_id)
            if player_id_ is None:
                print(f'-数据库中找不到 {player_id}')
                return f'数据库中找不到 {player_id}'
            DB.ban_player_id(player_id=player_id_)
            return_code1, msg1 = DB.push_to_server_ban(player_id=player_id_, game_server=game_server)
            return_code2, msg2 = DB.push_to_server_whitelist(player_id=player_id_, game_server=game_server, mode=0)
            if return_code1 != 200 and return_code2 != 200:
                print(f'-数据库中已封禁{player_id_}，但推送游戏服务器失败')
                return f'数据库中已封禁{player_id_}，但推送游戏服务器失败'
            print(f'-已封禁{player_id_}')
            return f'已封禁{player_id_}'
        else:
            player_id_ = DB.search_player_id(player_id=player_id)
            if player_id_ is None:
                print(f'-数据库中找不到 {player_id}')
                sys.exit(0)
            DB.ban_player_id(player_id=player_id_)
            print(f'-已封禁{player_id_}，但未推送至游戏服务器')

    @staticmethod
    def unban_db(player_id: str, game_server: MCServerConnection = None) -> Optional[str]:
        if game_server is not None:
            player_id_ = DB.search_player_id(player_id=player_id)
            if player_id_ is None:
                print(f'-数据库中找不到 {player_id}')
                return f'数据库中找不到 {player_id}'
            DB.ban_player_id(player_id=player_id_, mode=0)
            return_code, msg = DB.push_to_server_ban(player_id=player_id_, game_server=game_server, mode=0)
            if return_code != 200:
                print(f'-数据库中已解除封禁{player_id_}，但推送游戏服务器失败')
                return f'数据库中已解除封禁{player_id_}，但推送游戏服务器失败'
            print(f'-已解除封禁{player_id_}')
            return f'已解除封禁{player_id_}'
        else:
            player_id_ = DB.search_player_id(player_id=player_id)
            if player_id_ is None:
                print(f'-数据库中找不到 {player_id}')
                sys.exit(0)
            DB.ban_player_id(player_id=player_id_, mode=0)
            print(f'-已解除封禁{player_id_}，但未推送至游戏服务器')


if __name__ == '__main__':
    AdminCLI.admin_cli('g d 1 2 te')
