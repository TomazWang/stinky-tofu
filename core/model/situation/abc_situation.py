import abc

from core.model.user_message import UserMessage


class Situation(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __contains__(self, item):
        pass

    @abc.abstractmethod
    def get_response(self, text="") -> str:
        pass

    @abc.abstractmethod
    def get_message_type(self) -> str:
        return UserMessage.TYPE_UNKNOWN
