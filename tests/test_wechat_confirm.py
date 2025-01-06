import hashlib
import os
import unittest
from weauth.tencent_server.wx_server import WxConnection

class MyTestCase(unittest.TestCase):
    @unittest.skip('no need')
    def test_wechat_confirm(self):

        self.assertEqual(os.system("WeAuth.py -w"), 0)  # add assertion here

if __name__ == '__main__':
    unittest.main()
