import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.gov.kr/portal/main'
res = requests.get(url)

soup = bs(res.text, 'html.parser')

scripts = soup.find_all('script')

print(scripts)
