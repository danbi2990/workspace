# from pprint import pprint
from datetime import datetime, timedelta

import pandas as pd

from api.common import get_df_as_per_total
from db.mongo_connection import MyMongo

pd.set_option('display.expand_frame_repr', False)

fmt = '%Y%m%d'
date = datetime.now()
date_str = date.strftime(fmt)

# one_day = timedelta(days=-3)
# date_end = date_start + one_day
# date_end_str = date_end.strftime(fmt)
# print(date_end_str)

date_range_dash = pd.date_range(start='2018-01-01', end='2019-01-01')
date_range = [x.strftime(fmt) for x in date_range_dash]

for d in date_range:
    with MyMongo() as db:
        bid_result = db.get_df_from_table('defense', 'facility_bid_result', {'opengDate': date_str})

    if bid_result.empty:
        continue

    url = 'http://openapi.d2b.go.kr/openapi/service/BidResultInfoService/getFcltyCmpetBidResultMnufList'
    params = {
        'orntCode': '',
        'cntrwkNo': '',
        'ntatPlanDate': '',
    }

    for index, row in bid_result.iterrows():
        params['orntCode'] = row['orntCode']
        params['cntrwkNo'] = row['cntrwkNo']
        params['ntatPlanDate'] = row['opengDate']

        df = get_df_as_per_total(url, params)

        time_stamp = datetime.now()
        df['update_on'] = time_stamp
        print(df)








# print(df.columns)

# with MyMongo() as db:
#     prev_df = db.get_df_from_table('defense', 'orntCode')
#     db.archive_complement_and_dump_new(prev_df, df, 'code', 'defense',
#                                        'orntCode', 'orntCode_archive')
