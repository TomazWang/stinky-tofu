import unittest

from core.model.situation.ask_for_introduce import AskingForIntroduceSitu
from core.model.situation.echo import EchoSitu
from core.model.user_message import UserMessage
from core.msg_parser import MessageParser


class TestMessageParser(unittest.TestCase):
    def test_parse_msg(self):
        parser = MessageParser(
            ['機器人'],
            [
                AskingForIntroduceSitu(),
                EchoSitu()
            ]
        )

        usr_msg = parser.parse_msg('機器人 你好')
        self.assertEqual(usr_msg.type, UserMessage.TYPE_UNKNOWN)
        self.assertEqual(usr_msg.text, "你好")

        usr_msg = parser.parse_msg('機器人 你是誰')
        self.assertEqual(usr_msg.type, AskingForIntroduceSitu().get_message_type())
        self.assertEqual(usr_msg.text, "你是誰")

        usr_msg = parser.parse_msg('機器人 說 你好')
        self.assertEqual(usr_msg.type, EchoSitu().get_message_type())
        self.assertEqual(usr_msg.text, "說 你好")


if __name__ == '__main__':
    unittest.main()
