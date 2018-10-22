from pymongo import UpdateOne

import numpy as np

from db.mongo import MyMongo
from lib.util import print_bulk_result
from api.kakao_geocode import get_geocode_from_address


def load_market_set_geocode(schema, collection):
    with MyMongo() as db:
        # parking = list(db.find('market', collection, {'위도': '0.000'}))
        docs = list(db.find(schema, collection, {'위도': np.nan}))

    # print(cemetry[1])
    # print(enshrinement)

    queries = []
    for doc in docs:
        address = get_geocode_from_address(str(doc['소재지도로명주소']), None, str(doc['시장명']))
        if type(address) == str:
            print('Address Not Found.')
            print(doc['소재지도로명주소'], doc['시장명'])
            continue

        # lat, lng = address['y'], address['x']
        doc['위도'] = address['y']
        doc['경도'] = address['x']
        doc['filter0'] = address.get('region_1depth_name')
        doc['filter1'] = address.get('region_2depth_name')
        doc['filter2'] = address.get('region_3depth_name')

        queries.append(UpdateOne({'_id': doc['_id']}, {'$set': doc}, upsert=True))

        if len(queries) == 20:
            with MyMongo() as db:
                obj = db.get_table_obj(schema, collection)
                result = obj.bulk_write(queries)
                print_bulk_result(result)
                queries.clear()

    with MyMongo() as db:
        obj = db.get_table_obj(schema, collection)
        result = obj.bulk_write(queries)
        print_bulk_result(result)
        queries.clear()


cols = ['traditional']
# cols = ['organization', 'education']
for collection in cols:
    load_market_set_geocode('market', collection)

