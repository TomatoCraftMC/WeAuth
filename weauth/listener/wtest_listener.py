#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/19 21:57
# ide： PyCharm
# file: wtest_listener.py
from flask import Flask, request
from xml.dom.minidom import parseString
from weauth.tencent_server.wx_server import WxConnection


class WechatTestListener:
    def __init__(self, wx_user_name: str, url: str):
        self.wx_service = Flask(__name__)
        self.url = url
        self.wx_user_name = wx_user_name
        self._register_routes()

    def _register_routes(self):
        @self.wx_service.route(self.url, methods=["POST"])
        def wx():
            data = request.data
            print("-接收到来自微信消息")
            print(data)
            xml_data = parseString(data).documentElement
            raw_message = xml_data.getElementsByTagName("Content")[0].childNodes[0].data
            open_id = (
                xml_data.getElementsByTagName("FromUserName")[0].childNodes[0].data
            )
            print(f"-信息：\n{raw_message}")
            print(f"-发送者OpenID: {open_id}")

            return WxConnection.message_encode(
                openid=open_id, weid=self.wx_user_name, message="服务器连接正常！"
            )
