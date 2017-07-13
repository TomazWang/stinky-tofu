from linebot.models import TextSendMessage

from core import response
from core.msg_parser import *


class Brain:
    """
    Brain is a class that distribute all message and reply as needed.
    """

    def __init__(self, line_bot_api):
        self.line_bot_api = line_bot_api

    def reply(self, reply_token, message):
        self.line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text=message))

    def hear(self, event):
        text = event.message.text

        user_msg = parse_msg(text)

        if user_msg is not None:
            reply_msg = response.response_to(user_msg, event, self.line_bot_api)
            self.reply(event.reply_token, reply_msg)
