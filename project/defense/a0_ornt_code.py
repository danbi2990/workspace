# from pprint import pprint
from datetime import datetime
from api.common import get_df_as_per_total
from db.mongo_connection import MyMongo

url = 'http://openapi.d2b.go.kr/openapi/service/CodeInqireService/getOrntCodeList'
params = {
}

df = get_df_as_per_total(url, params)
time_stamp = datetime.now()
df['update_on'] = time_stamp

with MyMongo() as db:
    prev_df = db.get_df_from_table('defense', 'orntCode')
    db.archive_complement_and_dump_new(prev_df, df, 'code', 'defense',
                                       'orntCode', 'orntCode_archive')
