import unittest
from weauth.mc_server import MCServerConnection
import yaml
from weauth.exceptions import ConfigFileNotFound
import sys

@unittest.skip('local')
class MyTestCase(unittest.TestCase):
    def test_something(self):
        game_server = MCServerConnection()
        config = MyTestCase.read_config()

        if config['server_connect'] == 0:
            server_type = 'MCSM'
            game_server = MCServerConnection(config['mcsm_adr'],
                                             config['mcsm_api'],
                                             config['uuid'],
                                             config['remote-uuid'], server_type=server_type)
        elif config['server_connect'] == 1:
            server_type = 'RCON'
            game_server = MCServerConnection(config['rcon_host_add'],
                                             config['rcon_port'],
                                             config['rcon_password'],
                                             server_type=server_type)
        else:
            print('-错误的服务器类型')
            sys.exit(1)
        return_cdoe, msg = game_server.push_command(command='tell @p hello wolrd')

        print('{}'.format(repr(msg)))

        self.assertEqual(return_cdoe, 201)  # add assertion here
    @staticmethod
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

if __name__ == '__main__':
    unittest.main()
