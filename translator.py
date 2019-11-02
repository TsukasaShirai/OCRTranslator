'''
NICTの翻訳サービスを使います。
登録して各パラメータを取得してください
'''
import requests
from requests_oauthlib import OAuth1

#英語から日本語にするやつ
def translate(text):

	NAME = '[登録名を入力してください]'
	KEY = ''[提供されたKEYを入力してください]''
	SECRET = '[提供されたSECRETを入力してください]'
	URL = '[提供されたURLを入力してください]'

	consumer = OAuth1(KEY , SECRET)
	params = {
		'key': KEY,
		'name': NAME,
		'type': 'json',
		'split': 0,
		'text': text
	}

	response = requests.post(URL, data=params, auth=consumer)
	response.encoding = 'utf-8'
	json = response.json()
	
	return json['resultset']['result']['text']
