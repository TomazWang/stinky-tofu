from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class SmartBot:
    bot = ChatBot(
        # 這個 ChatBot 的名字叫做 Stanley
        "臭豆腐機器人",
        storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
        database='auto_chatbot-db'
    )

    def __init__(self) -> None:
        super().__init__()
        # 建立一個 ChatBot
        self.bot.set_trainer(ChatterBotCorpusTrainer)

        self.bot.train(
            "./corpus/greeting/greetings.yml",
            "./corpus/nerd/science.yml"
        )

    def get_response(self, message=""):
        return self.bot.get_response(message)