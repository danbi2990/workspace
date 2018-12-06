
import socket
from urllib.parse import urlencode, quote_plus

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

for idx, row in cvs_tobacco.loc[cvs_tobacco['lat'].isna()].iterrows():
    addr = row['도로명전체주소']
    name = row['사업장명']
    doc = get_cvs_geocode(addr, name)
    if doc:
        res = {}
        res['관리번호'] = row['관리번호']
        res['lat'] = doc['y']
        res['lng'] = doc['x']
        buffer_.append(res)
        # cvs_tobacco.at[idx, 'lat'] = doc['y']
        # cvs_tobacco.at[idx, 'lng'] = doc['x']

    if len(buffer_) == 20:
        with MyMongo() as db:
            db.update_one_bulk('cvs', 'cvs', buffer_, '관리번호')
        buffer_.clear()

with MyMongo() as db:
    db.update_one_bulk('cvs', 'cvs', buffer_, '관리번호')
