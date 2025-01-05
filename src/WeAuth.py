# WeAuth.py
# created by NearlyHeadlessJack 2024-01-03
# https://github.com/nearlyheadlessjack/weauth
# 程序总入口
from listener.listener import Listener
from database.database import DB
import yaml
from utils.check_for_update import check_for_update
from utils.create_config_yaml import create_config_yaml
from mc_server.mcsm_connect import MCSM
from tencent_server.wx_server import WxConnection
from exceptions.exceptions import *

VERSION: str = '1.0.0'  # 版本号
BUILD_VERSION: str = '1.0.0.2025.1.5.1'   # 内部版本号

def main() -> None:
    """应用程序入口"""
    print(" ")
    print("      __        __      _         _   _     ")
    print("      \ \      / /__   / \  _   _| |_| |__  ")
    print("       \ \ /\ / / _ \ / _ \| | | | __| '_ \ ")
    print("        \ V  V /  __// ___ \ |_| | |_| | | |")
    print("         \_/\_/ \___/_/   \_\__,_|\__|_| |_|")
    print("                                            ")
    print("                 Version: {} \n".format(VERSION))

    # 检查更新
    print("-正在检查更新...\n")
    if check_for_update(VERSION) == 1:
        print("-当前为最新版本")
    else:
        print("-已有新版本,您可以前往 https://gitee.com/NHJ2001/WeAuth 进行更新。\
        \n或者前往 https://github.com/nearlyheadlessjack/weauth 进行更新。\n")
    # 检查数据库
    DB.check_database()
    
    # 读取配置文件
    try:
        config = read_config()
    except ConfigFileNotFound:
        create_config_yaml()
        print('-首次运行, 请先在config.yaml中进行配置!')
        return None

    # 测试游戏端连接
    if MCSM.test_connection(config['mcsm_adr'], config['mcsm_api'], config['uuid'], config['remote-uuid']) == 200:
        print('-成功连接到游戏服务器!')
    else:
        print('-无法连接到游戏服务器, 请检查config.yaml配置以及网络状况!')
        # sys.exit(1)

    # 测试微信服务器连接
    access_token = test_wechat_server(app_id=config['appID'], app_secret=config['AppSecret'])

    # 连接MCSManager所需要的参数
    mcsm = {
        'adr': config['mcsm_adr'],
        'apikey': config['mcsm_api'],
        'uuid': config['uuid'],
        'remote-uuid': config['remote-uuid']
    }

    # 公众号回复语句
    responses = {
        'welcome': config['welcome']  # 玩家注册白名单成功
    }

    listener = Listener(mcsm=mcsm,
                        wx_user_name=config['WxUserName'],responses=responses)
    # 核心监听程序运行
    listener.wx_service.run(host='0.0.0.0', port='80')


# 读取配置文件
def read_config() -> dict:
    """
    读取配置文件
    :return: 配置信息，以字典形式
    """
    try:
        with open('./config.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        return result
    except FileNotFoundError:
        raise ConfigFileNotFound('未找到配置文件')



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
    

if __name__ == '__main__':
    main()
    
    