from linebot import LineBotApi
from linebot.models import MessageEvent

from main.core.event_adapter.line_msg_adapter import LineMessageEventAdapter
from main.core.logic.command.asking_who_command_adpater import AskingWhoCommandAdapter
from main.core.logic.command.echo_command_adapter import EchoCommandAdapter
from main.core.logic.command.introduce_command_adpater import IntroduceCommandAdapter
from main.core.logic.command.roll_die_command import RollDiceCommandAdpater
from main.core.logic.command.smart_chat_command import SmartChatCommandAdapter
from main.core.logic.command.unknown_command_adapter import UnknownCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.multi_response_event import ResponseEvent


class LineCommandBot:
    '''
    CommandBot handles InputEvents and return ResponseEvent.
    '''

    def __init__(self, line_bot_api: LineBotApi) -> None:
        super().__init__()
        line_msg_adapter = LineMessageEventAdapter(line_bot_api)
        self.input_adapter = line_msg_adapter
        self.output_adapter = line_msg_adapter
        self.names = ['機器人', '臭豆腐']
        self.command_adapters = [
            AskingWhoCommandAdapter(self.names),
            EchoCommandAdapter(self.names),
            IntroduceCommandAdapter(self.names),
            RollDiceCommandAdpater(self.names),
            SmartChatCommandAdapter(self.names)
        ]
        self.default_command_adapter = UnknownCommandAdapter(self.names)

    def get_response(self, input_event: InputEvent) -> ResponseEvent:
        for command_adapter in self.command_adapters:
            if command_adapter.can_process(input_event):
                return command_adapter.process(input_event)

        if self.default_command_adapter.can_process(input_event):
            return self.default_command_adapter.process(input_event)

    def handle_message_event(self, msg_event: MessageEvent):
        input_event = self.input_adapter.handle_input(msg_event)
        res_event = self.get_response(input_event)
        self.output_adapter.handle_response(res_event)
