import abc

from app.core.model import UserMessage


class Situation(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __contains__(self, item):
        pass

    @abc.abstractmethod
    def get_response(self, text="") -> str:
        pass

    @abc.abstractmethod
    def get_message_action(self) -> str:
        return UserMessage.TYPE_UNKNOWN
