import configparser


class Config:
    def __init__(self, config):
        if 'CHANNEL' in config:
            channel_config = config['CHANNEL']
            self.channel_secret = channel_config['channel_secret']
            self.channel_access_token = channel_config['channel_access_token']


def load_config() -> Config:
    config = configparser.ConfigParser()
    config.read('../config.ini')
    return Config(config)
