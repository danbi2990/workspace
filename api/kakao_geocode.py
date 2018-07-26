import re
import socket
from urllib.parse import urlencode, quote_plus

import requests


def get_kakao_api_key():
    hname = socket.gethostname()
    api_key = ''
    if hname == 'ideapad':
        file_path = '/home/jake/Private/kakao_api_key.txt'
    elif hname == 'danbi-mac.local':
        file_path = '/Users/jake/Private/kakao_api_key.txt'

    with open(file_path) as f:
        api_key = f.read()
    return api_key.strip()


def fetch_geo_response_from_kakao(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    key = get_kakao_api_key()
    headers = {'Authorization': f'KakaoAK {key}'}
    payload = {'query': addr, }
    encoded = urlencode(payload, quote_via=quote_plus)
    url2 = f'{url}?{encoded}'
    res = requests.get(url2, headers=headers)

    return res.json()


def get_and_check_geo_response(addr, key):
    res = fetch_geo_response_from_kakao(addr)
    if res['meta']['total_count'] != 0:
        return res['documents'][0][key]
    else:
        False


def get_geocode_from_address(road_addr, old_addr, loc_name):
    if road_addr:
        addr = road_addr
        key = 'road_address'

        res = get_and_check_geo_response(addr, key)
        if res:
            return res

        without_paren = re.search(r'(.*)\(.+\)', road_addr)
        if without_paren:
            addr = without_paren.group(1)
            # print(addr)
            res = get_and_check_geo_response(addr, key)
            if res:
                return res

    if old_addr and not re.match(r'^\d', old_addr):
        addr = old_addr
        key = 'address'

        res = get_and_check_geo_response(addr, key)
        if res:
            return res

        if not loc_name:
            addr = old_addr + ' ' + loc_name

            res = get_and_check_geo_response(addr, key)
            if res:
                return res

    return 'Address Not Found.'
