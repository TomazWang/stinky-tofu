from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from main import setting
from main.utils import config_loader


class SmartBot:
    def __init__(self) -> None:
        super().__init__()

        db_uri = config_loader.load_config().mongodb_uri
        db_name = config_loader.load_config().db_name
        # db_uri = config_loader.load_config().db_uri

        print('db_uri =', db_uri, ', db_name =', db_name)

        self.bot = ChatBot(
            # 這個 ChatBot 的名字叫做 Stanley
            "臭豆腐機器人",
            database=db_name,
            database_uri=db_uri,
            storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
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

        greeting_file_path = setting.PROJECT_ROOT + '/chatter/corpus/greeting/greetings.yml'
        science_file_path = setting.PROJECT_ROOT + '/chatter/corpus/nerd/science.yml'

        self.bot.train(
            greeting_file_path,
            science_file_path
        )

    def get_response(self, message=""):
        return self.bot.get_response(message)

    def export_datas(self):
        export_path = setting.PROJECT_ROOT + '/chatter/output/export.json'
        self.bot.trainer.export_for_training(export_path)

    def stop(self):
        self.export_datas()
