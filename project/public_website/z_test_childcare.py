import requests

url = 'http://www.childcare.go.kr/'

res = requests.get(url)
print(res.text)
