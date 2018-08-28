from pprint import pprint
from urllib.parse import quote_plus

import requests
import pandas as pd
from pymongo import UpdateOne

from db.mongo_connection import MyMongo
from lib.util import print_bulk_result

pd.set_option('display.expand_frame_repr', False)
# shelter = pd.read_csv('shelter_from_safekorea.tsv', sep='\t')

with MyMongo() as db:
    shelter = db.get_df_from_table('hot_summer', 'shelter')

url = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&key=AIzaSyCJZabrYsVEdBiRseFCtJC7vYq8pflfcGg&address='

# print(shelter[:15])

queries = []

for idx, srs in shelter.iterrows():

    # if idx == 30:
    #     break

    if not pd.isna(srs['lat']) and not pd.isna(srs['lng']):
        # print(srs['lat'], srs['lng'])
        continue

    addr = srs['신주소']
    if not srs['신주소']:
        print(srs['신주소'])
        addr = srs['구주소']
        if not srs['구주소']:
            print(srs['구주소'])
            continue

    try:
        url2 = url + quote_plus(addr)
    except TypeError:
        print(addr)
        continue
    # print(url2)
    r = requests.get(url2)
    dct = r.json()
    # print(dct)

    try:
        location = dct['results'][0]['geometry']['location']
    except IndexError:
        print(srs['신주소'], srs['구주소'])
        continue
    lat = location['lat']
    lng = location['lng']
    # print(lat, lng)
    # shelter.at[idx, 'lat'] = lat
    # shelter.at[idx, 'lng'] = lng
    srs.at['lat'] = lat
    srs.at['lng'] = lng

    query = UpdateOne({'_id': srs['_id']}, {'$set': srs.to_dict()}, upsert=True)
    queries.append(query)

    if len(queries) == 100:
        with MyMongo() as db:
            sht_obj = db.get_table_obj('hot_summer', 'shelter')
            result = sht_obj.bulk_write(queries)
            print_bulk_result(result)
            # sht_obj.update_many({'_id': srs['_id']}, lst)
            queries.clear()

with MyMongo() as db:
    sht_obj = db.get_table_obj('hot_summer', 'shelter')
    result = sht_obj.bulk_write(queries)
    print_bulk_result(result)
    queries.clear()

# # print(shelter.iloc[:10])
# shelter.to_csv('shelter_from_safekorea.tsv', sep='\t', index=False)
