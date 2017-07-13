from unittest import TestCase

from core.model.situation.echo import EchoSitu

echo = EchoSitu()

class TestEchoSitu(TestCase):

    def test_contains(self):
        self.assertTrue("說 你好" in echo)
        self.assertTrue("重複 hi" in echo)
        self.assertTrue("重複" in echo)

    def test_get_response(self):
        if "說 你好" in echo:
            self.assertEqual(echo.get_response(), "你好")

        if "重複 hi" in echo:
            self.assertEqual(echo.get_response(), "hi")

        if "說 你好 我是豬" in echo:
            self.assertEqual(echo.get_response(), "你好 我是豬")

        if "說" in echo:
            self.assertEqual(echo.get_response(), EchoSitu.DEFAULT_RESPONSE)

        if "說    " in echo:
            self.assertEqual(echo.get_response(), EchoSitu.DEFAULT_RESPONSE)
