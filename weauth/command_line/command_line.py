#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2025/1/5 14:20
# ide： PyCharm
# file: command_line.py
from weauth.exceptions.exceptions import *
from weauth.database import DB
from weauth.mc_server import MCServerConnection
from weauth.constants.core_constant import CDKEY_LENGTH_ONE_PIECE
from weauth.cdkey import CDKey
import yaml


class CommandLine:
    def __init__(self):
        ...

    @staticmethod
    def command_node(
            command: str, open_id: str, responses: list, game_sever: MCServerConnection
    ) -> (int, str):
        raw_command = command
        if raw_command[0] == "#":  # 白名单添加入口
            welcome = responses[0]
            return CommandLine.add_new_player_entry(
                raw_id=raw_command[1:],
                open_id=open_id,
                welcome=welcome,
                game_sever=game_sever,
            )
        elif raw_command[0] == "@":  # 管理员发送指令入口
            return CommandLine.admin_command(
                raw_command=command[1:], open_id=open_id, game_sever=game_sever
            )
        elif raw_command[0] == "$":  # CDKey兑换入口
            cdkey = raw_command[1:]
            if len(cdkey) != CDKEY_LENGTH_ONE_PIECE * 4 + 3:
                return 0, "CDKey无效"
            player_id = DB.get_player_id(openid=open_id)
            if player_id is None:
                return 0, "您的微信号还未绑定游戏ID"
            msg = CDKey.cdkey_cli(
                cdkey=cdkey, player_id=player_id, game_server=game_sever
            )
            return 0, msg
        elif raw_command[0] == "!":  # 超级管理员入口
            player_id = DB.get_player_id(openid=open_id)
            if CommandLine.search_super_op(open_id=open_id):
                from weauth.command_line import AdminCLI

                return AdminCLI.admin_cli(command=command[1:], game_server=game_sever)
            else:
                return -1, "0"

        else:
            return -1, "0"

        # match raw_command[0]:
        #     case '#':
        #         welcome = responses[0]
        #         return CommandLine.add_new_player_entry(raw_id=raw_command[1:], open_id=open_id, mcsm=mcsm,welcome=welcome)
        #     case '@':
        #         return CommandLine.admin_command(raw_command=command[1:], open_id=open_id, mcsm=mcsm)
        #     case '$':
        #         ...
        #     case _:
        #         return -1,'0
        pass

    @staticmethod
    def add_new_player_entry(
            raw_id: str, open_id: str, welcome: str, game_sever: MCServerConnection
    ) -> (int, str):

        if (
                raw_id == "@a" or raw_id == "@p" or raw_id == "@e" or raw_id == "@s"
        ):  # 不允许特殊字符当作ID
            flag = 0  # 0则向服务器返回信息，否则不返回
            message = "ID不合法"
            return flag, message
        else:
            try:
                flag, message = CommandLine.add_player(
                    id=raw_id, open_id=open_id, welcome=welcome, game_sever=game_sever
                )
                return flag, message
            except Banned:
                message = "您被禁止加入服务器。"
                print("\033[0;32;40m-用户被禁止加入服务器\033[0m")
                return 0, message
            except AlreadyIn:
                message = "该角色已加入服务器。"
                print("\033[0;32;40m-角色重复加入服务器\033[0m")
                return 0, message
            except OpenidAlreadyIn:
                message = "您的微信号已绑定角色。"
                print("\033[0;32;40m-用户OpenID重复绑定\033[0m")
                return 0, message
            except ServerConnectionFailed:
                message = "游戏服务器连接失败, 请联系服务器管理员。"
                print("-游戏服务器连接失败")
                return 0, message
            except PlayerIdNotExist:
                message = "您输入的ID不存在，请检查后重新输入!"
                print("-服务器反馈无法找到玩家ID")
                return 0, message

        # match raw_id:
        #     case '@a' | '@p' | '@e' | '@s':  # 不允许特殊字符当作ID
        #         flag = 0  # 0则向服务器返回信息，否则不返回
        #         message = 'ID不合法'
        #         return flag, message
        #     case _:
        #         try:
        #             flag,message = CommandLine.add_player(id=raw_id,open_id=open_id, mcsm=mcsm, welcome=welcome)
        #             return flag,message
        #         except Banned:
        #             message = '您被禁止加入服务器。'
        #             print('\033[0;32;40m-用户被禁止加入服务器\033[0m')
        #             return 0, message
        #         except AlreadyIn:
        #             message = '该角色已加入服务器。'
        #             print('\033[0;32;40m-角色重复加入服务器\033[0m')
        #             return 0, message
        #         except OpenidAlreadyIn:
        #             message = '您的微信号已绑定角色。'
        #             print('\033[0;32;40m-用户OpenID重复绑定\033[0m')
        #             return 0, message
        #         except ServerConnectionFailed:
        #             message = '游戏服务器连接失败, 请联系服务器管理员。'
        #             print('-游戏服务器连接失败')
        #             return 0, message

    @staticmethod
    def add_player(
            id: str, open_id: str, welcome: str, game_sever: MCServerConnection
    ) -> (int, str):
        return_code, msg = DB.add(player_id=id, openid=open_id, game_server=game_sever)
        print("\033[0;32;40m-添加新玩家完成!\033[0m")
        message = "您的ID " + id + " 已添加至服务器白名单。\n" + welcome
        return 0, message

    @staticmethod
    def admin_command(
            raw_command: str, open_id: str, game_sever: MCServerConnection
    ) -> (int, str):
        if CommandLine.search_op(open_id=open_id):
            print("\033[0;32;40m-管理员通过公众号发出指令!\033[0m")
            return_code, msg = DB.push_to_server_command(
                command=raw_command, game_server=game_sever
            )

            return 0, msg
        else:
            return -1, "您不是管理员"

    @staticmethod
    def search_op(open_id: str) -> bool:
        player_id = DB.get_player_id(openid=open_id)
        if player_id is None:
            return False
        try:
            with open("ops.yaml", "r", encoding="utf-8") as f:
                result = yaml.load(f.read(), Loader=yaml.FullLoader)
            op_list = result["ops"]
        except FileNotFoundError:
            return False
        except KeyError:
            return False

        if player_id.upper() in [str.upper(i) for i in op_list]:
            return True
        return False

    @staticmethod
    def search_super_op(open_id: str) -> bool:
        player_id = DB.get_player_id(openid=open_id)
        if player_id is None:
            return False
        try:
            with open("ops.yaml", "r", encoding="utf-8") as f:
                result = yaml.load(f.read(), Loader=yaml.FullLoader)
            super_op_list = result["super_ops"]
        except FileNotFoundError:
            return False
        except KeyError:
            return False

        if player_id.upper() in [str.upper(i) for i in super_op_list]:
            return True
        return False
