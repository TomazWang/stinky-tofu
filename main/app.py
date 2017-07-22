import logging
import sys

from flask import Flask, abort, request
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage)

from main.core.command_bot import LineCommandBot
from main.utils import config_loader

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

config_data = config_loader.load_config()
CHANNEL_ACCESS_TOKEN = config_data.channel_access_token
CHANNEL_SECRET = config_data.channel_secret

if CHANNEL_SECRET is None:
    logging.warning('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if CHANNEL_ACCESS_TOKEN is None:
    logging.warning('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


command_bot = LineCommandBot(line_bot_api)

@app.route('/')
def home():
    return 'Hello tomazium bot.'
    # return CHANNEL_ACCESS_TOKEN + "\n" + CHANNEL_SECRET


@app.route("/bot/stinky/info")
def bot_info_stinky():
    return "This page is not complete."


@app.route("/bot/stinky/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)
    logging.info('main >> callback: Request body = {}'.format(body))

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text="機器人維修中... "))
    command_bot.handle_message_event(event)


if __name__ == "__main__":
    app.run()
