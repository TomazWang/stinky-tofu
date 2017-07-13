import random

from linebot import LineBotApi
from linebot.models import MessageEvent

from core.msg_parser import UserMessage


def get_unknown_res():
    responses = [
        '我不清楚你在說什麼',
        '抱歉... 我聽不懂...'
    ]

    return random.choice(responses)


def get_introduce_res():
    responses = [
        '我是臭豆腐機器人，目前還在測試中，請多指教(moon grin)(moon grin)'
    ]

    return random.choice(responses)


def get_who_res(user_name: str):
    return "你是" + user_name + "啊～"


def response_to(user_msg: UserMessage, event: MessageEvent, line_bot_api: LineBotApi) -> str:
    """ 
    response_to generate suitable response for specific message. 
    """
    response_str = get_unknown_res()
    if user_msg.type is UserMessage.TYPE_WHO:
        user_profile = line_bot_api.get_profile(event.source.user_id)
        response_str = get_who_res(user_profile.display_name)
    elif user_msg.type is UserMessage.TYPE_INTRODUCE:
        response_str = get_introduce_res()

    return response_str
