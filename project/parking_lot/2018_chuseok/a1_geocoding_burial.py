from pymongo import UpdateOne

from db.mongo import MyMongo
from lib.util import print_bulk_result
from api.kakao_geocode import get_geocode_from_address


def load_burial_set_geocode(collection):
    with MyMongo() as db:
        # cemetry = list(db.find('burial', 'cemetry', {'lat': {'$exists': False}}))
        burial = list(db.find('burial', collection, {'lat': {'$exists': False}}))

    # print(cemetry[1])
    # print(enshrinement)

    queries = []
    for doc in burial:
        address = get_geocode_from_address(doc['주소'], None, doc['시설명'])
        if type(address) == str:
            print('Address Not Found.')
            print(doc['주소'], doc['시설명'])
            continue

        # lat, lng = address['y'], address['x']
        doc['lat'] = address['y']
        doc['lng'] = address['x']
        doc['filter0'] = address.get('region_1depth_name')
        doc['filter1'] = address.get('region_2depth_name')
        doc['filter2'] = address.get('region_3depth_name')

        queries.append(UpdateOne({'_id': doc['_id']}, {'$set': doc}, upsert=True))

        if len(queries) == 20:
            with MyMongo() as db:
                obj = db.get_table_obj('burial', collection)
                result = obj.bulk_write(queries)
                print_bulk_result(result)
                queries.clear()

    with MyMongo() as db:
        obj = db.get_table_obj('burial', collection)
        result = obj.bulk_write(queries)
        print_bulk_result(result)
        queries.clear()


cols = ['cemetry', 'enshrinement', 'natural_burying']
collection = 'natural_burying'
load_burial_set_geocode(collection)
