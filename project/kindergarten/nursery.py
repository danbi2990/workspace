import requests

url = 'https://www.childcare.go.kr/cpis2gi/nursery/NurseryContentsSlL.jsp?programId=P0001PG00001909&flag=NSSlPL&offset=0&ctprvn=11000&signgu=11110&areaType=1&dong=&crtype=&crspec=&crpub=&crcert=&sgubun=&crname='

r = requests.get(url, verify=False)

print(r.text)
