#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2025/1/6 19:59 
# ide： PyCharm
# file: wechat_confirm.py
import sys

from weauth.listener import WeChatConfirmListener
from gevent import pywsgi

from gevent import ssl


def confirm(token: str, url: str, cer_path: str = None, key_path: str = None):
    if cer_path is None:
        wechat_listener = WeChatConfirmListener(token, url)
        server = pywsgi.WSGIServer(('0.0.0.0', 80), wechat_listener.wx_service)
        server.serve_forever()
    else:
        wechat_listener = WeChatConfirmListener(token, url, ssl=True)
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        try:
            ssl_context.load_cert_chain(certfile=cer_path, keyfile=key_path)
        except FileNotFoundError:
            print('-未找到ssl证书文件！')
            sys.exit(0)
        server = pywsgi.WSGIServer(('0.0.0.0', 443), wechat_listener.wx_service,
                                   ssl_context=ssl_context)
        server.serve_forever()

    # 核心监听程序运行
    # server.serve_forever()

    # wechat_listener.wx_service.run(host='0.0.0.0', port=80)
