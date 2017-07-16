import unittest

from core.model.user_message import UserMessage
from core.msg_parser import MessageParser

from app.core.model.situation import AskingForIntroduceSitu
from app.core.model.situation import EchoSitu


class TestMessageParser(unittest.TestCase):
    def test_parse_msg(self):
        self.situ_introduce = AskingForIntroduceSitu()
        # self.situ_who = AskingForIntroduceSitu()
        self.situ_echo = EchoSitu()

        parser = MessageParser(
            ['機器人', '臭豆腐'],
            [
                self.situ_introduce,
                self.situ_echo
            ]
        )

        usr_msg = parser.parse_msg('機器人 你好')
        self.assertEqual(usr_msg.action, UserMessage.TYPE_UNKNOWN)
        self.assertEqual(usr_msg.context, "你好")

        usr_msg = parser.parse_msg('機器人 你是誰')
        self.assertEqual(usr_msg.action, AskingForIntroduceSitu().get_message_action())
        self.assertEqual(usr_msg.context, "你是誰")

        usr_msg = parser.parse_msg('機器人 說 你好')
        self.assertEqual(usr_msg.action, EchoSitu().get_message_action())
        self.assertEqual(usr_msg.context, "說 你好")

        usr_msg = parser.parse_msg('臭豆腐說 比比是豬')
        self.assertEqual(usr_msg.action, EchoSitu().get_message_action())
        self.assertEqual(usr_msg.context, "說 比比是豬")

        # usr_msg = parser.parse_msg('臭豆腐 你好')
        # self.assertEqual(usr_msg.type, EchoSitu().get_message_type())
        # self.assertEqual(usr_msg.text, "你好")

        usr_msg = parser.parse_msg('臭豆腐，我是誰？')
        # self.assertEqual(usr_msg.type, AskingWhoSitu().get_message_type())
        self.assertEqual(usr_msg.context, "我是誰？")


if __name__ == '__main__':
    unittest.main()
