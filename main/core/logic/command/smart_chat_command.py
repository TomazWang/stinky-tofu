from main.chatter.smartbot import SmartBot
from main.core.logic.command.name_command_adapter import NameCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.response_event import ResponseEvent


class SmartChatCommandAdapter(NameCommandAdapter):
    def __init__(self, names) -> None:
        super().__init__(names)
        self.smart_bot = SmartBot()

    def process(self, input_event: InputEvent) -> ResponseEvent:
        message = input_event.content
        response = self.smart_bot.get_response(message)

        res_event = ResponseEvent(ResponseEvent.TYPE_MESSAGE, input_event, content=response)
        return res_event
