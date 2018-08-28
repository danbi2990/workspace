from urllib.parse import urlencode, quote_plus
import requests

# url = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&key=AIzaSyCJZabrYsVEdBiRseFCtJC7vYq8pflfcGg&address='
addr = '서울특별시 서초구 본마을2길 2'
# url2 = url + quote_plus(addr)
# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyB17TlvXbIv0Hz7l6kQXIHwpNMGVBuTiVU
# AIzaSyCJZabrYsVEdBiRseFCtJC7vYq8pflfcGg

# https://sgisapi.lostat.go.kr/OpenAPI3/addr/geocode.json
url = 'https://sgisapi.kostat.go.kr/OpenAPI3/addr/geocode.json'
key = '2dcd93f6f0c34b869855'

payload = {
    'accessToken': key,
    'address': addr,
}

encoded = urlencode(payload, quote_via=quote_plus)
url2 = f'{url}?{encoded}'
print(url2)

r = requests.get(url2)
print(r.json())
