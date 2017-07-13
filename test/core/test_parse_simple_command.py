import unittest

from core.msg_parser import parse_msg, UserMessage


class TestMsg_Parser(unittest.TestCase):
    def test_parse_msg(self):
        self.assertEqual(parse_msg('我是誰'), None)
        self.assertEqual(parse_msg('機器人，我是誰').type, UserMessage.TYPE_WHO)


if __name__ == '__main__':
    unittest.main()
