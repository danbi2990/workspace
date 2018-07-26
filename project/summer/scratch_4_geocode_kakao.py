from urllib.parse import urlencode, quote_plus
from pprint import pprint
import re

import requests


def get_geo_response_from_kakao(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    key = '59de66bcd53e9c76c896341d6dc4522c'
    headers = {'Authorization': f'KakaoAK {key}'}
    payload = {'query': addr, }
    encoded = urlencode(payload, quote_via=quote_plus)
    url2 = f'{url}?{encoded}'
    res = requests.get(url2, headers=headers)

    return res.json()


def fetch_and_check_geo_response(addr, key):
    res = get_geo_response_from_kakao(addr)
    if res['meta']['total_count'] != 0:
        return res['documents'][0][key]
    else:
        False


def trial_and_error_to_get_geocode(srs):
    if str(srs['신주소']) != 'nan':
        addr = srs['신주소']
        key = 'road_address'

        res = fetch_and_check_geo_response(addr, key)
        if res:
            return res

        without_paren = re.search(r'(.*)\(.+\)', srs['신주소'])
        if without_paren:
            addr = without_paren.group(1)
            print(addr)
            res = fetch_and_check_geo_response(addr, key)
            if res:
                return res

    if str(srs['구주소']) != 'nan' and not re.match(r'^\d', srs['구주소']):
        addr = srs['구주소']
        key = 'address'

        res = fetch_and_check_geo_response(addr, key)
        if res:
            return res

        if str(srs['시설이름'] != 'nan'):
            addr = srs['구주소'] + ' ' + srs['시설이름']

            res = fetch_and_check_geo_response(addr, key)
            if res:
                return res

    return 'No Address Found.'


srs = {
    '신주소': '서울특별시 양천구 목동 목동중앙북로20길 7-5, 경로당 (목동)',
    '구주소': '서울특별시 양천구 목2동 523-47 달거리경로당',
    '시설이름': '달거리경로당',
}

dct = trial_and_error_to_get_geocode(srs)
# dct = r.json()
pprint(dct)

# try:
#     # road_address = dct['documents'][0]['address']
#     road_address = dct['documents'][0]['road_address']
# except IndexError as e:
#     print('IndexError occurred')
#     print(dct)

# pprint(road_address)
