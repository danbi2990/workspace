import re
from pprint import pprint

import pandas as pd
from pymongo import UpdateOne

from db.mongo_connection import MyMongo
from util.util import print_bulk_result

pd.set_option('display.expand_frame_repr', False)
with MyMongo() as db:
    sht_obj = db.get_table_obj('hot_summer', 'shelter')

shelter = list(sht_obj.find())

for s in shelter:
    if re.match(r'^\d', s['구주소']):

        continue
    splited = s['구주소'].split()
    if len(splited) < 2:
        continue
    s['filter0'] = splited[0]
    s['filter1'] = splited[1]

# pprint(shelter[:5])
# df = pd.DataFrame(shelter)
queries = [
    UpdateOne(
        {'_id': s['_id']},
        {'$set': s}
    )
    for s in shelter
]

with MyMongo() as db:
    obj = db.get_table_obj('hot_summer', 'shelter')
    result = obj.bulk_write(queries)
    print_bulk_result(result)


# df = pd.DataFrame(shelter)

# try:
#     # split_addr = df['구주소'].str.split()
#     # print(type(split_addr))
#     df['filter0'] = df['구주소'].str.split()[0]
#     df['filter1'] = df['구주소'].str.split()[1]

# except ValueError as e:
#     print(e)
#     # print(split_addr[0])


# print(df[:10])
