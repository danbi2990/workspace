import socket
from urllib.parse import urlencode, quote_plus
from time import sleep

import pandas as pd
import requests

from db.mongo import MyMongo
from api.kakao_geocode import get_cvs_geocode
# from api.kakao_geocode import get_geocode_from_address


with MyMongo() as db:
    cvs_tobacco = db.get_df_from_table('cvs', 'cvs')

# cvs_tobacco = pd.read_csv('cvs_all_lat_lng.tsv', sep='\t', dtype=object).drop_duplicates(['관리번호'])

print(f'cvs_tobacco: {len(cvs_tobacco)}')  # before: 67602, after: 65541

i = 0
buffer_ = []
error_ = []

for idx, row in cvs_tobacco.loc[cvs_tobacco['lat'].isna()].iterrows():
    sleep(0.1)
    road_addr = row['도로명전체주소']
    old_addr = row['소재지전체주소']
    name = row['사업장명']
    doc = None
    res = {}
    err = {}
    doc = get_cvs_geocode(road_addr, old_addr, name)
    if doc:
        res['관리번호'] = row['관리번호']
        res['lat'] = doc['y']
        res['lng'] = doc['x']
        buffer_.append(res)
    else:
        print(road_addr)
        print(old_addr)
        print(name)
        err['관리번호'] = row['관리번호']
        err['사업장명'] = name
        err['도로명전체주소'] = road_addr
        err['소재지전체주소'] = old_addr
        error_.append(err)

        with MyMongo() as db:
            db.update_one_bulk('cvs', 'error_kakao', error_, '관리번호')
        error_.clear()
        # cvs_tobacco.at[idx, 'lat'] = doc['y']
        # cvs_tobacco.at[idx, 'lng'] = doc['x']

    if len(buffer_) == 20:
        with MyMongo() as db:
            db.update_one_bulk('cvs', 'cvs', buffer_, '관리번호')
        buffer_.clear()

with MyMongo() as db:
    db.update_one_bulk('cvs', 'cvs', buffer_, '관리번호')
