from unittest import TestCase

from core.model.situation.echo import EchoSitu

echo = EchoSitu()

class TestEchoSitu(TestCase):

    def test_contains(self):
        self.assertTrue("說 你好" in echo)
        self.assertTrue("重複 hi" in echo)
        self.assertTrue("重複" in echo)

    def test_get_response(self):
        self.assertEqual(echo.get_response("說 你好"), "你好")
        self.assertEqual(echo.get_response("重複 hi"), "hi")
        self.assertEqual(echo.get_response("說 你好 我是豬"), "你好 我是豬")
        self.assertEqual(echo.get_response("說"), EchoSitu.DEFAULT_RESPONSE)
        self.assertEqual(echo.get_response("說    "), EchoSitu.DEFAULT_RESPONSE)
