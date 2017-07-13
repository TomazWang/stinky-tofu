from core.model.situation.abc_situation import Situation


class EchoSitu(Situation):
    TYPE_ECHO = "TYPE_ECHO"

    def __init__(self) -> None:
        super().__init__()
        self.keywords = ['說', '重複']
        self.context = '不好意思請問你要我說什麼？'

    def get_response(self):
        return self.context

    def __contains__(self, text):
        if type(text) is not str:
            raise TypeError

        command = text.split(" ", 2)[0]
        context = text.split(" ", 2)[1]
        self.context = context
        return any(keyword in command.lower() for keyword in self.keywords)

    def get_message_type(self) -> str:
        return EchoSitu.TYPE_ECHO
