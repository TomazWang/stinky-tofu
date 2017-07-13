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
