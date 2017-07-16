from unittest import TestCase

from core.model.user_message import UserMessage
from core.response import response_to

from app.core.model.situation import AskingForIntroduceSitu
from app.core.model.situation import EchoSitu

situations = [
    AskingForIntroduceSitu(),
    EchoSitu(),
]


class TestResponse_to(TestCase):
    def test_response_to(self):
        usr_msg = UserMessage("", AskingForIntroduceSitu().get_message_action())
        response_msg = response_to(usr_msg, situations)
        self.assertEqual(response_msg, AskingForIntroduceSitu().get_response())

        usr_msg = UserMessage("說 你好", EchoSitu().get_message_action())
        response_msg = response_to(usr_msg, situations)
        self.assertEqual(response_msg, "你好")

        usr_msg = UserMessage("說 hi", EchoSitu().get_message_action())
        response_msg = response_to(usr_msg, situations)
        self.assertEqual(response_msg, "hi")
