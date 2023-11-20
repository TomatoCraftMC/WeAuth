#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/5 12:18 
# ide： PyCharm
# file: create_config_yaml.py
from weauth.constants.core_constant import VERSION_PYPI
import yaml


def create_config_yaml(config: dict, default_config:dict) -> int:

    required_keys = [
            'server_connect',
            'welcome',
            'mcsm_adr',
            'mcsm_api',
            'uuid',
            'remote-uuid',
            'rcon_host_add',
            'rcon_port',
            'rcon_password',
            'token',
            'EncodingAESKey',
            'appID',
            'AppSecret',
            'EncodingMode',
            'WxUserName',
            'url'
    ]
    for key in required_keys:
        if key not in config:
            config[key] = default_config[key]

    config_dict = {
        'version': VERSION_PYPI,
        'server_connect': config['server_connect'],
        'welcome': config['welcome'],
        'mcsm_adr': config['mcsm_adr'],
        'mcsm_api': config['mcsm_api'],
        'uuid': config['uuid'],
        'remote-uuid': config['remote-uuid'],
        'rcon_host_add': config['rcon_host_add'],
        'rcon_port': config['rcon_port'],
        'rcon_password': config['rcon_password'],
        'token': config['token'],
        'EncodingAESKey': config['EncodingAESKey'],
        'appID': config['appID'],
        'AppSecret': config['AppSecret'],
        'EncodingMode': config['EncodingMode'],
        'WxUserName': config['WxUserName'],
        'url': config['url']
    }

    # 生成 comment 字典
    comment_dict = {
        'version': '版本号，请勿修改',
        'server_connect': '游戏服务器连接方式，0 为MCSManager，1 为rcon',
        'welcome': '玩家成功加入白名单后，微信的回复消息',
        'mcsm_adr': 'MCSM的url地址',
        'mcsm_api': 'MCSM的api密钥',
        'uuid': 'MCSM实例的应用实例ID',
        'remote-uuid': 'MCSM实例的远程节点ID',
        'rcon_host_add': 'RCON 主机域名或者IP',
        'rcon_port': 'RCON 端口',
        'rcon_password': 'RCON 密码',
        'token': '微信公众号token',
        'EncodingAESKey': '微信公众号加密密钥（暂时无用）',
        'appID': '微信公众号appID',
        'AppSecret': '微信公众号AppSecret',
        'EncodingMode': '微信服务器内容加密方式： 0为明文，其他待开发',
        'WxUserName': '微信公众号原始ID',
        'url': 'WeAuth路由地址，用于监听来自微信服务器消息'
    }

    text = ''
    for key in config_dict:
        text += f"# {comment_dict[key]}\n"
        text += f"{key}: {config_dict[key]}\n\n\n"

    with open('./config.yaml', 'w+') as f:
        f.write(text)
        return 0


if __name__ == '__main__':
    create_config_yaml()


