from unittest import TestCase

from core.model.situation.ask_for_introduce import AskingForIntroduceSitu
from core.model.situation.echo import EchoSitu
from core.model.user_message import UserMessage
from core.response import response_to

situations = [
    AskingForIntroduceSitu(),
    EchoSitu()
]


class TestResponse_to(TestCase):
    def test_response_to(self):
        usr_msg = UserMessage("", AskingForIntroduceSitu().get_message_type())
        response_msg = response_to(usr_msg, situations)
        self.assertEqual(response_msg, AskingForIntroduceSitu().get_response())

        usr_msg = UserMessage("說 你好", EchoSitu().get_message_type())
        response_msg = response_to(usr_msg, situations)
        self.assertEqual(response_msg, "你好")

        usr_msg = UserMessage("說 hi", EchoSitu().get_message_type())
        response_msg = response_to(usr_msg, situations)
        self.assertEqual(response_msg, "hi")
