from urllib.parse import urlencode

import requests


url = 'http://211.237.50.150:7080/openapi/sample/xml/Grid_20161118000000000370_1/1/5?'

params = {
    # 'API_KEY': '7fa82ef7bbf5f4ed665c14f994b48a5f8e66fa86ddfad5483edc20c8e08b95a9',
    'TYPE': 'json',
    # 'API_URL': '',
    'START_INDEX': '1',
    'END_INDEX': '5',
    # 'DSTRCT': '',
    # 'NATION': '',
    # 'CTY': '',
}

urlp = url + urlencode(params)

res = requests.get(urlp)

print(res.text)

'''
'API_KEY': '', STRING(기본)  sample  발급받은 API_KEY
'TYPE': '',    STRING(기본)  xml 요청파일 타입 xml, json
'API_URL': '', STRING(기본)  Grid_000001 OpenAPI 서비스 URL
'START_INDEX': '', INTEGER(기본) 1   요청시작위치
'END_INDEX': '',   INTEGER(기본) 5   요청종료위치
'DSTRCT': '',  STRING(선택)  권역  권역
'NATION': '',  STRING(선택)  국가  국가
'CTY': '', STRING(선택)  도시  도시
'''