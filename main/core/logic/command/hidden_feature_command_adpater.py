from main.core.logic.command.command_adapter import CommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.multi_response_event import ResponseEvent, ResponseMessage
from main.utils.line_sticker_utls import StickerUtils


class HiddenFeatureCommandAdapter(CommandAdapter):
    def can_process(self, input_event: InputEvent) -> bool:
        return input_event.event_type == InputEvent.TYPE_TEXT and input_event.content.startswith(
            'debug')

    def handle_sticker_debug(self, data):
        if len(data) == 3:
            pkg_id = data[1]
            stk_id = data[2]
            uri = StickerUtils.id_to_uri(pkg_id, stk_id)
            res_msg = ResponseMessage(
                res_type=ResponseMessage.TYPE_STICKER,
                content=uri)
            return res_msg

    def process(self, input_event: InputEvent) -> ResponseEvent:
        res_event = ResponseEvent(input_event)

        msg = input_event.content.replace('debug', '').lstrip()

        if msg.startswith('sticker'):
            data = msg.split()
            sticker_res = self.handle_sticker_debug(data)
            res_event.add_response(sticker_res)

        if res_event.response_count() <= 0:
            res_event.add_response(
                ResponseMessage(
                    res_type=ResponseMessage.TYPE_TEXT,
                    content='cannot recognize this debug feature: {}'.format(msg)
                )
            )

        return res_event
