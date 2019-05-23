
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
				"text": "こんにちは、初めまして。\nライフシフト株式会社　コンサルティング事業部　サポートセンターです。",
				"buttons": ["こんにちは"]
			}
		],

		"Get Started": [
			{
				"method": "send_image",
				"image_url": "https://raw.githubusercontent.com/pomtaro/pic-garage/master/unDraw_sketch/welcome.png"
			},
			{
				"method": "send_quick_reply",
				"text": "こんにちは、初めまして。\nライフシフト株式会社　コンサルティング事業部　サポートセンターです。",
				"buttons": ["こんにちは"]
			}
		],

		"こんにちは": [
			{
				"method": "send_quick_reply",
				"text": "弊社の時間創出コンサルティングに関するお問い合わせですか？\n"
						"ITサービスの紹介に関するお問い合わせですか？",
				"buttons": ["コンサルティング", "ITサービス"]
			}
		],

		"コンサルティング": [
			{
				"method": "send_message",
				"text": "申し訳ありません、現在準備中です。"
			}
		],

		"ITサービス": [
			{
				"method": "send_quick_reply",
				"text": "お問い合わせありがとうございます。\n"
				        "ご興味のある分野をお選びください。",
				"buttons": ["情報共有", "勤怠管理", "資料作成", "助成金支援"]
			}
		],

		"情報共有": [
			{
				"method": "send_message",
				"text": "Slackをお試しください。"
			}
		],

		"勤怠管理": [
			{
				"method": "send_message",
				"text": "Smart kintAIをお試しください。"
			}
		],

		"資料作成": [
			{
				"method": "send_message",
				"text": "Beautiful.AIをお試しください。"
			}
		],

		"助成金支援": [
			{
				"method": "send_carousel_link",
				"titles": ["クラウドシエン"],
				"subtitles": ["助成金AIマッチング"],
				"image_urls": ["https://github.com/pomtaro/pic-garage/blob/master/consulting/cloud_sien.jpeg?raw=true"],
				"link_urls": ["https://crowdsien.com/"],
				"buttons_titles": [["Webサイトを見る"]]
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
				elif method == "send_carousel_link":
					print("send_carousel_link")
					titles = self.flow_dict[message_text][item_number]["titles"]
					subtitles = self.flow_dict[message_text][item_number]["subtitles"]
					image_urls = self.flow_dict[message_text][item_number]["image_urls"]
					link_urls = self.flow_dict[message_text][item_number]["link_urls"]
					print(link_urls)
					buttons_titles = self.flow_dict[message_text][item_number]["buttons_titles"]
					self.send_carousel_link(recipient_id, titles, subtitles, image_urls, link_urls, buttons_titles, access_token)
				elif method == "continue_chat":
					self.continue_chat(recipient_id, access_token)

		else:
			self.send_message_for_else(recipient_id, access_token)

	def generate_sorry(self):
		sorry_words = "大変申し訳ありません。\n" \
		              "ご回答は選択肢よりお願い致します。"

		return sorry_words

	def send_message_for_else(self, recipient_id, access_token):
		text = self.generate_sorry()
		self.send_message(recipient_id, text, access_token)

		text = "お手数をおかけ致しますが、最初からスタートします。"
		buttons = ["スタート"]
		self.send_quick_reply(recipient_id, text, buttons, access_token)

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

	def send_carousel_link(self, recipient_id, titles,  subtitles, image_urls, link_urls, buttons_titles, access_token):

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
					"type": "web_url",
					"url": link_urls[num],
					"title": button_title,
				}
				buttons.append(button_dict)

			carousel_dict = {
				"title": titles[num],
				"image_url": image_urls[num],
				"subtitle": subtitles[num],
				"default_action": {
					"type": "web_url",
					"url": link_urls[num],
					# "messenger_extensions": True,
					"webview_height_ratio": "tall",
					"fallback_url": "https://advisor.lifeshift.co.jp"
				},
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
