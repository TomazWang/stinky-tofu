from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class SmartBot:
    bot = ChatBot(
        # 這個 ChatBot 的名字叫做 Stanley
        "臭豆腐機器人",
        storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
        database='auto_chatbot-db',
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
                "response_selection_method": "chatterbot.response_selection.get_first_response"
            },
            {
                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                'threshold': 0.65,
                'default_response': '我不清楚你在說什麼'
            }
        ]

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

    def export_datas(self):
        self.bot.trainer.export_for_training('./export.json')

    def stop(self):
        self.export_datas()
