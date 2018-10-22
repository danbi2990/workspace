import requests

url = 'https://www.gov.kr/portal/main'

res = requests.get(url)
print(res.text)
