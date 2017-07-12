from linebot.models import TextSendMessage


class Brain:
    def __init__(self, line_bot_api):
        self.line_bot_api = line_bot_api

    def reply(self, reply_token, message):
        self.line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text=message))

    def handle_msg(self, event):
        text = event.message.text

        if text == '我是誰':
            profile = self.line_bot_api.get_profile(event.source.user_id)
            name = profile.display_name
            id = profile.user_id
            reply_msg = "你是" + name + "啊～"
        else:
            # echo
            reply_msg = text

        self.reply(event.reply_token, reply_msg)
