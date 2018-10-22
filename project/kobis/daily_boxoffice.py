from datetime import datetime, timedelta
from pprint import pprint

import pandas as pd

from api.kobis import get_json_from_url
from db.mongo import MyMongo


def get_boxoffice_list(dict):
    return dict['boxOfficeResult']['dailyBoxOfficeList']


def add_days(sdt, days=1, fmt='%Y%m%d'):
    fdt = datetime.strptime(sdt, fmt)
    fdt += timedelta(days=days)
    return fdt.strftime(fmt)


url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDa\
ilyBoxOfficeList.json'
params = dict(
    targetDt=''
)

fmt = '%Y%m%d'
datelist = pd.date_range(
    # start='20180503',
    # end='20180503',
    start=datetime.today() - timedelta(days=1),
    end=datetime.today() - timedelta(days=1),
)

for d in datelist:
    targetDt = d.strftime(fmt)
    params['targetDt'] = targetDt
    data = get_json_from_url(url, params)
    lst = get_boxoffice_list(data)
    for e in lst:
        e['targetDt'] = targetDt
    pprint(lst)

    # mm = MyMongo(get_connection_string())
    # mm.insert_daily_boxoffice(lst)
    # mm.close_connection()
