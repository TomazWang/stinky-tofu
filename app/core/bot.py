from core import response
from core.msg_parser import MessageParser
from linebot.models import TextSendMessage, MessageEvent

from app.core.model.situation import AskingForIntroduceSitu
from app.core.model.situation import AskingWhoSitu
from app.core.model.situation import EchoSitu


class Brain:
    """
    Brain is a class that distribute all message and reply as needed.
    """

    def __init__(self, event: MessageEvent, line_bot_api):
        self.event = event
        self.line_bot_api = line_bot_api

        self.user_id = event.source.user_id

        self.situations = [
            AskingWhoSitu(user_id=self.user_id, api=line_bot_api),
            AskingForIntroduceSitu(),
            EchoSitu()
        ]
        self.ear = MessageParser(
            ['臭豆腐', 'stinky', '機器人'],
            self.situations
        )

    def reply(self, reply_token, message):
        self.line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text=message))

    def hear(self, event):
        text = event.message.text

        user_msg = self.ear.parse_msg(text)

        if user_msg is not None:
            reply_msg = response.response_to(user_msg, self.situations)
            self.reply(event.reply_token, reply_msg)
