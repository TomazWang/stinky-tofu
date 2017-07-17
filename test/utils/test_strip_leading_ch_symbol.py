import unittest

from main.utils import cht_utils


class TestStrip_leading_ch_symbol(unittest.TestCase):
    def test_strip_leading_ch_symbol(self):
        self.assertEqual(cht_utils.strip_leading_ch_symbol('？你好'),'你好')
        self.assertEqual(cht_utils.strip_leading_ch_symbol('！！，你好？'),'你好？')
        self.assertEqual(cht_utils.strip_leading_ch_symbol('你好？'),'你好？')
        self.assertEqual(cht_utils.strip_leading_ch_symbol('！！！你居然，有逗點，卡中間'),'你居然，有逗點，卡中間')
        # self.assertEqual(cht_utils.strip_leading_ch_symbol('?你好'),'你好')

if __name__ == '__main__':
    unittest.main()
