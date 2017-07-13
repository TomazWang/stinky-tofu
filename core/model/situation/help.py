
from core.model.situation.abc_situation import Situation


class AskingForHelpSitu(Situation):
    TYPE_HELP = "TYPE_HELP"

    def __init__(self) -> None:
        super().__init__()
        self.keywords = ['說明', '幫助', '解釋']

    def get_response(self):
        # todo
        return '我是臭豆腐機器人，目前還在測試中，請多指教 \U0x10008D \n'

    def __contains__(self, command):
        if type(command) is not str:
            raise TypeError

        return any(keyword in command.lower() for keyword in self.keywords)

    def get_message_type(self) -> str:
        return AskingForHelpSitu.TYPE_HELP
