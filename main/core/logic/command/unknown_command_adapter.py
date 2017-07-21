from main.core.logic.command.name_command_adapter import NameCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.multi_response_event import ResponseMessage
from main.core.model.event.response_event import SingleResponseEvent


class UnknownCommandAdapter(NameCommandAdapter):
    def process(self, input_event: InputEvent) -> SingleResponseEvent:
        response = '我不清楚你在說什麼'
        res_event = SingleResponseEvent(ResponseMessage.TYPE_TEXT, input_event, content=response)
        return res_event
