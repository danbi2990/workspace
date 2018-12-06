#%%
import pandas as pd
from api.kakao_geocode import get_geocode_from_address

#%%
directory_path = '/Users/jake/OneDrive - leverage innovative users/Documents/편의점/'
file_name = 'cvs_all.tsv'
file_path = directory_path + file_name

#%%
cvs_all = pd.read_csv(file_path, sep='\t', dtype=object)
#%%
print(f'Len: {len(cvs_all)}')
print(f'Columns: {cvs_all.columns}')

#%%
tmp = cvs_all.iloc[0]; tmp


#%%
doc = get_geocode_from_address(tmp['도로명전체주소'], None, tmp['사업장명']); doc


#%%

i = 0
for idx, row in cvs_all.iterrows():
    if i == 10:
        break
    i += 1
    doc = get_geocode_from_address(row['도로명전체주소'], None, row['사업장명'])
    if doc:
        cvs_all.at[idx, 'lat'] = doc['y']
        cvs_all.at[idx, 'lng'] = doc['x']

#%%
cvs_all.iloc[:10]

#%%
from math import sin, cos, sqrt, atan2, radians


def get_distance_from_coords(lat1, lon1, lat2, lon2):

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c * 1000

    return distance

#%%
lat1, lat2 = float(cvs_all['lat'].iloc[0]), float(cvs_all['lat'].iloc[1])
lon1, lon2 = float(cvs_all['lng'].iloc[0]), float(cvs_all['lng'].iloc[1])
d = get_distance_from_coords(lat1, lon1, lat2, lon2)
print(d)

#%%
cvs_all['lat']

#%%
url_example = 'https://map.naver.com/findroute2/findWalkRoute.nhn?call=route2&output=json&coord_type=naver&search=0&start=126.9856310%2C37.5755750%2C%EC%84%B8%EB%B8%90%EC%9D%BC%EB%A0%88%EB%B8%90+%EC%A2%85%EB%A1%9C%ED%97%88%EB%B8%8C%EC%A0%90&destination=127.0025186%2C37.5836415%2CGS25+%EB%8F%99%EC%88%AD%EC%A0%90'

import requests

def get_distance_from_naver(lat1, lon1, name1, lat2, lon2, name2):
    url_base = 'https://map.naver.com/findroute2/findWalkRoute.nhn?call=route2&output=json&coord_type=naver&search=0&'
    parameters = f'start={lon1}%2C{lat1}%2C{name1}&destination={lon2}%2C{lat2}%2C{name2}'
    # parameters_encoded = quote_plus(parameters)
    url = url_base + parameters
    print(url)
    res = requests.get(url)
    return res

lat1, lat2 = float(cvs_all['lat'].iloc[0]), float(cvs_all['lat'].iloc[1])
lon1, lon2 = float(cvs_all['lng'].iloc[0]), float(cvs_all['lng'].iloc[1])
name1 = '세븐일레븐+종로허브점'
name2 = 'GS25동숭점'
d = get_distance_from_naver(lat1, lon1, name1, lat2, lon2, name2)
print(d)

# 127: lat, 37: lon
#%%
print(d.text)

#%%






