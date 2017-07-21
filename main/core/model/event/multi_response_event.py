from main.core.model.event.input_event import InputEvent


class ResponseMessage:
    """
    Response is an object that contains data that will be send back to user.
    
    
    :keyword    content:    The text content of the message response. 
                            It also can be the url of an image message or a file message.
    :type       content:    str
    
    :keyword    res_type:  The type of this response.
    :type       res_type:  int
    """
    TYPE_TEXT = 1
    TYPE_AUDIO = 2
    TYPE_IMAGE = 3
    TYPE_VIDEO = 4
    TYPE_STICKER = 5

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.content = kwargs.get('content', '')
        self.res_type = kwargs.get('res_type', -1)


class ResponseEvent:
    """
    MultiResponseEvent can store multiple response at once. It's helpful for a response that 
    contents more than one types. e.g. "It's a partly clodly day tomorrow !! + (a image of 
    cloud)" 
    """

    def __init__(self, input_event: InputEvent) -> None:
        """
        :param input_event: the input_event which this response event should reply to. 
        :type input_event: InputEvent
        """
        super().__init__()
        self.input_event = input_event
        self.responses = []

    def add_response(self, res: ResponseMessage):
        """
        add a response to response queue.
        :param res: the Response object.
        :return: None
        """
        self.responses.append(res)
