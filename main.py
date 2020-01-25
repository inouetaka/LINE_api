import os
import sqlite3


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
    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    sql = 'SELECT * FROM pokes WHERE name = (?)'
    run = (word)
    c.execute(sql, run)
    result = c.fetchone()


    conn.close()

    res = ImageSendMessage(
        original_content_url = f"{'https://' + result[0][2]}",
        preview_image_url = f"{'https://' + result[0][2]}"
    )
    res_message = f"図鑑番号:{result[0][0]}\n名前:{result[0][1]}"

    line_bot_api.reply_message(
        event.reply_token,
        [res, TextSendMessage(text=res_message)]
    )

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))