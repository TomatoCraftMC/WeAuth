import unittest
from weauth.utils.add_op import check_op_id_input

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test1 = 'gjej1mdn'
        test2 = '92nfkdnk1'
        test3 = '@j1kmf'
        test4 = 'ADDDDD___882'
        test5 = 'B B'
        test6 = '____'
        test7 = '-'
        self.assertEqual(check_op_id_input(test1), False)  # add assertion here
        self.assertEqual(check_op_id_input(test2), False)
        self.assertEqual(check_op_id_input(test3), True)
        self.assertEqual(check_op_id_input(test4), False)
        # self.assertEqual(check_op_id_input(test5), True)
        self.assertEqual(check_op_id_input(test6), False)
        self.assertEqual(check_op_id_input(test7), True)


if __name__ == '__main__':
    unittest.main()
