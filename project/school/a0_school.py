from pprint import pprint

import requests

from db.mongo import MyMongo

url = 'http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=74751f165497de438a2edf355c8028a7&svcType=api&svcCode=SCHOOL&contentType=json&thisPage=1&perPage=10&gubun=alte_list'

gubun = ['elem_list', 'midd_list', 'high_list', 'univ_list', 'seet_list', 'alte_list']

response = requests.get(url)

result = response.json()
content = result['dataSearch']['content']
pprint(content)
# print(len(content))

# with MyMongo() as db:
#     db.insert_many('school', 'university', content)


'''
apiKey  String[필수]      OPENAPI 등록 신청 후 관리자로부터 발급받은 KEY값
svcType String[필수]  api api
svcCode String[필수]  SCHOOL  리스트 : SCHOOL
contentType String      xml or json 형태 (URL 에서 .xml, .json 생략) 예: //www.career.go.kr/cnet/openapi/getOpenApi?apiKey=인증키&contentType=xml
gubun   String[필수]      학교 분류
    elem_list, midd_list, high_list, univ_list, seet_list(특수/기타학교), alte_list(대안학교)
region  String      지역
sch1    String      학교유형1
sch2    String      학교유형2
est String      설립유형
대학교 : 국립, 사립, 공립
대안학교 : 인가, 비인가, 위탁형
thisPage    String
1
현재페이지
perPage String
10
한페이지당 건수
searchSchulNm   String

검색어(초등학교, 중학교, 고등학교, 특수학교, 대안학교, 대학교)

'''
