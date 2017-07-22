import logging

from linebot.api import LineBotApi
from linebot.models import MessageEvent, TextSendMessage
from linebot.models.messages import StickerMessage

from main.core.model.event.input_event import InputEvent
from main.core.model.event.multi_response_event import ResponseEvent, ResponseMessage
from main.core.model.source import Sender, Source, Room, Group
from main.utils.line_sticker_utls import StickerUtils


class LineMessageEventAdapter:
    """
    LineMessageEventAdapter is parse a line message event to an InputEvent obj.
    """

    def __init__(self, line_api: LineBotApi) -> None:
        super().__init__()
        self.line_bot_api = line_api

    def handle_input(self, msg_event: MessageEvent) -> InputEvent:

        # source

        source = Source()

        user_id = msg_event.source.user_id
        if user_id is not None and len(user_id) > 0:

            try:
                logging.info(
                    'LineMessageEventAdapter >> '
                    'handle_input: handle user_profile, user_id = ' + user_id)

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
        logging.info('handle_response:')

        if res_event is None:
            # do nothing if no response required
            logging.info('handle_response: no response.')
            return

        messages = []
        for response in res_event.responses:

            if response.res_type == ResponseMessage.TYPE_TEXT:
                message = response.content
                logging.info('handle_response: message response = ' + message)

                messages.append(TextSendMessage(text=message))

            elif response.res_type == ResponseMessage.TYPE_STICKER:
                pkg_id, stk_id = StickerUtils.uri_to_id(response.content)
                logging.info('handle_reponse: pkg_id = {}, stk_id = {}'.format(pkg_id, stk_id))

                messages.append(StickerMessage(package_id=pkg_id, sticker_id=stk_id))

        logging.info('handle_reponse: messages = {}'.format(messages))
        reply_token = res_event.input_event.reply_token
        logging.info('handle_response: reply_token = ' + reply_token)

        self.line_bot_api.reply_message(reply_token, messages)
