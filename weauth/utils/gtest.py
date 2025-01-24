#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/19 21:36
# ide： PyCharm
# file: gtest.py
import sys
from weauth.mc_server import MCServerConnection

import yaml


def gtest() -> None:
    print("-正在测试游戏服务器连接")
    try:
        with open("config.yaml", "r", encoding="utf-8") as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        print("-已读取配置文件")
    except FileNotFoundError:
        print("-未找到配置文件config.yaml!")
        sys.exit(0)

    config = result

    return_code = -200
    message = "-1"

    if config["server_connect"] == 0:
        server_type = "MCSM"
        game_server = MCServerConnection(
            config["mcsm_adr"],
            config["mcsm_api"],
            config["uuid"],
            config["remote-uuid"],
            server_type=server_type,
        )
        return_code, message = game_server.test_connection()
        print("-正在连接到MCSManager......")
    elif config["server_connect"] == 1:
        server_type = "RCON"
        game_server = MCServerConnection(
            config["rcon_host_add"],
            config["rcon_port"],
            config["rcon_password"],
            server_type=server_type,
        )
        return_code, message = game_server.test_connection()
        print("-正在通过Rcon连接到Minecraft Server......")

    if return_code == 200:
        print("-成功连接到游戏服务器!")
        sys.exit(0)
    else:
        print(
            f"-连接游戏服务器失败，请重新检查\n-返回码 {return_code} \n-返回信息 {message}"
        )
        sys.exit(0)


if __name__ == "__main__":
    gtest()
