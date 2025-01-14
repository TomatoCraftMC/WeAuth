#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2024/7/2 下午5:26
# ide： PyCharm
# file: listener.py
from flask import Flask, request
from xml.dom.minidom import parseString
from weauth.database import DB
from weauth.exceptions.exceptions import *
from weauth.tencent_server.wx_server import WxConnection
from weauth.command_line import CommandLine
import sqlite3
from weauth.mc_server import MCServerConnection


class Listener:
    def __init__(self, wx_user_name, responses: dict,url:str,game_server:MCServerConnection):
        __responses = [responses['welcome']]
        self.xml_data = []
        self.WxUserName = wx_user_name
        self.wx_service = Flask(__name__)
        @self.wx_service.route(url,methods=['POST'])
        def wx():
            if request.method == 'POST':
                data = request.get_data()
                type_of_message = Listener.message_type(data)  # 0 用户文本消息, 1 用户取消订阅事件, -1 无效post
                if type_of_message == -1:  # 非POST消息
                    return 'Incorrect'
                elif type_of_message == 0: # 文本消息
                    self.xml_data = parseString(data).documentElement
                    raw_command = self.xml_data.getElementsByTagName("Content")[0].childNodes[0].data
                    open_id = self.xml_data.getElementsByTagName("FromUserName")[0].childNodes[0].data
                    flag, message = CommandLine.command_node(command=raw_command,
                                                             open_id=open_id,responses=__responses,game_sever=game_server)
                    if flag != 0:
                        return '无回复'
                    else:
                        return WxConnection.message_encode(openid=open_id, weid=self.WxUserName, message=message)

                elif type_of_message == 1:  # 取消订阅
                    self.xml_data = parseString(data).documentElement
                    open_id = self.xml_data.getElementsByTagName("FromUserName")[0].childNodes[0].data
                    player_id = DB.get_player_id(open_id)
                    # is_openid_player, player_id = DB.search(open_id)
                    if player_id is not None:  # 取消订阅的人是玩家
                        try:
                            Listener.remove_whitelist(player_id, open_id,game_server=game_server)
                        except ServerConnectionFailed:
                            print('-游戏服务器连接失败')
                            conn = sqlite3.connect('WeAuth.db')  # 因为没有推送给游戏，所以撤回数据库修改
                            cur = conn.cursor()
                            cur.execute("UPDATE players SET ISSUB=? WHERE OPENID=?", (1, open_id))
                            conn.commit()
                            cur.close()
                            conn.close()
                    else:
                        print("-无此角色")
                        return '无返回消息'
                    return '无返回消息'
                else:
                    return '无返回消息'


    @staticmethod
    def remove_whitelist(player_id, openid,game_server:MCServerConnection):
        return_code,msg = DB.push_to_server_whitelist(player_id=player_id, game_server=game_server, mode=-1)
        if return_code != 200:
            raise ServerConnectionFailed('游戏服务器连接失败')
        else:
            DB.remove_openid(openid)
            print('\033[0;32;40m-删除动作完成\033[0m')

    @staticmethod
    def message_type(data):
        # 0 用户文本消息, 1 用户取消订阅事件, -1 无效post
        try:
            xml_data = parseString(data).documentElement
            message_type = xml_data.getElementsByTagName("MsgType")[0].childNodes[0].data
        except:
            return -1
        else:
            if message_type == 'text':
                return 0
            elif message_type == 'event':
                if xml_data.getElementsByTagName("Event")[0].childNodes[0].data == 'unsubscribe':
                    return 1
                else:
                    return -1
            else:
                return -1
