#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/5 12:18 
# ide： PyCharm
# file: create_config_yaml.py

def create_config_yaml() -> int:
    text = ('# 连接Minecraft服务端的方法，0为MCSM API，1为rcon\n'
            'server_connect: 0\n\n'
            '# 白名单加入成功时的回复语\n'
            'welcome: 欢迎加入我的服务器!如果仍然无法加入服务器, 请联系管理员。祝您游戏愉快!\n\n'
            '# MCSM面板的地址\n'
            'mcsm_adr: http://127.0.0.1:23333/\n\n'
            '# MCSM的API Key\n'
            'mcsm_api: xxxxxx\n\n'
            '# MCSM实例的应用实例 ID\n'
            'uuid: xxxxxx\n\n'
            '# MCSM实例的远程节点 ID\n'
            'remote-uuid: xxxxxx\n\n'
            '# rcon连接地址或域名\n'
            'rcon_host_add: 8.8.8.8\n\n'
            '# rcon连接端口\n'
            'rcon_port: 25565\n\n'
            '# rcon连接密码\n'
            'rcon_password: <PASSWORD>\n\n'
            '# 微信公众号TOEKN\n'
            'toekn: xxxxxx\n\n'
            '# 微信公众号EncodingAESKey(可选)\n'
            'EncodingAESKey: xxxxxxx\n\n'
            '# 微信公众号appID\n'
            'appID: xxxxxx\n\n'
            '# 微信公众号AppSecret\n'
            'AppSecret:\n\n'
            '# 微信服务器内容加密方式： 0为明文，其他待开发\n'
            'EncodingMode: 0\n\n'
            '# 微信公众号原始ID\n'
            'WxUserName: xxxxxx\n\n'
            '# WeAuth路由地址\n'
            'url: /wx\n\n')

    with open('./config.yaml','w+') as f:
        f.write(text)
        return 0




if __name__ == '__main__':
    create_config_yaml()


