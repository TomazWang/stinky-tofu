import random
from typing import List

from linebot import LineBotApi
from linebot.models import MessageEvent

from core.model.situation.abc_situation import Situation
from core.model.user_message import UserMessage


def get_unknown_res():
    responses = [
        '我不清楚你在說什麼',
        '抱歉... 我聽不懂...'
    ]

    return random.choice(responses)


def response_to(user_msg: UserMessage, situations: List[Situation]) -> str:
    """ 
    response_to generate suitable response for specific message. 
    """
    response_str = get_unknown_res()

    for situation in situations:
        if situation.get_message_type() == user_msg.type:
            return situation.get_response(user_msg.text)

    return response_str
