"""
情報をFirebaseに格納する
情報：借り入れ社数、借り入れ総額、毎月返済額、ユーザID、各step
弁護士登録
弁護士への自動送信
"""

import os
import sys
import json
import time
import requests
from flask import Flask, request
from datetime import datetime
from Flow import Flow
from Get_started import Getstarted

app = Flask(__name__)

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
VERIFY_TOKEN = os.environ["VERIFY_TOKEN"]

flow = Flow()

getstarted = Getstarted()
getstarted.send_get_started(ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    data = request.get_json()
    print('***** post data *****')
    print(data)

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):

                    sender_id = messaging_event["sender"]["id"]

                    if messaging_event["message"].get("text"):
                        message_text = messaging_event["message"]["text"]

                        send_typing_on(sender_id)

                        flow.execute_method(sender_id, message_text, ACCESS_TOKEN)

                    else:
                        flow.execute_method(sender_id, "error", ACCESS_TOKEN)

                if messaging_event.get("delivery"):
                    pass

                if messaging_event.get("optin"):
                    pass

                if messaging_event.get("postback"):

                    sender_id = messaging_event["sender"]["id"]
                    message_text = messaging_event["postback"]["title"]
                    return_id = messaging_event["postback"]["payload"]

                    send_typing_on(sender_id)

                    flow.execute_method(sender_id, message_text, ACCESS_TOKEN)

    return "ok", 200


def send_typing_on(recipient_id):
    params = {
        "access_token": ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "sender_action": "typing_on"
    })

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    time.sleep(0.5)


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
