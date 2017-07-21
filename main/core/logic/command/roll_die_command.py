import random

import emoji

from main.core.logic.command.name_command_adapter import NameCommandAdapter
from main.core.model.event.input_event import InputEvent
from main.core.model.event.multi_response_event import ResponseMessage
from main.core.model.event.response_event import SingleResponseEvent
from main.utils import cht_utils


class RollDiceCommandAdpater(NameCommandAdapter):
    """
    Command template: 機器人 擲骰子 [幾個 幾面骰]
    Command template: 機器人 擲骰子 [幾面骰]
    return          : 擲了{幾}個{幾}面骰 --> [骰子結果]+[骰子結果]+[骰子結果] = 總和 
    """
    keywords = ['擲骰子', 'roll']

    def can_process(self, input_event: InputEvent) -> bool:
        if not super().can_process(input_event):
            return False

        message_text = super().filter_out_names(input_event.content).lstrip()
        message_text = cht_utils.strip_leading_ch_symbol(message_text)
        return any(message_text.startswith(kw) for kw in self.keywords)

    def process(self, input_event: InputEvent) -> SingleResponseEvent:
        message_text = super().filter_out_names(input_event.content).strip()
        message_text = cht_utils.strip_leading_ch_symbol(message_text)

        for kw in self.keywords:
            if message_text.startswith(kw):
                print('find kw :', kw)
                message_text = message_text[len(kw):]
                print('message_text = (' + message_text + ')')

        message_text = message_text.lstrip()

        args = message_text.split()
        die_face_max = 6
        die_count = 1

        result_message = '請問是怎樣的骰子呢？:confused:\n\n' \
                         '請對我說："機器人 擲骰子 [幾個 幾面骰]"，或是 "機器人 擲骰子 [幾面骰]"。\n\n' \
                         '[]中的資料可以不用輸入，預設是一個六面骰。:game_die:\n\n' \
                         'ex: 機器人 擲骰子 3 12'

        if len(args) == 1:
            if args[0].isdigit():
                die_face_max = int(args[0])
            else:
                die_face_max = 1
        elif len(args) == 2:
            if args[0].isdigit() and args[1].isdigit():
                die_count = int(args[0])
                die_face_max = int(args[1])
            else:
                die_count = 0

        roll_result = []
        if die_count > 300:
            result_message = '一次{}個？也太多骰子了吧～:anguished: \n重來重來，最多300個:game_die:'.format(die_count)
        else:
            for i in range(die_count):
                roll = random.randint(1, die_face_max)
                roll_result.append(roll)

        if len(roll_result) > 0:
            result_message = "擲了 {}個 {}面骰：\n\n".format(die_count, die_face_max)

        if len(roll_result) > 1:
            result_message += "總合：{}\n".format(sum(roll_result))
            result_message += "骰子結果："
            result_message += ", ".join(str(r) for r in roll_result)
        elif len(roll_result) == 1:
            result_message += "結果：{}\n".format(sum(roll_result))

        result_message = emoji.emojize(result_message, use_aliases=True)

        res_event = SingleResponseEvent(
            ResponseMessage.TYPE_TEXT,
            input_event,
            content=result_message)

        return res_event
