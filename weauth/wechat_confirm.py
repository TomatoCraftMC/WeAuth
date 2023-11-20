#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/6 19:59 
# ide： PyCharm
# file: wechat_confirm.py
from weauth.listener import WeChatConfirmListener

def confirm(token:str,url:str):
    wechat_listener = WeChatConfirmListener(token,url)
    # 核心监听程序运行
    wechat_listener.wx_service.run(host='0.0.0.0', port=80)