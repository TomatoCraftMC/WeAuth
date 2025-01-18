#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2025/1/6 19:45 
# ide： PyCharm
# file: wechat_confirm_listener.py
from flask import Flask, request
from xml.dom.minidom import parseString
from weauth.tencent_server.wx_server import WxConnection

class WeChatConfirmListener:
    def __init__(self, token: str, url: str, ssl: bool = False):
        print('-正在启动微信验证服务器')
        print('-服务器已启动,请在微信公众号后台进行操作,当前token为 {}'.format(token))
        if ssl:
            print('-URL地址为 https://您的服务器IP或域名{}'.format(url))
            print('-验证程序默认使用443端口')
        else:
            print('-URL地址为 http://您的服务器IP或域名{}'.format(url))
            print('-验证程序默认使用80端口')
        self.wx_service = Flask(__name__)
        @self.wx_service.route(url,methods=['GET'])
        def wx():
            if request.method == 'GET':
                try:
                    timestamp = request.args.get("timestamp")
                    nonce = request.args.get("nonce")
                    echo_str = str(request.args.get("echostr"))
                    signature = request.args.get("signature")
                    print ('echostr:{}'.format(echo_str))
                    return WxConnection.confirm_token(token,timestamp,nonce,echo_str,signature)
                except FileNotFoundError:
                    return -1
            return -1

