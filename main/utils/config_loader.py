# import configparser
import os


class Config:
    def __init__(self):
        self.channel_secret = os.environ.get('CHANNEL_SECRET', '')
        self.channel_access_token = os.environ.get('CHANNEL_ACCESS_TOKEN', '')
        self.mongodb_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
        self.db_uri = os.environ.get('DB_URI', '127.0.0.1')
        self.db_name = os.environ.get('DB_NAME', 'stinky-db')


# if 'CHANNEL' in config:
#             channel_config = config['CHANNEL']
#             self.channel_secret = channel_config['channel_secret']
#             self.channel_access_token = channel_config['channel_access_token']


def load_config() -> Config:
    return Config()
    # config = configparser.ConfigParser()
    # config.read('../config.ini')
    # return Config(config)
