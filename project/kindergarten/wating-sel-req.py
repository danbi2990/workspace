from selenium.webdriver.chrome.options import Options
from seleniumrequests import Chrome

chrome_options = Options()
chrome_options.add_argument("--headless")

webdriver = Chrome(chrome_options=chrome_options)
url = 'http://www.childcare.go.kr/cpms/enterwait/EntWaitReqstNsrChoiseSIL.jsp'
data = {
    # 'alltype': 'A',
    # 'chilinnb': '',
    # 'crname': '',
    # 'crpub': '',
    # 'crspec': '',
    # 'crtype': '',
    'ctprvn': '11000',
    # 'dong': '1111065000',
    'flag': 'NsrSIL',
    'offset': '0',
    'programId': 'P001PG00010002',
    # 'road': '%EB%8C%80%ED%95%99%EB%A1%9C',
    # 'sgubun': '',
    'signgu': '11110',
}

response = webdriver.request('POST', url, data=data, verify=False)
sel_but = response.find_element_by_link_text('검색')
res2 = sel_but.click()
print(res2.text)
