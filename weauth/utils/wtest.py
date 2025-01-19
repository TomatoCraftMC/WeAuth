#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/19 21:48 
# ide： PyCharm
# file: wtest.py
import yaml
import sys
from weauth.tencent_server.wx_server import WxConnection
from weauth.listener import WechatTestListener as Listener
from gevent import pywsgi
from gevent import ssl


def wtest() -> None:
    print('-正在测试微信服务器连接')
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        print('-已读取配置文件')
    except FileNotFoundError:
        print('-未找到配置文件config.yaml!')
        sys.exit(0)

    config = result
    url = config['url']
    # 测试微信服务器连接
    print('-正在检验AppID与AppSecret是否正确')
    if test_wechat_server(app_id=config['appID'], app_secret=config['AppSecret']) == -1:
        sys.exit(0)

    print("-正在启动监听......\n")
    listener = Listener(wx_user_name=config['WxUserName'], url=config['url'])

    if config['ssl'] == 1:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        try:
            ssl_context.load_cert_chain(certfile=config['ssl_cer'], keyfile=config['ssl_key'])
        except FileNotFoundError:
            print('-未找到ssl证书文件！')
            sys.exit(0)
        server = pywsgi.WSGIServer(('0.0.0.0', 443), listener.wx_service,
                                   ssl_context=ssl_context)
        print(f"-开始在 https://0.0.0.0{url} 进行监听")
        print('-您可以向公众号发送消息进行测试')
        server.serve_forever()
    else:
        # 核心监听程序运行
        server = pywsgi.WSGIServer(('0.0.0.0', 80), listener.wx_service)
        print(f"-开始在 http://0.0.0.0{url} 进行监听")
        print('-您可以向公众号发送消息进行测试')
        server.serve_forever()


def test_wechat_server(app_id, app_secret):
    code1, code2 = WxConnection.get_access_token(app_id, app_secret)
    if code1 == -2:
        print("-连接微信服务器网络错误，无法连接!")
        # sys.exit(2)
        return -1
    elif code1 == -1:
        print("-连接微信服务器时请求错误，错误码: " + str(code2))
        # sys.exit(3)
        return -1

    elif code1 == 0:
        print("-检验通过")
        return code2


if __name__ == '__main__':
    wtest()
