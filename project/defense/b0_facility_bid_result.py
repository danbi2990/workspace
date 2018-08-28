from pprint import pprint
from datetime import datetime

from pymongo import UpdateOne

from api.common import get_df_as_per_total, get_refined_dict_from_url, get_items_from_dict, get_df_from_url
from db.mongo_connection import MyMongo
from lib.util import print_bulk_result

url = 'http://openapi.d2b.go.kr/openapi/service/BidResultInfoService/getFcltyCmpetBidResultList'
params = {
    'opengDateBegin': '20180101',
    'opengDateEnd': '20190101',
    'numOfRows': '4000',
}

# result = get_df_from_url(url, params)
# tmp0 = result.groupby('pblancNo').agg({'pblancNo': 'count'})
# dup = tmp0.loc[tmp0['pblancNo'] > 1]

# dup = dup.rename(columns={'pblancNo': 'cnt'})
# dup = dup.reset_index()
# dup2 = result.merge(dup, on='pblancNo')
# print(dup2[['pblancNo', 'pblancOdr', 'cntrwkNo', 'cnt']])

dct = get_refined_dict_from_url(url, params)
items = get_items_from_dict(dct)

queries = [
    UpdateOne(
        {'pblancNo': i['pblancNo'], 'pblancOdr': i['pblancOdr']},
        {'$set': i},
        upsert=True,
    ) for i in items
]

# print(queries)

with MyMongo() as db:
    print('Run upsert operation.')
    obj = db.get_table_obj('defense', 'facility_bid_result')
    result = obj.bulk_write(queries)

print_bulk_result(result)



# time_stamp = datetime.now()

# pprint(dct)

# with MyMongo() as db:
#     prev_df = db.get_df_from_table('defense', 'orntCode')
#     db.archive_complement_and_dump_new(prev_df, df, 'code', 'defense',
#                                        'orntCode', 'orntCode_archive')
