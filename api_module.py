import requests

CLIENT_ID = "시크릿 키"
CLIENT_SECRET = "시크릿 키"
headers = {"X-Naver-Client-Id":CLIENT_ID,"X-Naver-Client-Secret":CLIENT_SECRET}

def translate(text, en_to_ko=True):

    data = {"source":"en", "target":"ko", "text":text} if en_to_ko else {"source":"ko", "target":"en", "text":text}

    response = requests.post("https://openapi.naver.com/v1/papago/n2mt", headers=headers, data=data)

    translated_text = response.json()['message']['result']['translatedText']

    return translated_text