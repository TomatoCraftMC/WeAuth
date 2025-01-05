#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2024/7/2 下午5:26 
# ide： PyCharm
# file: __init__.py.py

import time
import sys
import requests
import json
import xml.etree.ElementTree as ET
from tencent_server import TencentServerConnection


class WxConnection(TencentServerConnection):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_access_token(appid, apps):
        """
        获取微信公众号token
        :param appid:
        :param apps:
        :return:
        """
        body = {
            "grant_type": "client_credential",
            "appid": appid,
            "secret": apps
        }
        url = r'https://api.weixin.qq.com/cgi-bin/token?'
        try:
            response = requests.get(url, params=body)
            res = json.loads(response.text)
        except:
            return -2, -2
        else:
            try:
                return 0, res['access_token']
            except KeyError:
                return -1, res['errcode']

    @staticmethod
    def message_encode(openid, weid, message):

        root = ET.Element("xml")
        ToUserName = ET.SubElement(root, "ToUserName")
        FromUserName = ET.SubElement(root, "FromUserName")
        CreateTime = ET.SubElement(root, "CreateTime")
        MsgType = ET.SubElement(root, "MsgType")
        Content = ET.SubElement(root, "Content")

        ToUserName.text = openid
        FromUserName.text = weid
        CreateTime.text = str(int(time.time()))
        MsgType.text = "text"
        Content.text = message

        tree = ET.ElementTree(root)
        xml_data = ET.tostring(root, encoding='utf-8')

        return xml_data
