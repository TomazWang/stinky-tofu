from chatterbot import ChatBot
from chatterbot.conversation.statement import Statement
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

        greeting_path = setting.PROJECT_ROOT + '/chatter/corpus/greeting/'
        nerd_path = setting.PROJECT_ROOT + '/chatter/corpus/nerd/'

        self.bot.train(
            greeting_path + 'greetings.yml',
            nerd_path + 'science.yml'
        )

        # for debug
        gretting_file_path = greeting_path + 'greetings.yml'
        with open(gretting_file_path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                print(line)

    def get_response(self, message="") -> Statement:
        print('get response from =', message)
        return self.bot.get_response(message)

    def export_datas(self):
        export_path = setting.PROJECT_ROOT + '/chatter/output/export.json'
        self.bot.trainer.export_for_training(export_path)

    def stop(self):
        self.export_datas()
