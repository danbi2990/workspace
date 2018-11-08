from urllib.parse import urlencode

import requests

url = 'http://www.wedisk.co.kr/wediskNew/Home/contentsList.do?'

params = {
    'data': {"searchType":"1","category":"00","subCategory":"","subKey":"","searchArea":"21","searchKeyword":"","pageViewRowNumber":"20","selectCategory":"00","selectSubCategory":"","pageViewPoint":"3","oldSearchOption":"","sort":"0","chkMbc":"","SubCategory":"","keyword":""}
}

# data = {"searchType":"1","category":"00","subCategory":"","subKey":"","searchArea":"21","searchKeyword":"","pageViewRowNumber":"20","selectCategory":"00","selectSubCategory":"","pageViewPoint":"3","oldSearchOption":"","sort":"0","chkMbc":"","SubCategory":"","keyword":""}

full_url = url + urlencode(params)
# response = requests.get(full_url)
# print(response.text)

print(full_url)
