'''
Microsoft Computer Vision OCRを使います
登録してキーとかエンドポイントとか取得してください
'''
import requests

def getDoc(image_data):

	subscription_key = '[取得したサブスクリプションキーを記載してください]'
	endpoint = '[作成したエンドポイントURLを記載してください]'
	ocr_url = endpoint + "vision/v2.1/ocr"

	headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
	params = {'language': 'unk', 'detectOrientation': 'true'}
	response = requests.post(ocr_url, headers=headers, params=params, data = image_data)
	response.raise_for_status()
	analysis = response.json()

	line_infos = [region["lines"] for region in analysis["regions"]]
	result = ""
	for line in line_infos:
		for word_metadata in line:
			for word_info in word_metadata["words"]:
				result = result + " " + word_info["text"] 
	return result
