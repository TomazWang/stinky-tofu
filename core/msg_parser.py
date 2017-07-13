from typing import Optional


class UserMessage:
    # greeting (ex. Hi, Hello ...)
    TYPE_GREETING = 'TYPE_GREETING'

    # roll a die
    TYPE_ROLL_DIE = 'TYPE_ROLL_DIE'

    # set a nickname
    TYPE_RENAME = 'TYPE_RENAME'

    # user ask who is he/she
    TYPE_WHO = 'TYPE_WHO'

    # ask for help
    TYPE_HELP = 'TYPE_HELP'

    TYPE_SIMPLE_ECHO = 'TYPE_SIMPLE_ECHO'

    TYPE_INTRODUCE = 'TYPE_INTRODUCE'

    TYPE_UNKNOWN = 'TYPE_UNKNOWN'

    def __init__(self, msg_text: str, msg_type: str, reply_to: str = None) -> None:
        super().__init__()
        self.reply_to = reply_to
        self.text = msg_text
        self.type = msg_type


def is_command_who(text):
    keywords = ['我是誰', 'who am i']
    return any(keyword in text.lower() for keyword in keywords)


def is_command_introduce(text):
    keywords = ['你是誰', 'who are you']
    return any(keyword in text.lower() for keyword in keywords)


def parse_simple_command(text):
    type_str = UserMessage.TYPE_UNKNOWN

    if is_command_who(text):
        type_str = UserMessage.TYPE_WHO
    elif is_command_introduce(text):
        type_str = UserMessage.TYPE_INTRODUCE

    return type_str


BOT_NAMES = ['臭豆腐', 'stinky', '機器人', 'bot']


def parse_msg(text: str, reply_to: str = None, skip_check=False) -> Optional[UserMessage]:
    text = text.lstrip()
    is_calling_me = any(text.lower().startswith(bot_name) for bot_name in BOT_NAMES)

    if not skip_check and not is_calling_me:
        return None

    if reply_to is None:
        msg_type = parse_simple_command(text)
        return UserMessage(text, msg_type)
