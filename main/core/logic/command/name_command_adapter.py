import abc

from main.core.logic.command.command_adapter import CommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.response_event import ResponseEvent


class NameCommandAdapter(CommandAdapter):
    def __init__(self, names) -> None:
        super().__init__()
        self.alias = names

    def can_process(self, input_event: InputEvent) -> bool:
        if not input_event.event_type == InputEvent.TYPE_TEXT:
            return False

        message_text = input_event.source_content.lstrip()

        if any(message_text.startswith(name) for name in self.alias):
            return True

    @abc.abstractmethod
    def process(self, input_event: InputEvent) -> ResponseEvent:
        pass

    def filter_out_names(self, content_text) -> str:
        """
        Filter out bot names from the start of the content_text. 
        e.g. <bot_name_1> <bot_name_2> <some_string> --> <some_string>
        
        :param content_text: the source text
        :return: 
        """

        message_text = content_text.lstrip()

        for name in self.alias:
            if message_text.startswith(name):
                message_text = self.filter_out_names(message_text[len(name):])
                break

        return message_text
