from typing import Optional, List

from core.model.situation.abc_situation import Situation
from core.model.user_message import UserMessage


class MessageParser:
    def __init__(self, bot_names: List[str], situations: List[Situation]) -> None:
        super().__init__()
        self.situations = situations
        self.bot_names = bot_names

    def parse_simple_command(self, text) -> str:

        for situ in self.situations:
            if text in situ:
                return situ.get_message_type()

        return UserMessage.TYPE_UNKNOWN

    def parse_msg(self, text: str, reply_to: str = None, skip_check=False) -> Optional[UserMessage]:
        text = text.lstrip()

        calling_str = text.split(" ", 2)[0]
        command_str = text.split(" ", 2)[1]

        is_calling_me = any(calling_str.lower().startswith(bot_name) for bot_name in self.bot_names)

        if not skip_check and not is_calling_me:
            return None

        if reply_to is None:
            msg_type = self.parse_simple_command(command_str)
            return UserMessage(text, msg_type)
