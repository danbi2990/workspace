import re
import json
from pprint import pprint

import requests

from db.mongo import MyMongo

url = 'http://www.safekorea.go.kr/idsiSFK/sfk/cs/sfc/selectHtwRstrList.do'

payload = {
    "searchInfo": {
        "pageIndex": "1",
        # "pageUnit": "30",
        "pageUnit": "46000",
        # "pageSize": 4532,
        "firstIndex": "1",
        "lastIndex": "1",
        "recordCountPerPage": "10",
        "q_area_cd_3": "",
        "q_area_cd_2": "",
        "q_area_cd_1": "",
        "searchRstrNm": "",
        "searchFcltyTy": "",
        "searchYear": "2018",
        "searchChckAirconAt": "",
        "govAreaCode": "",
        "parntsBdongCd": "",
        "searchCdKey": "G116",
        "searchGb": "pageSearch",
        "acmdfclty_cd": "",
    }
}

r = requests.post(url, data=json.dumps(payload))
r.encoding = 'utf-8'
dct = r.json()

lst = dct['htwRstrList']

keys2filter = {
    'fcltyTy': '시설종류',
    'rnDtlAdres': '도로명주소',
    'rstrNm': '시설이름',
    'usePsblNmpr': '이용가능인원',
}

filtered = []
for l in lst:
    shelter = {}
    shelter['지번주소'] = l['arcd'] + ' ' + l['dtlAdres']
    for k, v in l.items():
        if k == 'rnDtlAdres':
            v = re.sub(r'\s+', ' ', v)
            v = re.sub(r'\s,', ',', v)
        if k in keys2filter.keys():
            shelter[keys2filter[k]] = v
    filtered.append(shelter)

with MyMongo() as db:
    db.delete_and_insert('summer', 'shelter', filtered)
    # print(result.inserted_count)
