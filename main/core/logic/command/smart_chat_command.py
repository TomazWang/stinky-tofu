from main.chatter.smartbot import SmartBot
from main.core.logic.command.name_command_adapter import NameCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.multi_response_event import ResponseMessage
from main.core.model.event.response_event import SingleResponseEvent


class SmartChatCommandAdapter(NameCommandAdapter):
    def __init__(self, names) -> None:
        super().__init__(names)
        self.smart_bot = SmartBot()

    def process(self, input_event: InputEvent) -> SingleResponseEvent:
        message = input_event.content
        statement = self.smart_bot.get_response(message)

        res_event = SingleResponseEvent(ResponseMessage.TYPE_TEXT, input_event, content=statement.text)
        return res_event
