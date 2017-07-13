class UserMessage:
    TYPE_UNKNOWN = 'TYPE_UNKNOWN'

    def __init__(self, msg_text: str, msg_type: str, reply_to: str = None) -> None:
        super().__init__()
        self.reply_to = reply_to
        self.text = msg_text
        self.type = msg_type
