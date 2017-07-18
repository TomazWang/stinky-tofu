import json

from linebot.api import LineBotApi
from linebot.models import MessageEvent, TextSendMessage

from main.core.model.event.input_event import InputEvent
from main.core.model.event.response_event import ResponseEvent
from main.core.model.source import Sender, Source, Room, Group


class LineMessageEventAdapter:
    '''
    LineMessageEventAdapter is parse a line message event to an InputEvent obj.
    '''

    def __init__(self, line_api: LineBotApi) -> None:
        super().__init__()
        self.line_bot_api = line_api

    def handle_input(self, msg_event: MessageEvent) -> InputEvent:

        # source

        source = Source()

        user_id = msg_event.source.user_id
        if user_id is not None and len(user_id) > 0:

            try:
                user_profile = self.line_bot_api.get_profile(user_id)
                sender = Sender(user_id,
                                display_name=user_profile.display_name,
                                profile_photo_url=user_profile.picture_url
                                )
                source.sender = sender
            except:
                pass

        if msg_event.source.type == 'room':
            room_id = msg_event.source.room_id
            source.room = Room(room_id=room_id)
        elif msg_event.source.type == 'group':
            group_id = msg_event.source.group_id
            source.group = Group(group_id=group_id)

        # content
        message = msg_event.message
        message_type = -1
        message_content = None
        if message.type == 'text':
            message_type = InputEvent.TYPE_TEXT
            message_content = message.text
        elif message.type == 'image':
            message_type = InputEvent.TYPE_IMAGE
            message_content = message.id
        elif message.type == 'video':
            message_type = InputEvent.TYPE_VIDEO
            message_content = message.id
        elif message.type == 'audio':
            message_type = InputEvent.TYPE_AUDIO
            message_content = message.id
        elif message.type == 'file':
            message_type = InputEvent.TYPE_FILE
            message_content = message.id
        elif message.type == 'sticker':
            message_type = InputEvent.TYPE_STICKER
            message_content = (message.stickerId, message.stickerId)

        input_event = InputEvent(
            message_type,
            content=message_content,
            reply_token=msg_event.reply_token,
            event_source=source
        )

        return input_event

    def handle_response(self, res_event: ResponseEvent):
        print('handle_response:')

        if res_event is None:
            # do nothing if no response required
            print('handle_response:', 'no response.')
            return
        if res_event.event_type == res_event.TYPE_MESSAGE:
            message = res_event.content
            print('handle_response:', 'message response =', message)
            print('handle_response:', 'reply_token =', res_event.reply_token)

            data = {
                'replyToken': res_event.reply_token,
                'messages': TextSendMessage(text=message).as_json_dict()
            }

            print(json.dumps(data))

            self.line_bot_api.reply_message(
                res_event.reply_token,
                TextSendMessage(text=message))
