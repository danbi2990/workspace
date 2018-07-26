from api.common import get_df_from_url
from db.mongo_connection import MyMongo


def fetch_passenger(selectdate):
    url = 'http://openapi.airport.kr/openapi/service/PassengerNoticeKR/getfPassengerNoticeIKR'
    params = {
        'selectdate': 0,
    }
    params['selectdate'] = selectdate
    df = get_df_from_url(url, params)
    idx = df.loc[df['adate']=='합계'].index
    idxdec = idx - 1
    date = df.iloc[idxdec]['adate'].values[0]
    df.at[idx, 'adate'] = date
    df.at[idx, 'atime'] = 'total'

    with MyMongo() as db:
        passenger = db.get_table_obj('airport', 'passenger')
        passenger.delete_many({'adate': date})
        print(f'Old Data Removed from \'{passenger}\', date: {date}.')
        passenger.insert_many(df.to_dict(orient='records'))
        print(f'New Data inserted to \'{passenger}\'.')


selectdate_list = [0, 1]
for d in selectdate_list:
    fetch_passenger(d)
