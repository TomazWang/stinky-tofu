from linebot.models import TextSendMessage

from app import line_bot_api


def reply(reply_token, message):
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=message))


def handle_msg(event):
    text = event.message.text

    if text == '我是誰':
        profile = line_bot_api.get_profile(event.source.user_id)
        name = profile.display_name
        id = profile.user_id
        reply_msg = "你是" + name + "啊～"
    else:
        # echo
        reply_msg = text

    reply(event.reply_token, reply_msg)
