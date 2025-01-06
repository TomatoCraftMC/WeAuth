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
                data = request.get_data()
                try:
                    xml_data = parseString(data).documentElement
                    timestamp = xml_data.getElementsByTagName("timestamp")[0].childNodes[0].data
                    nonce = xml_data.getElementsByTagName("nonce")[0].childNodes[0].data
                    echo_str = xml_data.getElementsByTagName("echostr")[0].childNodes[0].data
                    signature = xml_data.getElementsByTagName("signature")[0].childNodes[0].data
                    return WxConnection.confirm_token(token,timestamp, nonce, int(echo_str), signature)
                except Exception:
                    return -1
            return -1

