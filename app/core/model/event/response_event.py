from app.core.model.event.input_event import InputEvent


class ResponseEvent:
    TYPE_MESSAGE = 1
    TYPE_AUDIO = 2
    TYPE_IMAGE = 3
    TYPE_VIDEO = 4
    TYPE_STICKER = 5

    def __init__(self, event_type: int, input_event: InputEvent, **kwargs) -> None:
        super().__init__()
        self.event_type = event_type
        self.reply_token = input_event.reply_token
        self.reply_to = input_event.sender

        if event_type == self.TYPE_MESSAGE:
            self.content = kwargs.get('content', '')
        else:
            self.content = kwargs.get('content', None)
