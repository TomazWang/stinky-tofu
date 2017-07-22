import logging

from main.core.logic.command.name_command_adapter import NameCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.multi_response_event import ResponseMessage
from main.core.model.event.response_event import SingleResponseEvent
from main.utils import cht_utils


class EchoCommandAdapter(NameCommandAdapter):
    keywords = ['說', '跟我說', '重複']

    def can_process(self, input_event: InputEvent) -> bool:
        if not super().can_process(input_event):
            return False

        message_text = super().filter_out_names(input_event.content).lstrip()
        message_text = cht_utils.strip_leading_ch_symbol(message_text)
        return any(message_text.startswith(kw) for kw in self.keywords)

    def process(self, input_event: InputEvent) -> SingleResponseEvent:
        message_text = super().filter_out_names(input_event.content).strip()
        logging.info('EchoCommandAdapter >> process: message_text = ({})'.format(message_text))
        message_text = cht_utils.strip_leading_ch_symbol(message_text)
        logging.info('EchoCommandAdapter >> process: message_text = ({})'.format(message_text))

        for kw in self.keywords:
            if message_text.startswith(kw):
                message_text = message_text[len(kw):]

        message_text = message_text.lstrip()

        res_event = SingleResponseEvent(ResponseMessage.TYPE_TEXT, input_event, content=message_text)
        return res_event
