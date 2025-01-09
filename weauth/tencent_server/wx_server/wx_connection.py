#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/6 19:23 
# ide： PyCharm
# file: wx_connection.py
import hashlib
import time
import sys
import requests
import json
import xml.etree.ElementTree as ET
from weauth.tencent_server import TencentServerConnection


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
        except Exception:
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
        message_slash = message.replace('\\n', '\n')
        Content.text = message_slash
        print(f'Content is\n {message_slash}')
        print(repr(message_slash))

        tree = ET.ElementTree(root)
        xml_data = ET.tostring(root, encoding='utf-8')

        return xml_data

    @staticmethod
    def confirm_token(token:str,timestamp:str,nonce:str,echo_str:str,signature:str) ->str:
        try:
            temp_list = [token, timestamp, nonce]
            temp_list.sort()
            temp = ''.join(temp_list)
            sha1 = hashlib.sha1(temp.encode('utf-8'))
            hashcode = sha1.hexdigest()

            if hashcode == signature:
                print('校验成功!')
                print('echostr={}'.format(echo_str))
                return echo_str
            else:
                print('微信Token校验失败')
                return '404'
        except Exception as e:
            print('微信Token解析失败', e)
            return '404'


