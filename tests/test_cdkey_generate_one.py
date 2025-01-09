import unittest
from unittest.mock import patch
from weauth.cdkey.cdkey import CDKey
import string


class TestCDKey(unittest.TestCase):

    def test_generate_cdkey_one_PositiveLength_CorrectFormat(self):
        cdkey = CDKey.generate_cdkey_one()
        print(cdkey)
        self.assertTrue(len(cdkey) == 19)  # 4*4 + 3（连字符）
        self.assertTrue(all(c in string.ascii_letters + string.digits + '-' for c in cdkey))
        self.assertTrue(cdkey.count('-') == 3)
