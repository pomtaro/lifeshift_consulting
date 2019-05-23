
import requests
import json
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Flow:
	
	flow_dict = {
        "スタート": [
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/welcome.png"
            },
            {
                "method": "send_quick_reply",
                "text": "こんにちは、初めまして。\n私と一緒にあなたの借金状況を見直してみましょう。",
                "buttons": ["こんにちは"]
            },
            {
                "method": "set_id_to_firestore"
            }
        ],

        "Get Started": [
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/welcome.png"
            },
            {
                "method": "send_quick_reply",
                "text": "こんにちは、初めまして。\n私と一緒にあなたの借金状況を見直してみましょう。",
                "buttons": ["こんにちは"]
            },
            {
                "method": "set_id_to_firestore"
            }

        ],

        "こんにちは": [
            {
                "method": "send_message",
                "text": "日本では実に多くの方が借金について悩んでいます。"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/debt.png"
            },
            {
                "method": "send_quick_reply",
                "text": "しかし、借金をうまく返していく方法もあります。\n私はそのお手伝いをします。具体的な流れを見てみましょう。",
                "buttons": ["具体的な流れを見る"]
            }
        ],

        "具体的な流れを見る": [
            {
                "method": "send_message",
                "text": "それでは、見ていきましょう。"
            },
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "1. チャット形式で会話が進みます。",
                    "2. あなたは選択肢を選ぶだけです。",
                    "3. あなたの借金状況を診断します。"
                ],
                "subtitles": [
                    "私が会話をリードします。安心してください。",
                    "リラックスして自分に当てはまる選択肢を選んでください。",
                    "借金状況とその解決方法をお伝えします。"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/explain1.png",
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/explain2.png",
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/explain3.png"
                ]
            },
            {
                "method": "send_quick_reply",
                "text": "私がリードしますので、大まかに理解できれば大丈夫です。",
                "buttons": ["わかりました"]
            }
        ],

        "わかりました": [
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                             "unDraw_sketch/Get%20started.png"
            },
            {
                "method": "send_quick_reply",
                "text": "さあ、始めましょう",
                "buttons": ["始める"]
            }
        ],

        "始める": [
            {
                "method": "send_message",
                "text": "リラックスしてください、質問は4つです。"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question1.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["生活費のため", "娯楽のため", "失職、退職", "病気", "ギャンブル"]
            }
        ],

        "生活費のため": [
            {
                "method": "set_debt_reason_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question2.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["1社", "2社", "3社以上"]
            }
        ],

        "娯楽のため": [
            {
                "method": "set_debt_reason_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question2.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["1社", "2社", "3社以上"]
            }
        ],

        "失職、退職": [
            {
                "method": "set_debt_reason_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question2.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["1社", "2社", "3社以上"]
            }
        ],

        "病気": [
            {
                "method": "set_debt_reason_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question2.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["1社", "2社", "3社以上"]
            }
        ],

        "ギャンブル": [
            {
                "method": "set_debt_reason_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question2.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["1社", "2社", "3社以上"]
            }
        ],

        "1社": [
            {
                "method": "set_debt_companies_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question3.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["0~100万", "100~500万", "500~1000万", "1000~2000万", "2000万以上"]
            }
        ],

        "2社": [
            {
                "method": "set_debt_companies_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question3.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["0~100万", "100~500万", "500~1000万", "1000~2000万", "2000万以上"]
            }

        ],

        "3社以上": [
            {
                "method": "set_debt_companies_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question3.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["0~100万", "100~500万", "500~1000万", "1000~2000万", "2000万以上"]
            }

        ],

        "0~100万": [
            {
                "method": "set_debt_prices_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question4.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "100~500万": [
            {
                "method": "set_debt_prices_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question4.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "500~1000万": [
            {
                "method": "set_debt_prices_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question4.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "1000~2000万": [
            {
                "method": "set_debt_prices_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question4.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "2000万以上": [
            {
                "method": "set_debt_prices_to_firestore"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question4.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "0~1万": [
            {
                "method": "set_pay_per_month_to_firestore"
            },
            {
                "method": "send_quick_reply",
                "text": "お疲れ様でした。質問は以上です。\n結果を見てみましょう。",
                "buttons": ["見てみる"]
            }
        ],

        "1~5万": [
            {
                "method": "set_pay_per_month_to_firestore"
            },
            {
                "method": "send_quick_reply",
                "text": "お疲れ様でした。質問は以上です。\n結果を見てみましょう。",
                "buttons": ["見てみる"]
            }
        ],

        "5~10万": [
            {
                "method": "set_pay_per_month_to_firestore"
            },
            {
                "method": "send_quick_reply",
                "text": "お疲れ様でした。質問は以上です。\n結果を見てみましょう。",
                "buttons": ["見てみる"]
            }
        ],

        "10万以上": [
            {
                "method": "set_pay_per_month_to_firestore"
            },
            {
                "method": "send_quick_reply",
                "text": "お疲れ様でした。質問は以上です。\n結果を見てみましょう。",
                "buttons": ["見てみる"]
            }
        ],

        "見てみる": [
            {
                "method": "decide_consolidation_image"
            },
            {
                "method": "decide_consolidation_comment"
            },
            {
                "method": "send_message",
                "text": "チェック結果はこちらです。"
            },
            {
                "method": "send_image",
                "image_url": "dummy_url"  # decide_consolidation_image内でurlを定義している
            },
            {
                "method": "send_message",
                "text": ""  # decide_consolidation_comment内でtextを定義している
            },
            {
                "method": "send_quick_reply",
                "text": "借金整理には大きく3つの方法があります。\n"
                        "あなたにオススメの整理方法と、その他の方法についても確認しましょう。",
                "buttons": ["確認する"]
            },
            {
                "method": "send_info_to_lawyers"
            }
        ],

        "確認する": [
            {
                "method": "decide_consolidation_recommendation"
            },
            {
                "method": "send_message",
                "text": "あなたにオススメの整理方法はこちらです。"
            },
            {
                "method": "send_carousel",
                "titles": [],  # decide_consolidation_recommendation内で定義
                "subtitles": [],  # decide_consolidation_recommendation内で定義
                "image_urls": [],  # decide_consolidation_recommendation内で定義
                "buttons_titles": [[]]  # decide_consolidation_recommendation内で定義
            }
        ],

        "任意整理を詳しく見る": [
            {
                "method": "send_message",
                "text": "任意整理は一番手軽な借金整理の方法です。"
            },
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "金利なしで残りの借金を返済します。",
                    "あなたが交渉する必要はありません。",
                    "すべてを整理する必要はありません。"
                ],
                "subtitles": [
                    "返済の負担を大きく軽減することができます。",
                    "仕事等で忙しくても安心してください。",
                    "選択はあなたの自由です。"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                    "unDraw_sketch/%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86info1.png",
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                    "unDraw_sketch/%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86info2.png",
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                    "unDraw_sketch/%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86info3.png"
                ]
            },
            {
                "method": "send_quick_reply",
                "text": "セルフチェックは以上です、お疲れ様でした。\n最後にアンケートに答えてもらえませんか？",
                "buttons": ["アンケートに答える"]
            }
        ],

        "個人再生を詳しく見る": [
            {
                "method": "send_message",
                "text": "個人再生は借金の圧縮が特徴です。"
            },
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "借金を1/5に圧縮します。",
                    "財産を残すことができます。",
                    "ストレスから解放されます。"
                ],
                "subtitles": [
                    "圧縮した借金なら返済できるかもしれません。",
                    "あなたの大事な財産を守ることができます。",
                    "様々な強制執行を止めることができます。"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                    "unDraw_sketch/%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9Finfo1.png",
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                    "unDraw_sketch/%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9Finfo2.png",
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                    "unDraw_sketch/%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9Finfo3.png"
                ]
            },
            {
                "method": "send_quick_reply",
                "text": "セルフチェックは以上です、お疲れ様でした。\n最後にアンケートに答えてもらえませんか？",
                "buttons": ["アンケートに答える"]
            }

        ],

        "自己破産を詳しく見る": [
            {
                "method": "send_message",
                "text": "自己破産は借金を全て無くせることが特徴です。"
            },
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "すべての借金を無くします。",
                    "ストレスから解放されます。",
                    "生活に最低現必要な財産は残すことができます。"
                ],
                "subtitles": [
                    "もう一度、やり直しましょう。",
                    "様々な強制執行を止めることができます。",
                    "すべてが無くなるわけではありません。安心してください。"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                    "unDraw_sketch/%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3info1.png",
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                    "unDraw_sketch/%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3info2.png",
                    "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                    "unDraw_sketch/%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3info3.png"
                ]
            },
            {
                "method": "send_quick_reply",
                "text": "セルフチェックは以上です、お疲れ様でした。\n最後にアンケートに答えてもらえませんか？",
                "buttons": ["アンケートに答える"]
            }

        ],

        "アンケートに答える": [
            {
                "method": "send_message",
                "text": "ありがとうございます。"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                             "unDraw_sketch/%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["Excellent", "Good", "Bad"]
            }
        ],

        "Excellent": [
            {
                "method": "record_impression"
            },
            {
                "method": "send_message",
                "text": "セルフチェックは以上で終わりです、お疲れ様です。"
            },
            {
                "method": "send_quick_reply",
                "text": "もう一度セルフチェックに戻ることができます。",
                "buttons": ["セルフチェックに戻る"]
            }
        ],

        "Good": [
            {
                "method": "record_impression"
            },
            {
                "method": "send_message",
                "text": "セルフチェックは以上で終わりです、お疲れ様です。"
            },
            {
                "method": "send_quick_reply",
                "text": "もう一度セルフチェックに戻ることができます。",
                "buttons": ["セルフチェックに戻る"]
            }
        ],

        "Bad": [
            {
                "method": "record_impression"
            },
            {
                "method": "send_message",
                "text": "セルフチェックは以上で終わりです、お疲れ様です。"
            },
            {
                "method": "send_quick_reply",
                "text": "もう一度セルフチェックに戻ることができます。",
                "buttons": ["セルフチェックに戻る"]
            }
        ],

        "セルフチェックに戻る": [
            {
                "method": "send_message",
                "text": "どこまでもサポートします。"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question1.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["生活費のため", "娯楽のため", "失職、退職", "病気", "ギャンブル"]
            }
        ],

        "セルフチェックに進む": [
            {
                "method": "send_message",
                "text": "さあ、始めましょう。"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/question1.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでください。",
                "buttons": ["生活費のため", "娯楽のため", "失職、退職", "病気", "ギャンブル"]
            }
        ],

        "続きから始める": [
            {
                "method": "continue_chat"
            }
        ],

        "登録": [
            {
                "method": "register_lawyer"
            },
            {
                "method": "send_message",
                "text": "登録ありがとうございます。\nこれよりご相談者の借金情報を順次送信させて頂きます。"
            }
        ]
    }

    def message_is(self, message_text):
        if message_text in self.flow_dict.keys():
            return True
        else:
            return False

    def read_item_numbers(self, message_text):  # 要素数を判定
        if self.message_is(message_text):
            item_numbers = len(self.flow_dict[message_text])
            return item_numbers
        else:
            return False

    def read_method(self, message_text, item_number):  # methodを判定する
        if self.message_is(message_text):
            method = self.flow_dict[message_text][item_number]["method"]
            return method
        else:
            return False

    def execute_method(self, recipient_id, message_text, access_token):
        if self.message_is(message_text):

            item_numbers = self.read_item_numbers(message_text)

            for item_number in range(item_numbers):
                method = self.read_method(message_text, item_number)

                if method == "send_message":
                    text = self.flow_dict[message_text][item_number]["text"]
                    self.send_message(recipient_id, text, access_token)
                elif method == "send_quick_reply":
                    text = self.flow_dict[message_text][item_number]["text"]
                    buttons = self.flow_dict[message_text][item_number]["buttons"]
                    self.send_quick_reply(recipient_id, text, buttons, access_token)
                elif method == "send_image":
                    image_url = self.flow_dict[message_text][item_number]["image_url"]
                    self.send_image(recipient_id, image_url, access_token)
                elif method == "send_carousel":
                    titles = self.flow_dict[message_text][item_number]["titles"]
                    subtitles = self.flow_dict[message_text][item_number]["subtitles"]
                    image_urls = self.flow_dict[message_text][item_number]["image_urls"]
                    buttons_titles = self.flow_dict[message_text][item_number]["buttons_titles"]
                    self.send_carousel(recipient_id, titles, subtitles, image_urls, buttons_titles, access_token)
                elif method == "send_carousel_buttonless":
                    titles = self.flow_dict[message_text][item_number]["titles"]
                    subtitles = self.flow_dict[message_text][item_number]["subtitles"]
                    image_urls = self.flow_dict[message_text][item_number]["image_urls"]
                    self.send_carousel_buttonless(recipient_id, titles, subtitles, image_urls, access_token)
                elif method == "record_debt_companies":
                    self.record_debt_companies(message_text)
                elif method == "record_debt_prices":
                    self.record_debt_prices(message_text)
                elif method == "record_pay_per_month":
                    self.record_pay_per_month(message_text)
                elif method == "decide_consolidation_image":
                    self.decide_consolidation_image(recipient_id)
                elif method == "decide_consolidation_comment":
                    self.decide_consolidation_comment(recipient_id)
                elif method == "decide_consolidation_recommendation":
                    self.decide_consolidation_recommendation(recipient_id)
                elif method == "set_id_to_firestore":
                    self.set_id_to_firestore(recipient_id)
                elif method == "set_debt_reason_to_firestore":
                    self.set_debt_reason_to_firestore(recipient_id, message_text)
                elif method == "set_debt_companies_to_firestore":
                    self.set_debt_companies_to_firestore(recipient_id, message_text)
                elif method == "set_debt_prices_to_firestore":
                    self.set_debt_prices_to_firestore(recipient_id, message_text)
                elif method == "set_pay_per_month_to_firestore":
                    self.set_pay_per_month_to_firestore(recipient_id, message_text)
                elif method == "register_lawyer":
                    self.register_lawyer(recipient_id)
                elif method == "send_info_to_lawyers":
                    self.send_info_to_lawyers(recipient_id, access_token)
                elif method == "continue_chat":
                    self.continue_chat(recipient_id, access_token)

            self.record_step(recipient_id, message_text)
            if not message_text == "続きから始める":
                self.set_user_most_recent_word_to_firestore(recipient_id, message_text)

        else:
            self.send_message_for_else(recipient_id, access_token)

    def generate_random_sorry(self):
        sorry_words = [
            "すみません、自由なメッセージには対応してないんです。",
            "すみません、選択肢と異なります。",
            "間違えてしまったのですね、誰でもあることです。"
        ]

        return random.choice(sorry_words)

    def send_message_for_else(self, recipient_id, access_token):
        text = self.generate_random_sorry()
        self.send_message(recipient_id, text, access_token)

        text = "続きから始めますか？\nそれともセルフチェックに進みますか？"
        buttons = ["続きから始める", "セルフチェックに進む"]
        self.send_quick_reply(recipient_id, text, buttons, access_token)

    def continue_chat(self, recipient_id, access_token):
        most_recent_word = self.get_user_most_recent_word(recipient_id)
        self.execute_method(recipient_id, most_recent_word, access_token)

    def send_message(self, recipient_id, text, access_token):

        params = {
            "access_token": access_token
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": text
            }
        })

        requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

    def send_quick_reply(self, recipient_id, text, buttons, access_token):

        params = {
            "access_token": access_token
        }
        headers = {
            "Content-Type": "application/json"
        }

        quick_replies = []

        for button in buttons:
            quick_dict = {
                "content_type": "text",
                "title": button,
                "payload": "payload: {}".format(button)
            }
            quick_replies.append(quick_dict)

        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": text,
                "quick_replies": quick_replies
            }
        })

        requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

    def send_image(self, recipient_id, image_url, access_token):

        params = {
            "access_token": access_token
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "attachment": {
                    "type": "image",
                    "payload": {
                        "url": image_url,
                        "is_reusable": 'true'
                    }
                }
            }
        })

        requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

    def send_carousel(self, recipient_id, titles,  subtitles, image_urls, buttons_titles, access_token):

        params = {
            "access_token": access_token
        }
        headers = {
            "Content-Type": "application/json"
        }

        elements = []
        carousel_number = len(titles)

        for num in range(carousel_number):

            buttons = []

            for button_title in buttons_titles[num]:
                button_dict = {
                    "type": "postback",
                    "title": button_title,
                    "payload": "payload : " + button_title
                }
                buttons.append(button_dict)

            carousel_dict = {
                "title": titles[num],
                "image_url": image_urls[num],
                "subtitle": subtitles[num],
                "buttons": buttons
            }
            elements.append(carousel_dict)

        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": elements
                    }
                }
            }
        })

        requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

    def send_carousel_buttonless(self, recipient_id, titles, subtitles, image_urls, access_token):

        params = {
            "access_token": access_token
        }
        headers = {
            "Content-Type": "application/json"
        }

        elements = []
        carousel_number = len(titles)

        for num in range(carousel_number):
            carousel_dict = {
                "title": titles[num],
                "image_url": image_urls[num],
                "subtitle": subtitles[num]
            }
            elements.append(carousel_dict)

        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": elements
                    }
                }
            }
        })

        requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

    def get_user_debt_info(self, recipient_id):
        doc_ref = self.db.collection(u"users").document(recipient_id)
        info_dict = dict(doc_ref.get().to_dict())

        try:
            debt_companies = info_dict["debt_companies"]
            debt_prices = info_dict["debt_prices"]
            pay_per_month = info_dict["pay_per_month"]

            return debt_companies, debt_prices, pay_per_month
        except:
            return "1社", "0~100万", "0~1万"

    def decide_consolidation_group(self, recipient_id):

        debt_companies, debt_prices, pay_per_month = self.get_user_debt_info(recipient_id)

        if debt_prices == "0~100万":
            if pay_per_month == "0~1万":
                return "individual rehabilitation"
            elif pay_per_month == "1~5万" or pay_per_month == "5~10万" or pay_per_month == "10万以上":
                return "voluntary liquidation"
        elif debt_prices == "100~500万":
            if pay_per_month == "0~1万":
                return "personal bankruptcy"
            elif pay_per_month == "1~5万":
                return "individual rehabilitation"
            elif pay_per_month == "5~10万" or pay_per_month == "10万以上":
                return "voluntary liquidation"
        elif debt_prices == "500~1000万":
            if pay_per_month == "0~1万":
                return "personal bankruptcy"
            elif pay_per_month == "1~5万" or pay_per_month == "5~10万":
                return "individual rehabilitation"
            elif pay_per_month == "10万以上":
                return "voluntary liquidation"
        elif debt_prices == "1000~2000万":
            if pay_per_month == "0~1万" or pay_per_month == "1~5万":
                return "personal bankruptcy"
            elif pay_per_month == "5~10万" or pay_per_month == "10万以上":
                return "individual rehabilitation"
        elif debt_prices == "2000万以上":
            if pay_per_month == "0~1万" or pay_per_month == "1~5万" or pay_per_month == "5~10万":
                return "personal bankruptcy"
            elif pay_per_month == "10万以上":
                return "individual rehabilitation"

    def decide_consolidation_image(self, recipient_id):
        consolidation_group = self.decide_consolidation_group(recipient_id)

        urls_dict = {
            "voluntary liquidation": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                                     "unDraw_sketch/debt_danger11.png",
            "individual rehabilitation": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                                         "unDraw_sketch/debt_danger21.png",
            "personal bankruptcy": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                                   "unDraw_sketch/debt_danger31.png"
        }

        if consolidation_group == "voluntary liquidation":
            self.flow_dict["見てみる"][3]["image_url"] = urls_dict["voluntary liquidation"]
        elif consolidation_group == "individual rehabilitation":
            self.flow_dict["見てみる"][3]["image_url"] = urls_dict["individual rehabilitation"]
        elif consolidation_group == "personal bankruptcy":
            self.flow_dict["見てみる"][3]["image_url"] = urls_dict["personal bankruptcy"]

    def decide_consolidation_comment(self, recipient_id):
        consolidation_group = self.decide_consolidation_group(recipient_id)

        comments_dict = {
            "voluntary liquidation": "あなたの借金ヤバイ度は60%です。\n"
                                     "まだ間に合います。早めに借金整理を行う必要があります。",
            "individual rehabilitation": "あなたの借金ヤバイ度は80％です。\n"
                                         "まだ手段はあります。早めに行動しましょう。",
            "personal bankruptcy": "あなたの借金ヤバイ度は100％です。\n"
                                   "いますぐ行動しましょう。助けてくれる専門家がいます。"
        }

        if consolidation_group == "voluntary liquidation":
            self.flow_dict["見てみる"][4]["text"] = comments_dict["voluntary liquidation"]
        elif consolidation_group == "individual rehabilitation":
            self.flow_dict["見てみる"][4]["text"] = comments_dict["individual rehabilitation"]
        elif consolidation_group == "personal bankruptcy":
            self.flow_dict["見てみる"][4]["text"] = comments_dict["personal bankruptcy"]

    def decide_consolidation_recommendation(self, recipient_id):
        consolidation_group = self.decide_consolidation_group(recipient_id)

        urls_dict = {
            "voluntary liquidation_recommended": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                                                 "unDraw_sketch/%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86.png",
            "individual rehabilitation_recommended": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                                                     "unDraw_sketch/%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9F.png",
            "personal bankruptcy_recommended": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                                               "unDraw_sketch/%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3.png",
            "voluntary liquidation_other": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                                           "unDraw_sketch/%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86_other.png",
            "individual rehabilitation_other": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                                               "unDraw_sketch/%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9F_other.png",
            "personal bankruptcy_other": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/"
                                         "unDraw_sketch/%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3_other.png"
        }

        if consolidation_group == "voluntary liquidation":
            self.flow_dict["確認する"][2]["titles"] = ["任意整理",
                                                   "個人再生",
                                                   "自己破産"]
            self.flow_dict["確認する"][2]["subtitles"] = ["任意整理は最小限のリスクで借金の負担を減らす方法です。",
                                                      "個人再生は財産を残しながら借金を大きく減らす方法です。",
                                                      "自己破産は借金をすべて無くす方法です。"]
            self.flow_dict["確認する"][2]["image_urls"] = [urls_dict["voluntary liquidation_recommended"],
                                                       urls_dict["individual rehabilitation_other"],
                                                       urls_dict["personal bankruptcy_other"]]
            self.flow_dict["確認する"][2]["buttons_titles"] = [["任意整理を詳しく見る"],
                                                           ["個人再生を詳しく見る"],
                                                           ["自己破産を詳しく見る"]]
        elif consolidation_group == "individual rehabilitation":
            self.flow_dict["確認する"][2]["titles"] = ["個人再生",
                                                   "任意整理",
                                                   "自己破産"]
            self.flow_dict["確認する"][2]["subtitles"] = ["個人再生は財産を残しながら借金を大きく減らす方法です。",
                                                      "任意整理は最小限のリスクで借金の負担を減らす方法です。",
                                                      "自己破産は借金をすべて無くす方法です。"]
            self.flow_dict["確認する"][2]["image_urls"] = [urls_dict["individual rehabilitation_recommended"],
                                                       urls_dict["voluntary liquidation_other"],
                                                       urls_dict["personal bankruptcy_other"]]
            self.flow_dict["確認する"][2]["buttons_titles"] = [["個人再生を詳しく見る"],
                                                           ["任意整理を詳しく見る"],
                                                           ["自己破産を詳しく見る"]]
        elif consolidation_group == "personal bankruptcy":
            self.flow_dict["確認する"][2]["titles"] = ["自己破産",
                                                   "任意整理",
                                                   "個人再生"]
            self.flow_dict["確認する"][2]["subtitles"] = ["自己破産は借金をすべて無くす方法です。",
                                                      "任意整理は最小限のリスクで借金の負担を減らす方法です。",
                                                      "個人再生は財産を残しながら借金を大きく減らす方法です。"]
            self.flow_dict["確認する"][2]["image_urls"] = [urls_dict["personal bankruptcy_recommended"],
                                                       urls_dict["voluntary liquidation_other"],
                                                       urls_dict["individual rehabilitation_other"]]
            self.flow_dict["確認する"][2]["buttons_titles"] = [["自己破産を詳しく見る"],
                                                           ["任意整理を詳しく見る"],
                                                           ["個人再生を詳しく見る"]]

    def set_id_to_firestore(self, recipient_id):

        data = {
            u"id": recipient_id,
            u"first_timestamp": firestore.SERVER_TIMESTAMP
        }
        try:
            self.db.collection(u"users").document(recipient_id).update(data)
        except:
            self.db.collection(u"users").document(recipient_id).set(data)

    def set_debt_reason_to_firestore(self, recipient_id, message_text):

        data = {
            u"debt_reason": message_text
        }

        try:
            self.db.collection(u"users").document(recipient_id).update(data)
        except:
            self.db.collection(u"users").document(recipient_id).set(data)

    def set_debt_companies_to_firestore(self, recipient_id, message_text):

        data = {
            u"debt_companies": message_text
        }

        try:
            self.db.collection(u"users").document(recipient_id).update(data)
        except:
            self.db.collection(u"users").document(recipient_id).set(data)

    def set_debt_prices_to_firestore(self, recipient_id, message_text):

        data = {
            u"debt_prices": message_text
        }
        try:
            self.db.collection(u"users").document(recipient_id).update(data)
        except:
            self.db.collection(u"users").document(recipient_id).set(data)

    def set_pay_per_month_to_firestore(self, recipient_id, message_text):

        data = {
            u"pay_per_month": message_text
        }
        try:
            self.db.collection(u"users").document(recipient_id).update(data)
        except:
            self.db.collection(u"users").document(recipient_id).set(data)

    def record_step(self, recipient_id, message_text):

        data_update = {
            u"words." + message_text: u"done"
        }

        data_set = {
            u"words": {
                message_text: u"done"
            }
        }

        try:
            self.db.collection(u"users").document(recipient_id).update(data_update)
        except:
            self.db.collection(u"users").document(recipient_id).set(data_set)

    def register_lawyer(self, recipient_id):

        data = {
            "id." + recipient_id: recipient_id
        }

        try:
            self.db.collection("lawyers").document("ID").update(data)
        except:
            self.db.collection("lawyers").document("ID").set(data)

    def get_lawyers_id(self):

        doc_ref = self.db.collection(u"lawyers").document(u"ID")
        id_dict = dict(doc_ref.get().to_dict())

        ids = []
        for id in id_dict.values():
            ids.append(id)

        return ids

    def send_info_to_lawyers(self, recipient_id, access_token):

        debt_companies, debt_prices, pay_per_month = self.get_user_debt_info(recipient_id)
        print(debt_companies, debt_prices, pay_per_month)
        ids = self.get_lawyers_id()
        print(ids)

        text = "チャットボット利用者の情報が届きました。"
        info_text = "借り入れ社数、{}\n" \
                    "借り入れ総額、{}\n" \
                    "毎月返済額、{}".format(debt_companies, debt_prices, pay_per_month)
        for lawyer_id in ids:
            self.send_message(lawyer_id, text, access_token)
            self.send_message(lawyer_id, info_text, access_token)

    def get_user_last_word(self, recipient_id):
        doc_ref = self.db.collection(u"users").document(recipient_id)
        doc_dict = dict(doc_ref.get().to_dict())

        last_word = ""

        for key in list(self.flow_dict.keys()):
            if key == 'スタート' or key == 'Get Started':
                pass
            else:
                if key in list(doc_dict['words']):
                    last_word = key
                else:
                    pass
        return last_word

    def set_user_most_recent_word_to_firestore(self, recipient_id, message_text):

        data = {
            u"last_word": message_text
        }
        try:
            self.db.collection(u"users").document(recipient_id).update(data)
        except:
            self.db.collection(u"users").document(recipient_id).set(data)

    def get_user_most_recent_word(self, recipient_id):
        try:
            doc_ref = self.db.collection(u"users").document(recipient_id)
            doc_dict = dict(doc_ref.get().to_dict())

            return doc_dict["last_word"]
        except:
            return "スタート"
