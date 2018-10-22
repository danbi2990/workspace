from api.public_portal import get_public_portal_api_key, get_raw_dict_from_url
import requests
import urllib.parse


url = 'http://openapi.arko.or.kr:8080/openapi/service/MunhWaNuriCard/getList'
# key = get_public_portal_api_key()
params = {
    'pageNo': '1',
    'numOfRows': '10',
}
# query_params = urllib.parse.urlencode(params)

# url = f'{url}&ServiceKey={key}&{query_params}'
result = get_raw_dict_from_url(url, params)

# print(url)
# res = requests.get(url)
print(result)
