import random
from typing import List

from core.model.user_message import UserMessage

from app.core.model.situation import Situation


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
        if situation.get_message_action() == user_msg.action:
            return situation.get_response(user_msg.context)

    return response_str
