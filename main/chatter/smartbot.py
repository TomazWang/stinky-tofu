from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from main.utils import config_loader


class SmartBot:
    def __init__(self) -> None:
        super().__init__()

        db_uri = config_loader.load_config().db_uri

        self.bot = ChatBot(
            # 這個 ChatBot 的名字叫做 Stanley
            "臭豆腐機器人",
            storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
            database='smart-chatbot-db',
            databae_uri=db_uri,
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
