from main.core.model.source import Source


class InputEvent:
    '''
    InputEvent is a class content data of user input
    '''

    TYPE_TEXT = 1
    TYPE_AUDIO = 2
    TYPE_IMAGE = 3
    TYPE_VIDEO = 4
    TYPE_STICKER = 5
    TYPE_FILE = 6

    def __init__(self, event_type: int, **kwargs) -> None:
        '''
        :param event_type: the type of this InputEvent.
        :param kwargs: kwargs contents all the detail of this InputEvent
        :param sender: sender is a Sender object that contents all detail of the sender of this InputEvent.
        :param content: content 
         
         
        '''
        self.event_type = event_type
        self.content = kwargs.get('content', '')
        self.event_source = kwargs.get('event_source', Source())
        self.reply_token = kwargs.get('reply_token', '')
