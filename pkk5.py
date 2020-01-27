import argparse
import requests

def get_args():
    parser = argparse.ArgumentParser(description='simple script get some information by cadastral number')
    parser.add_argument('-t', '--object_type', action="store", dest="type", type=str, required=True,
                        help="1 for area, 5 for OKS")
    parser.add_argument('-cn', '--cadastral_number', action="store", dest="cn", type=str, required=True,
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


def get_data(obj_type, cn):

    headers = get_headers()

    r = requests.get('http://pkk5.rosreestr.ru/api/features/{0}/{1}'.format(obj_type, cn), headers=headers).json()
    return r


def main():
    data = get_data(get_args().type, get_args().cn)
    for j in data['feature']['attrs']:
        print j, data['feature']['attrs'][j]


if __name__ == "__main__":
    main()
