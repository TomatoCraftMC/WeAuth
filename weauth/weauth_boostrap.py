# WeAuth.py
# created by NearlyHeadlessJack 2024-01-03
# https://github.com/nearlyheadlessjack/weauth
# 程序总入口
from email.policy import default
import sys
from http.client import responses
from gevent import pywsgi

# import click
from weauth.listener import Listener
from weauth.database.database import DB
import yaml
from weauth.utils.check_for_update import check_for_update
from weauth.utils.create_config_yaml import create_config_yaml
from weauth.mc_server.mcsm_connect import MCSM
from weauth.tencent_server.wx_server import WxConnection
from weauth.exceptions.exceptions import *
from weauth.constants.core_constant import *
from weauth.constants import exit_code
from weauth.mc_server import MCServerConnection

# @click.command()
# @click.option(
#     '-p',
#     '--port',
#     default='80',
#     help='本地监听端口号'
# )
def main(args) -> None:
    """应用程序入口"""
    print(" ")
    print("\033[32m      __        __      _         _   _     \033[0m")
    print("\033[32m      \ \      / /__   / \  _   _| |_| |__  \033[0m")
    print("\033[32m       \ \ /\ / / _ \ / _ \| | | | __| '_ \ \033[0m")
    print("\033[32m        \ V  V /  __// ___ \ |_| | |_| | | |\033[0m")
    print("\033[32m         \_/\_/ \___/_/   \_\__,_|\__|_| |_|\033[0m")
    print("                 Version: {}".format(VERSION))
    print("\033[34mWeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.\033[0m")
    print("Project Homepage: {}\n".format(GITHUB_URL))
    port = args.port
    # 检查更新
    print("-正在检查更新...")
    if check_for_update(VERSION) == 1:
        print("-当前为最新版本")
    else:
        print("-已有新版本,您可以前往 {} 进行更新。".format(GITHUB_URL))
    # 检查数据库
    DB.check_database()
    default_config = {
        'server_connect': 0,
        'welcome': '欢迎加入我的服务器!\\n如果仍然无法加入服务器, 请联系管理员。\\n祝您游戏愉快!',
        'mcsm_adr': 'http://127.0.0.1:23333/',
        'mcsm_api': '12345',
        'uuid': '12345',
        'remote-uuid': '12345',
        'rcon_host_add': '127.0.0.1',
        'rcon_port': '25565',
        'rcon_password': 'PASSWORD',
        'token': '12345',
        'EncodingAESKey': '12345',
        'appID': '12345',
        'AppSecret': '12345',
        'EncodingMode': '12345',
        'WxUserName': '12345',
        'url': '/wx'
    }

    if not args.test_mode:
        # 读取配置文件
        try:
            config = read_config()
            check_config_version(config,default_config=default_config)
        except ConfigFileNotFound:
            create_config_yaml(config=default_config,default_config=default_config)
            print('-首次运行, 请先在config.yaml中进行配置!')
            sys.exit(0)
    else:
        config = default_config

    # 检查是否有op列表
    check_op_list()
    server_type = 'MCSM'

    if config['server_connect'] == 0:
        server_type = 'MCSM'
        game_server = MCServerConnection(config['mcsm_adr'],
                                          config['mcsm_api'],
                                          config['uuid'],
                                          config['remote-uuid'],server_type=server_type)
    elif config['server_connect'] == 1:
        server_type = 'RCON'
        game_server = MCServerConnection(config['rcon_host_add'],
                                          config['rcon_port'],
                                          config['rcon_password'],
                                          server_type=server_type)

    else:
        print('-错误的服务器类型')
        sys.exit(1)


    # 测试游戏端连接
    return_code,message = game_server.test_connection()
    if  return_code == 200:
        print('-成功连接到游戏服务器!')
    else:
        print('-无法连接到游戏服务器, 请检查config.yaml配置以及网络状况!')
        if not args.test_mode:
            sys.exit(0)


    url = config['url']
    if args.url != '/wx':
        url = args.url

    # 测试微信服务器连接
    access_token = test_wechat_server(app_id=config['appID'], app_secret=config['AppSecret'])

    # 公众号回复语句
    responses = {
        'welcome': config['welcome']  # 玩家注册白名单成功
    }

    # 创建Flask实例
    print("-正在启动监听......\n")
    listener = Listener(wx_user_name=config['WxUserName'],responses=responses,url=url,game_server=game_server)

    # 核心监听程序运行
    server = pywsgi.WSGIServer(('0.0.0.0', int(port)), listener.wx_service)
    print(f"-开始在 http://0.0.0.0:{port}{url} 进行监听")
    server.serve_forever()

    # 核心监听程序运行(flask自带web服务器)
    # listener.wx_service.run(host='0.0.0.0', port=port)


# 读取配置文件
def read_config() -> dict:
    """
    读取配置文件
    :return: 配置信息，以字典形式
    """
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        return result
    except FileNotFoundError:
        raise ConfigFileNotFound('未找到配置文件')

def check_op_list() -> None:
    """
     检查是否有op表，没有则新建
    """
    try:
        with open('ops.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
    except FileNotFoundError:
        with open('./ops.yaml', 'w+') as f:
            context = {
                'ops': ['test_id1','test_id2']
            }
            yaml.dump(data=context, stream=f, allow_unicode=True)

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
        print("-已更新Access Token")
        return code2

def check_config_version(config:dict,default_config:dict):
    print("-正在更新配置文件")
    create_config_yaml(config=config,default_config=default_config)


# if __name__ == '__main__':
#     main()


    