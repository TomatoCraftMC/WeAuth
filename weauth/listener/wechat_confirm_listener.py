#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/6 19:45 
# ide： PyCharm
# file: wechat_confirm_listener.py
from flask import Flask, request
from xml.dom.minidom import parseString
from weauth.tencent_server.wx_server import WxConnection


class WeChatConfirmListener:
    def __init__(self,token:str):
        print('-正在启动微信验证服务器')
        self.wx_service = Flask(__name__)
        @self.wx_service.route('/wx',methods=['GET'])
        def wx():
            if request.method == 'GET':
                try:
                    timestamp = request.args.get("timestamp")
                    nonce = request.args.get("nonce")
                    echo_str = str(request.args.get("echo_str"))
                    signature = request.args.get("signature")
                    return WxConnection.confirm_token(token,timestamp,nonce,echo_str,signature)
                except FileNotFoundError:
                    return -1
            return -1

