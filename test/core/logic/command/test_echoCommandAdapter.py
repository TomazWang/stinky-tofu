import unittest

from main.core.logic.command.echo_command_adapter import EchoCommandAdapter
from main.core.model.event.input_event import InputEvent


class TestEchoCommandAdapter(unittest.TestCase):
    expect_dict = {
        '機器人，說你好': (True, '你好'),
        '機器人說你好': (True, '你好'),
        '機器人 說 你好': (True, '你好'),
        '機器人，說說說': (True, '說說'),
        '機器人說不要說你好': (True, '不要說你好'),
        '機器人 說 說說說說說說你愛我': (True, '說說說說說說你愛我')
    }

    echo_adapter = EchoCommandAdapter('機器人')

    def test_can_process(self):
        for statement in self.expect_dict.keys():
            input_event = InputEvent(InputEvent.TYPE_TEXT, source_content=statement)
            self.assertEqual(
                self.echo_adapter.can_process(input_event),
                self.expect_dict[statement][0]
            )

    def test_process(self):
        for statement in self.expect_dict.keys():
            print('testing ', statement, ':')
            input_event = InputEvent(InputEvent.TYPE_TEXT, source_content=statement)
            res_event = self.echo_adapter.process(input_event)

            self.assertEqual(res_event.content, self.expect_dict[statement][1])


if __name__ == '__main__':
    unittest.main()
