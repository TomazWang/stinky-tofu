from main.core.logic.command.name_command_adapter import NameCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.response_event import ResponseEvent


class UnknownCommandAdapter(NameCommandAdapter):
    def process(self, input_event: InputEvent) -> ResponseEvent:
        response = '我不清楚你在說什麼'
        res_event = ResponseEvent(ResponseEvent.TYPE_MESSAGE, input_event, content=response)
        return res_event
