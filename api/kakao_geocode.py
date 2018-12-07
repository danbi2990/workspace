import re
import socket
from urllib.parse import urlencode, quote_plus

import requests
import numpy as np


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


def fetch_geo_response_from_kakao(addr, url_type='address'):
    urls = {
        'address': 'https://dapi.kakao.com/v2/local/search/address.json',
        'keyword': 'https://dapi.kakao.com/v2/local/search/keyword.json'
    }

    def get_response_by_type(url_type, response):
        # print(response)
        if not response or response['meta']['total_count'] == 0:
            return None

        doc = response['documents'][0]
        if url_type == 'address':
            return doc['road_address'] or doc['address']

        if url_type == 'keyword':
            return doc

    url = urls[url_type]
    key = get_kakao_api_key()
    headers = {'Authorization': f'KakaoAK {key}'}
    payload = {'query': addr, }
    encoded = urlencode(payload, quote_via=quote_plus)
    url2 = f'{url}?{encoded}'
    res = requests.get(url2, headers=headers)

    return get_response_by_type(url_type, res.json())
    # return res.json()


# def get_and_check_geo_response(addr, url_type='address'):
#     res = fetch_geo_response_from_kakao(addr, url_type)
#     print(addr)
#     if res['meta']['total_count'] != 0:
#         doc = res['documents'][0]
#         return doc['road_address'] or doc['address']
#     else:
#         False


def get_cvs_geocode(road_addr, loc_name):
    # if road_addr and (road_addr != np.NaN):
    if type(road_addr) == str:
        without_paren = re.search(r'(.*)\(.+\)', road_addr)
        if without_paren:
            road_addr = without_paren.group(1)

        without_comma = re.search(r'(.*),.+', road_addr)
        if without_comma:
            road_addr = without_comma.group(1)

        res = fetch_geo_response_from_kakao(road_addr)
        if res:
            return res

    if loc_name:
        res = fetch_geo_response_from_kakao(loc_name, url_type='keyword')
        if res:
            return res

    return None


def get_geocode_from_address(road_addr, old_addr, loc_name):
    if road_addr:
        addr = road_addr

        res = fetch_geo_response_from_kakao(addr)
        if res:
            return res

        without_paren = re.search(r'(.*)\(.+\)', road_addr)
        if without_paren:
            addr = without_paren.group(1)
            # print(addr)
            res = fetch_geo_response_from_kakao(addr)
            if res:
                return res

    if old_addr and not re.match(r'^\d', old_addr):
        addr = old_addr

        res = fetch_geo_response_from_kakao(addr)
        if res:
            return res

        if not loc_name:
            addr = old_addr + ' ' + loc_name

            res = fetch_geo_response_from_kakao(addr)
            if res:
                return res

    if loc_name:
        res = fetch_geo_response_from_kakao(loc_name, url_type='keyword')
        if res:
            return res

    return 'Address Not Found.'
