import emoji

from main.core.logic.command.name_command_adapter import NameCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.response_event import ResponseEvent


class IntroduceCommandAdapter(NameCommandAdapter):
    keywords = ['你是誰', '自我介紹']

    def can_process(self, input_event: InputEvent) -> bool:
        if not super().can_process(input_event):
            return False

        message_text = super().filter_out_names(input_event.content)
        return any(message_text.startswith(kw) for kw in self.keywords)

    def process(self, input_event: InputEvent) -> ResponseEvent:
        content = emoji.emojize('我是臭豆腐機器人，目前還在測試中，請多指教 :smile::thumbsup: \n', use_aliases=True)
        res_event = ResponseEvent(ResponseEvent.TYPE_MESSAGE, input_event, content=content)
        return res_event
