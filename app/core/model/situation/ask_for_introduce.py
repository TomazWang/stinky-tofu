import emoji

from app.core.model.situation import Situation


class AskingForIntroduceSitu(Situation):
    TYPE_INTRODUCE = "TYPE_INTRODUCE"

    def __init__(self) -> None:
        super().__init__()
        self.keywords = ['你是誰', '自我介紹']

    def get_response(self, text=""):

        return emoji.emojize('我是臭豆腐機器人，目前還在測試中，請多指教 :smile::thumbsup: \n', use_aliases=True)

    def __contains__(self, command):
        if type(command) is not str:
            raise TypeError

        return any(keyword in command.lower() for keyword in self.keywords)

    def get_message_action(self) -> str:
        return AskingForIntroduceSitu.TYPE_INTRODUCE
