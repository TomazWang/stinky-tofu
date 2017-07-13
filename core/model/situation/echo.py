from core.model.situation.abc_situation import Situation


class EchoSitu(Situation):
    TYPE_ECHO = "TYPE_ECHO"
    DEFAULT_RESPONSE = '不好意思請問你要我說什麼呢？'

    def __init__(self) -> None:
        super().__init__()
        self.keywords = ['說', '重複']

    def get_response(self, text=""):
        reply = EchoSitu.DEFAULT_RESPONSE
        print("EchoSitu: get_response --- ", "text = ", text)
        sp = text.split(" ", 1)
        print("EchoSitu: get_response --- ", "sp = ", sp)

        if len(sp) > 1 and len(sp[1].strip()) > 0:
            reply = sp[1]
            print("EchoSitu: get_response --- ", "reply = ", reply)
        return reply

    def __contains__(self, text):
        if type(text) is not str:
            raise TypeError

        sp = text.split(" ", 1)
        command = sp[0]

        if any(keyword in command.lower() for keyword in self.keywords):
            return True
        else:
            return False

    def get_message_type(self) -> str:
        return EchoSitu.TYPE_ECHO
