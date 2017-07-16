class UserMessage:
    TYPE_UNKNOWN = 'TYPE_UNKNOWN'

    def __init__(self, msg_context: str, msg_action: str, reply_to: str = None) -> None:
        super().__init__()
        self.reply_to = reply_to
        self.context = msg_context
        self.action = msg_action

