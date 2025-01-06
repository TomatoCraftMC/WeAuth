import hashlib
import unittest
from weauth.tencent_server.wx_server import WxConnection

class MyTestCase(unittest.TestCase):
    @unittest.skip('no need')
    def test_wechat_confirm(self):
        token = '111'
        timestamp = '111'
        nonce = '111'
        echo_str = 111
        signature = '111'
        result = WxConnection.confirm_token(token,timestamp,nonce,echo_str,signature)
        temp_list = [token,timestamp,nonce]
        temp_list.sort()
        temp = ''.join(temp_list)
        sha1 = hashlib.sha1(temp.encode('utf-8'))
        hashcode = sha1.hexdigest()

        self.assertEqual(result, hashcode)  # add assertion here

if __name__ == '__main__':
    unittest.main()
