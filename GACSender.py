import requests,json

class send():
    def __init__(self, pnum):
        resp = requests.post('https://api.line.me/v2/bot/message/reply/profiles/register', data={'phoneNumber': pnum,'countryCode': 'TH','name': 'pratannaimjoi','email': 'pratannaimjoi@gmail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Mozilla / 5.0 ( Linux ; Android 5.1 . 1 ; Nexus 5 รูปร่าง/ LMY48B ; WV ) AppleWebKit / 537.36 ( KHTML , เหมือนตุ๊กแก) เวอร์ชัน/ 4.0 Chrome / 43.0 2357.65 Mobile Safari / 537.36'})
        print(resp.status_code)
        if resp.status_code == 200:
            self.responseNum = 0
        elif resp.status_code == 429:
            self.responseNum = 1
        else:
            self.responseNum = 2
