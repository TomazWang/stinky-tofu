from main.core.logic.command.name_command_adapter import NameCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.response_event import ResponseEvent
from main.utils import cht_utils


class EchoCommandAdapter(NameCommandAdapter):
    keywords = ['說', '跟我說', '重複']

    def can_process(self, input_event: InputEvent) -> bool:
        if not super().can_process(input_event):
            return False

        message_text = super().filter_out_names(input_event.content).lstrip()
        message_text = cht_utils.strip_leading_ch_symbol(message_text)
        return any(message_text.startswith(kw) for kw in self.keywords)

    def process(self, input_event: InputEvent) -> ResponseEvent:
        message_text = super().filter_out_names(input_event.content).strip()
        print('message_text = ('+message_text+')')
        message_text = cht_utils.strip_leading_ch_symbol(message_text)
        print('message_text = ('+message_text+')')

        for kw in self.keywords:
            if message_text.startswith(kw):
                print('find kw :', kw)
                message_text = message_text[len(kw):]
                print('message_text = ('+message_text+')')

        message_text = message_text.lstrip()
        print('message_text = ('+message_text+')')

        res_event = ResponseEvent(ResponseEvent.TYPE_MESSAGE, input_event, content=message_text)
        return res_event
