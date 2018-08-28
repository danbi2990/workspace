from pymongo import UpdateOne

from db.mongo import MyMongo
from lib.util import print_bulk_result
from api.kakao_geocode import get_geocode_from_address


with MyMongo() as db:
    cursor = db.find('summer', 'shelter', {'filter2': {'$exists': False}})
    shelter = list(cursor)

# print(len(shelter))

queries = []
for doc in shelter:
    address = get_geocode_from_address(doc['도로명주소'], doc['지번주소'], doc['시설이름'])
    if type(address) == str:
        print('Address Not Found.')
        print(doc['도로명주소'], doc['지번주소'], doc['시설이름'])
        continue

    lat, lng = address['y'], address['x']
    doc['lat'] = address['y']
    doc['lng'] = address['x']
    doc['filter0'] = address['region_1depth_name']
    doc['filter1'] = address['region_2depth_name']
    doc['filter2'] = address['region_3depth_name']

    queries.append(UpdateOne({'_id': doc['_id']}, {'$set': doc}, upsert=True))

    if len(queries) == 20:
        with MyMongo() as db:
            sht_obj = db.get_table_obj('summer', 'shelter')
            result = sht_obj.bulk_write(queries)
            print_bulk_result(result)
            queries.clear()

with MyMongo() as db:
    sht_obj = db.get_table_obj('summer', 'shelter')
    result = sht_obj.bulk_write(queries)
    print_bulk_result(result)
    queries.clear()
