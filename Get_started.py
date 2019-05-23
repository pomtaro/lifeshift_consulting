
import requests
import json

class Getstarted():

    def send_get_started(self, access_token):
        params = {
            "access_token": access_token
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "get_started": {
                "payload": "Welcome!"
            },
            "greeting": [
                {
                    "locale": "default",
                    "text": "ライフシフト株式会社　コンサルティング事業部\n"
                            "自動応答チャットボットです。\n"
                            "コンサルティングに関するご質問がございましたら、お気軽にご連絡下さい。\n"
                            "ITサービスのご紹介も行なっております。"
                }
            ]
        })

        requests.post("https://graph.facebook.com/v2.6/me/messenger_profile", params=params, headers=headers, data=data)
