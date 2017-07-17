from linebot import LineBotApi
from linebot.models import MessageEvent

from app.core.event_adapter.line_msg_adapter import LineMessageEventAdapter
from app.core.model.event.input_event import InputEvent
from app.core.model.event.response_event import ResponseEvent


class LineCommandBot:
    '''
    CommandBot handles InputEvents and return ResponseEvent.
    '''

    def __init__(self, line_bot_api: LineBotApi, **kwargs) -> None:
        super().__init__()
        line_msg_adapter = LineMessageEventAdapter(line_bot_api)
        self.input_adapter = kwargs.get('input_adapter', line_msg_adapter)
        self.output_adapter = kwargs.get('output_adapter', line_msg_adapter)
        self.command_adapters = kwargs.get('command_adapter', [])

    def get_response(self, input_event: InputEvent) -> ResponseEvent:
        for command_adapter in self.command_adapters:
            if command_adapter.can_process(input_event):
                return command_adapter.process(input_event)

    def handle_message_event(self, msg_event: MessageEvent):
            input_event = self.input_adapter.handle_input(msg_event)
            res_event = self.get_response(input_event)
            self.output_adapter.handle_response(res_event)


