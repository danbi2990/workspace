import pandas as pd

from db.mongo import MyMongo
from api.public_portal import get_refined_dict_from_url, get_df_from_url

'''
발의법률안 목록 정보조회
mem_name_check - G01: 대표발의, G02: 1인발의, G03: 공동발의
'''

url = 'http://apis.data.go.kr/9710000/BillInfoService/getMotionLawList'
numOfRows = 200
pars = {
    'numOfRows': 10,
    'pageNo': 1,
    'mem_name': '',
    'hj_nm': '',
    'ord': 'A01',
    'start_ord': 20,
    'end_ord': 20,
    # 'mem_name_check': 'G01'
}

with MyMongo() as db:
    members = db.get_df_from_table('assembly', 'member')[['empNm', 'hjNm']]

for index, row in members.iterrows():
    # if index == 4:
    #     break
    df = pd.DataFrame()
    nm, hj = row['empNm'], row['hjNm']
    pars['mem_name'], pars['hj_nm'], pars['numOfRows'] = nm, hj, 1

    dic = get_refined_dict_from_url(url, pars)
    total = int(dic['totalCount'])
    pars['numOfRows'] = numOfRows
    p_cnt = int(total / numOfRows) + 1
    for i in range(p_cnt):
        pars['pageNo'] = p_cnt - i
        tmp = get_df_from_url(url, pars)
        df = df.append(tmp)

    df['empNm'] = nm
    df['hjNm'] = hj
    docs = df.to_dict(orient='records')
    # print(docs)

    with MyMongo() as db:
        db.update_one_bulk('assembly', 'bill_repr', docs, 'empNm', 'hjNm', 'billId')

print('All Done.')
