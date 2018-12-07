import requests

def get_distance_from_naver(lat1, lon1, name1, lat2, lon2, name2):
    url_base = 'https://map.naver.com/findroute2/findWalkRoute.nhn?call=route2&output=json&coord_type=naver&search=0&'
    parameters = f'start={lon1}%2C{lat1}%2C{name1}&destination={lon2}%2C{lat2}%2C{name2}'
    # parameters_encoded = quote_plus(parameters)
    url = url_base + parameters
    print(url)
    res = requests.get(url)
    return res

# lat1, lat2 = '37.572482119354014', '37.57306227195158'
# lon1, lon2 = '126.9838128807272', '126.98326485978382'
lat1, lat2 = '37.577146200573374', '37.576335287688764'
lon1, lon2 = '126.96943017884111', '126.96933996356815'
name1 = '세븐일레븐+종로배화점'
name2 = '씨유+종로사직공원점'
d = get_distance_from_naver(lat1, lon1, name1, lat2, lon2, name2)
print(d)
