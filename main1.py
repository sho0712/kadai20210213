"""大沼アプリ"""

import json
import os

import random

# import gmail_login

from dotenv import load_dotenv

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, ImageMessage, TextSendMessage, ImageSendMessage, FlexSendMessage, StickerSendMessage)

load_dotenv()

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route('/')
def index():
    return 'You call index()'


@app.route("/push_sample")
def push_sample():
    """プッシュメッセージを送る"""
    user_id = os.environ["USER_ID"]
    line_bot_api.push_message(user_id, TextSendMessage(text="Hello World!"))

    return "OK"


@app.route("/callback", methods=["POST"])
def callback():
    """Messaging APIからの呼び出し関数"""
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    with open('json/face_scale.json') as f:
        face_scale = json.load(f)
    with open('json/syousai_message.json') as f:
        syousai_message = json.load(f)

    if event.message.text == "発熱":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'脳炎・髄膜炎：\n'
                                  f'筋炎・横紋筋融解症：\n'
                                  f'間質性肺疾患：\n'
                                  f'腎機能障害：\n'
                                  f'重度の皮膚障害：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "体重減":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'甲状腺中毒症：\n'
                                  f'副腎機能障害：\n'
                                  f'1型糖尿病：\n'
                                  f'筋炎・横紋筋融解症：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )


    elif event.message.text == "息苦しい":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'心筋炎：\n'
                                  f'間質性肺疾患：\n'
                                  f'腎機能障害：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "吐き気":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'副腎機能障害：\n'
                                  f'1型糖尿病：\n'
                                  f'膵炎：\n'
                                  f'脳炎・髄膜炎：\n'
                                  f'大腸炎・重度の下痢：\n'
                                  f'肝機能障害・肝炎：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "だるい":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'甲状腺機能低下症：\n'
                                  f'副腎機能障害：\n'
                                  f'下垂体機能障害：\n'
                                  f'1型糖尿病：\n'
                                  f'心筋炎：\n'
                                  f'大腸炎・重度の下痢：\n'
                                  f'腎機能障害：\n'
                                  f'肝機能障害・肝炎：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "その他":
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='その他', contents=syousai_message)
        )
    elif event.message.text == "体調は普通":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'このような副作用が疑われます。\n'
                                 f'脳炎:\n'
                                 f'https://pat.tecentriq.jp/lng/snd/sef/'))
    elif event.message.text == "ものが二重にみえる":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'重症筋無力症：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )

    elif event.message.text == "目がかすむ":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'ぶどう膜炎：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "口がかわく":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'1型糖尿病：\n'
                                  f'大腸炎・重度の下痢：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "手足に力がはいらない":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'筋炎・横紋筋融解症：\n'
                                  f'重症筋無力症：\n'
                                  f'神経障害：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "手足がしびれる":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'神経障害：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "便に血がまじっている":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'大腸炎・重度の下痢：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "げり":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'甲状腺中毒症：\n'
                                  f'副腎機能障害：\n'
                                  f'血球貪食症候群：\n'
                                  f'大腸炎・重度の下痢：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "べんぴ":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'甲状腺機能低下症：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "体重減":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'甲状腺中毒症：\n'
                                  f'副腎機能障害：\n'
                                  f'1型糖尿病：\n'
                                  f'筋炎・横紋筋融解症：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "からだがむくむ":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'甲状腺機能低下症：\n'
                                  f'腎機能障害：\n'
                                  f'心筋炎：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "ひしん・ほっしん":
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=f'このような副作用が疑われます。\n'
                                  f'血球貪食症候群：\n'
                                  f'腎機能障害：\n'
                                  f'肝機能障害・肝炎：\n'
                                  f'重度の皮膚障害：\n'
                                  f'https://pat.tecentriq.jp/lng/fst/sef/'),
             TextSendMessage(text=f'『{event.message.text}』はどのくらいつらいですか？'),
             FlexSendMessage(alt_text='息苦しい', contents=face_scale)]
        )
    elif event.message.text == "つらくない":
        omikuji_message = ["体調が少しでも変化しましたら、医療機関もしくはご家族へ連絡をしてください。"]
        result = random.choice(omikuji_message)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'{result}'))
    elif event.message.text == "すこしつらい" or "つらい" or "とてもつらい" or "ひじょうにつらい":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'かかりつけの医療機関に連絡をしてください'))
        gmail_login.gmail_send(event.message.text)



    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'体調はいかがですか？左下『　≡　』を押して、今日の体調を報告してください'))


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


"""
毎日決まった時間に『今日の体調はいかがですか？』

つらくない以外はアラートでメールを病院（今回は大沼のメールへ送信）

つらくないの場合は、名言で返す
"""
