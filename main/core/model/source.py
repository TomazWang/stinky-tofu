class Sender:
    def __init__(self, sender_id: str, **kwargs) -> None:
        super().__init__()
        self.sender_id = sender_id
        self.display_name = kwargs.get('display_name', '')
        self.profile_photo_url = kwargs.get('profile_photo_url', '')

        # todo add some more...


class Group:
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.group_id = kwargs.get('group_id', '')
        self.group_name = kwargs.get('group_name', '')


class Room:
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.room_id = kwargs.get('room_id', '')
        self.room_name = kwargs.get('room_name', '')


class UnknownSender(Sender):
    def __init__(self) -> None:
        super().__init__('0')


class Source:
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.sender = kwargs.get('sender', UnknownSender())
        self.group = kwargs.get('group', None)
        self.room = kwargs.get('room', None)
