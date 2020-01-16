import requests

headers = {
        'pragma': 'no-cache',
        'referer': 'https://pkk5.rosreestr.ru/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        }

r = requests.get("https://pkk5.rosreestr.ru/api/features/1/66:26:2201001:4", headers=headers)

print r.json()
