import os
import pandas as pd

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
)

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


"""
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
"""

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    word = event.message.text
    poke = pd.read_csv('./poke.csv', index_col=0)
    result = poke[poke['name'] == word]

    res = ImageSendMessage(
        original_content_url = result['type'][0],
        preview_image_url = result['type'][0]
    )
    res_message = f"ポケモン画像:{res}\n図鑑番号:{result['number'][0]}\n名前:{result['name'][0]}"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=res_message)
        #res
    )

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))