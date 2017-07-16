# import configparser
import os

class Config:
    def __init__(self):
        self.channel_secret = os.environ['CHANNEL_SECRET']
        self.channel_access_token = os.environ['CHANNEL_ACCESS_TOKEN']
#         if 'CHANNEL' in config:
#             channel_config = config['CHANNEL']
#             self.channel_secret = channel_config['channel_secret']
#             self.channel_access_token = channel_config['channel_access_token']


def load_config() -> Config:
    return Config()
    # config = configparser.ConfigParser()
    # config.read('../config.ini')
    # return Config(config)
