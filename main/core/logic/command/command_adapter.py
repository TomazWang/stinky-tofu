import abc

from main.core.model.event.input_event import InputEvent
from main.core.model.event.response_event import ResponseEvent


class CommandAdapter(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def can_process(self, input_event: InputEvent) -> bool:
        pass

    @abc.abstractmethod
    def process(self, input_event: InputEvent) -> ResponseEvent:
        pass
