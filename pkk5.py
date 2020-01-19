import argparse
import requests


def get_args():
    parser = argparse.ArgumentParser(description='simple script to get cadastral number by coordinates')
    parser.add_argument('-c', '--coordinates', action="store", dest="coords", type=str, required=True,
                        help="coordinates separated by whitespace")
    args = parser.parse_args()
    return args


def get_headers():
    headers = {
        'pragma': 'no-cache',
        'referer': 'https://pkk5.rosreestr.ru/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    return headers


def get_data(coords):

    headers = get_headers()
    coords = coords.replace(' ', '+')

    r = requests.get("http://pkk5.rosreestr.ru/api/features/1?text={}&tolerance=5".format(coords), headers=headers).json()
    return r


def main():
    data = get_data(get_args().coords)
    for i in data['features']:
        print 'cadastral number: ' + i['attrs']['cn']
        print 'address: ' + i['attrs']['address']


if __name__ == "__main__":
    main()
