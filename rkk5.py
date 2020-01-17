# import libraries

import urllib, urllib2
import json
import requests


headers = {
        'pragma': 'no-cache',
        'referer': 'https://pkk5.rosreestr.ru/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        }


r = requests.get("http://pkk5.rosreestr.ru/api/features/1?text=65,210671+70,399301&tolerance=5", headers=headers).json()
for i in r['features']:
        print i['attrs']['address']


