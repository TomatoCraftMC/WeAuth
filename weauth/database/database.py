#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2024/7/2 下午5:26
# ide： PyCharm
# file: database.py
import sqlite3
from weauth.exceptions.exceptions import *
import os
from weauth.mc_server.mcsm_connect import MCSM
from weauth.mc_server import MCServerConnection
import yaml
from typing import Optional

class DB:
    def __init__(self):
        print('-数据库初始化')

    @staticmethod
    def add(player_id: str, openid: str,game_server:MCServerConnection)->(int,str):
        
        conn = sqlite3.connect('./WeAuth.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM players WHERE OPENID=?", (openid,))
        user: list
        for item in cur:
            user = item
            print("角色ID:{}\tOpenID:{}".format(str(player_id),str(openid)))
            if user[0] == player_id and user[3] == 1:  # 已有相同ID且已注册
                cur.close()
                conn.close()
                raise AlreadyIn('已添加相同ID')
            if user[1] == openid:
                if user[2] == 1:
                    cur.close()
                    conn.close()
                    raise Banned('被封禁')
                else:
                    if user[3] == 0:  # 注册取关后重新注册
                        return_code,msg = DB.push_to_server_whitelist(player_id=player_id, game_server=game_server)
                        DB.responses_check_whitelist(return_code,msg)
                        cur.execute("UPDATE players SET ISSUB=? WHERE OPENID=?",(1,openid))
                        conn.commit()
                        cur.close()
                        conn.close()
                        return 0, msg
                    else:
                        cur.close()
                        conn.close()
                        raise OpenidAlreadyIn('已添加相同OpenID')
        try:
            return_code, msg = DB.push_to_server_whitelist(player_id=player_id, game_server=game_server)
            DB.responses_check_whitelist(return_code,msg)
            cur.execute("INSERT INTO players values(?,?,?,?,?)", (player_id, openid, 0, 1, 0))
            conn.commit()  # 全新注册
            cur.close()
            conn.close()
            print("全新注册")
            return 0, msg

        except sqlite3.IntegrityError:
            cur.close()
            conn.close()
            raise AlreadyIn('已添加')

    @staticmethod
    def remove_openid(openid: str) -> None:
        conn = sqlite3.connect('./WeAuth.db')
        cur = conn.cursor()
        cur.execute("UPDATE players SET ISSUB=? WHERE OPENID=?",(0,openid))
        # n=cur.execute("DELETE FROM players WHERE OPENID=?",(openid,))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def update_item_by_player_id(player_id: str, ban: str, sub: str) -> None:
        conn = sqlite3.connect('./WeAuth.db')
        cur = conn.cursor()
        cur.execute("UPDATE players SET ISBAN=?, ISSUB=? WHERE ID=?", (int(ban), int(sub), player_id))
        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def remove_player_id(player_id: str) -> None:
        player_id = DB.search_player_id(player_id=player_id)
        if player_id is None:
            raise PlayerIdNotExist('玩家ID不存在')
        conn = sqlite3.connect('./WeAuth.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM players WHERE ID=?", (player_id,))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def ban_player_id(player_id: str, mode=1) -> None:
        player_id = DB.search_player_id(player_id=player_id)
        if player_id is None:
            raise PlayerIdNotExist('玩家ID不存在')
        conn = sqlite3.connect('./WeAuth.db')
        cur = conn.cursor()
        if mode == 1:
            cur.execute("UPDATE players SET ISBAN=? WHERE ID=?", (1, player_id))
        else:
            cur.execute("UPDATE players SET ISBAN=? WHERE ID=?", (0, player_id))
        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def check_database() -> None:
        """
        检查数据库是否存在，不存在则新建数据库
        :return:
        """
        if os.path.exists('./WeAuth.db'):
            print('-已找到数据库')
            conn = sqlite3.connect('WeAuth.db')
            cur = conn.cursor()
            cur.close()
            conn.close()
        else:
            print('-未找到数据库，将新建数据库')
            conn = sqlite3.connect('./WeAuth.db')
            cur = conn.cursor()
            sql_text_1 = '''CREATE TABLE players
                (ID TEXT,
                    OPENID TEXT,
                    ISBAN NUMBER,
                    ISSUB NUMBER,
                    UNIQUE(ID),
                    PRIMARY KEY(ID));'''
            cur.execute(sql_text_1)
            print('-新的数据库已建立在: ./WeAuth.db')
            cur.close()
            conn.close()
        
    @staticmethod
    def push_to_server_whitelist(player_id: str, game_server:MCServerConnection, mode=1)->(int,str):  # mode=1加模式，否则为删模式

        if mode == 1:
            command = 'whitelist add ' + player_id
        else:
            command = 'whitelist remove ' + player_id
        return game_server.push_command(command=command)

    @staticmethod
    def push_to_server_ban(player_id: str, game_server: MCServerConnection, mode=1) -> (
    int, str):  # mode=1为ban模式，否则为取消ban模式
        if mode == 1:
            command = 'ban ' + player_id
        else:
            command = 'ban remove ' + player_id
        return game_server.push_command(command=command)

    @staticmethod
    def push_to_server_command(command:str,game_server:MCServerConnection)->(int,str):  # 用于推送指令
        return game_server.push_command(command=command)

    @staticmethod
    def responses_check_whitelist(return_code,msg):
        if return_code != 200:
            raise ServerConnectionFailed('游戏服务器连接失败')
        elif msg == 'That player does not exist\n':
            raise PlayerIdNotExist('玩家ID不存在')
        pass

    @staticmethod
    def get_player_id(openid: str) -> Optional[str]:
        conn = sqlite3.connect('./WeAuth.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM players WHERE OPENID=?", (openid,))
        for item in cur:
            if item[1] == openid:
                player_id = item[0]
                cur.close()
                conn.close()
                return player_id
        cur.close()
        conn.close()
        return None

    @staticmethod
    def search_player_id(player_id: str) -> Optional[str]:
        conn = sqlite3.connect('./WeAuth.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM players WHERE ID=?", (player_id,))
        for item in cur:
            if item[0] == player_id:
                cur.close()
                conn.close()
                return item[0]
        cur.close()
        conn.close()
        return None

    @staticmethod
    def get_all_player_ids() -> list:
        player_ids = []
        conn = sqlite3.connect('./WeAuth.db')
        cur = conn.cursor()
        cur.execute("SELECT ID FROM players")
        for row in cur:
            player_ids.append(row[0])
        cur.close()
        conn.close()
        return player_ids

    @staticmethod
    def get_item(player_id: str) -> Optional[list]:
        player_item = []
        conn = sqlite3.connect('./WeAuth.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM players WHERE ID=?", (player_id,))
        for item in cur:
            if item[0] == player_id:
                player_item.extend(item)
                cur.close()
                conn.close()
                return player_item
        cur.close()
        conn.close()
        return None



# if __name__=='__main__':
#     createNewDb()
    

