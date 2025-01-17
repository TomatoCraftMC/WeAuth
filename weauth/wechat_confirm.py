#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2025/1/6 19:59 
# ide： PyCharm
# file: wechat_confirm.py
from weauth.listener import WeChatConfirmListener
from gevent import pywsgi

from gevent import ssl

def confirm(token:str,url:str):
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.load_cert_chain(certfile='/root/WeAuth/public.crt',
                                keyfile='/root/WeAuth/private.key')

    wechat_listener = WeChatConfirmListener(token,url)

    server = pywsgi.WSGIServer(('0.0.0.0', 443), wechat_listener.wx_service,
                               ssl_context=ssl_context)


    # 核心监听程序运行
    server.serve_forever()

    # wechat_listener.wx_service.run(host='0.0.0.0', port=80)
