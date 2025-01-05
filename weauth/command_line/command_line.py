#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/5 14:20 
# ide： PyCharm
# file: command_line.py
from weauth.exceptions.exceptions import *
from weauth.database import DB
class CommandLine:
    def __init__(self):
        ...

    @staticmethod
    def command_node(command: str, open_id: str,mcsm: list, responses: list) -> (int, str):
        raw_command = command
        match raw_command[0]:
            case '#':
                welcome = responses[0]
                return CommandLine.add_new_player_entry(raw_id=raw_command[1:], open_id=open_id, mcsm=mcsm,welcome=welcome)
            case '@':
                return CommandLine.admin_command(raw_command=command[1:], open_id=open_id, mcsm=mcsm)
            case '$':
                ...
            case _:
                return -1,'0'



        pass

    @staticmethod
    def add_new_player_entry(raw_id: str, open_id: str, mcsm:list, welcome: str) -> (int, str):

        match raw_id:
            case '@a' | '@p' | '@e' | '@s':  # 不允许特殊字符当作ID
                flag = 0  # 0则向服务器返回信息，否则不返回
                message = 'ID不合法'
                return flag, message
            case _:
                try:
                    flag,message = CommandLine.add_player(id=raw_id,open_id=open_id, mcsm=mcsm, welcome=welcome)
                    return flag,message
                except Banned:
                    message = '您被禁止加入服务器。'
                    print('\033[0;32;40m-用户被禁止加入服务器\033[0m')
                    return 0, message
                except AlreadyIn:
                    message = '该角色已加入服务器。'
                    print('\033[0;32;40m-角色重复加入服务器\033[0m')
                    return 0, message
                except OpenidAlreadyIn:
                    message = '您的微信号已绑定角色。'
                    print('\033[0;32;40m-用户OpenID重复绑定\033[0m')
                    return 0, message
                except ServerConnectionFailed:
                    message = '游戏服务器连接失败, 请联系服务器管理员。'
                    print('-游戏服务器连接失败')
                    return 0, message


    @staticmethod
    def add_player(id: str,open_id: str, mcsm: list, welcome: str) -> (int, str):
        DB.add(player_id=id, openid=open_id, mcsm=mcsm)
        print('\033[0;32;40m-添加新玩家完成!\033[0m')
        message = ('您的ID '+ id + ' 已添加至服务器白名单。\n' + welcome)
        return 0, message

    @staticmethod
    def admin_command(raw_command: str, open_id: str, mcsm:list):
        if DB.search_admin(openid=open_id) == 1:
            print('\033[0;32;40m-管理员通过公众号发出指令!\033[0m')
            DB.push_to_server_command(mcsm=mcsm,command=raw_command)
            message = '指令成功发送!'
            return 0,message
        else:
            return -1,'您不是管理员'