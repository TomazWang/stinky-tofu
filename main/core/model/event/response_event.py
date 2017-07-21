from main.core.model.event.input_event import InputEvent
from main.core.model.event.multi_response_event import ResponseEvent, ResponseMessage


class SingleResponseEvent(ResponseEvent):
    """
    ResponseEvent is the older version of Response. 
    It basically contains only one Response at a time.
    """
    def __init__(self, event_type: int, input_event: InputEvent, **kwargs) -> None:
        super().__init__(input_event)
        self.event_type = event_type

        kwargs['res_type'] = event_type
        self.add_response(ResponseMessage(**kwargs))
