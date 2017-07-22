import logging

import emoji

from main.core.logic.command.name_command_adapter import NameCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.multi_response_event import ResponseMessage
from main.core.model.event.response_event import SingleResponseEvent


class AskingWhoCommandAdapter(NameCommandAdapter):
    keywords = ['我是誰', '你知道我是誰嗎？']

    def can_process(self, input_event: InputEvent) -> bool:
        if super().can_process(input_event):
            message_text = self.filter_out_names(input_event.content)
            return any(message_text == keyword for keyword in self.keywords)
        else:
            return False

    def process(self, input_event: InputEvent) -> SingleResponseEvent:

        logging.info('AskingWhoCommandAdapter >> process:'
                     'start processing')

        response_event = SingleResponseEvent(ResponseMessage.TYPE_TEXT, input_event)

        display_name = input_event.event_source.sender.display_name
        logging.info('AskingWhoCommandAdapter >> process: '
                     'display_name ='+ display_name)

        if display_name is None or len(display_name) <= 0:
            response_event.content = emoji.emojize(
                '我還不認識你耶～\n' +
                '點這個連結讓我們成為好友吧\n' +
                ':arrow_down::arrow_down::arrow_down:\n\n'
                'http://bit.ly/line-bot_stinky-tofu'
                , use_aliases=True
            )
            return response_event

        else:
            response_event.content = emoji.emojize(
                "你是" + display_name + "啊～ :wave::wave:", use_aliases=True
            )
            return response_event
