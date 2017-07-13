from core.model.situation.abc_situation import Situation


class AskingForIntroduceSitu(Situation):
    TYPE_INTRODUCE = "TYPE_INTRODUCE"

    def __init__(self) -> None:
        super().__init__()
        self.keywords = ['你是誰', '自我介紹']

    def get_response(self):
        return '我是臭豆腐機器人，目前還在測試中，請多指教 \U0x10008D \n'

    def __contains__(self, command):
        if type(command) is not str:
            raise TypeError

        return any(keyword in command.lower() for keyword in self.keywords)

    def get_message_type(self) -> str:
        return AskingForIntroduceSitu.TYPE_INTRODUCE
