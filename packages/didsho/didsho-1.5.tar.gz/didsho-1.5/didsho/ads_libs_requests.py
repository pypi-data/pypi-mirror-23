# -*- coding: utf-8 -*-

import requests
import json


class Didsho:

    def __init__(self, botid, bot_token):
        self.apiUrl = "http://didsho.ir/getAdvertisement"
        self.botId = botid
        self.sort = 1
        self.keyboard = {"inline_keyboard": [[{"text": "شبکه تبلیغاتی دیدشو 💰🎯", "url": "https://t.me/didshobot"}]]}
        self.token = bot_token

    def send_ads(self, chat_id):
        url = requests.get("{0}/?bot_id={1}&sort={2}".format(self.apiUrl, self.botId, self.sort))
        data = url.json()

        media = str.split(str(data['media']), ",")
        text = "{0}\n{1}".format(data['text'], data['link'])

        if media[0] == 'text':
            result = requests.get("https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}&reply_markup={3}".format(self.token, chat_id, text, json.dumps(self.keyboard)))
        else:
            result = requests.get(
                "https://api.telegram.org/bot{0}/sendPhoto?chat_id={1}&photo={2}&caption={3}&reply_markup={4}".format(self.token, chat_id, media[1], text, json.dumps(self.keyboard)))

        print(result.json())

        return data['id']


