from pprint import pprint
# import requests
# from xmltodict import parse
# from common import get_items, get_data_frame, KEY

from api.public_portal import get_refined_dict_from_url

url = 'http://apis.data.go.kr/9710000/BillInfoService/getBillInfoList?'

params = {
    'numOfRows': '10',
    'pageNo': '1',
    'start_ord': '20',
    'end_ord': '20',
}

# r = requests.get(get_url())
# d = parse(r.text)
# print(d)
# d1 = get_items(d)
dct = get_refined_dict_from_url(url, params)
# print(d1['total'])

if dct['total'] == 0:
    print(dct['header'])

numOfRows = 200
pageCnt = int(int(dct['total']) / numOfRows) + 1
# print(pageCnt)  # 66

# for i in [65]:
for i in range(pageCnt):
    url = get_url(numOfRows, pageCnt - i)
    df = get_data_frame(url, 3)
    if df is not None:
        # print(df1)
        df0 = df.set_index('billId').drop(columns=['summary'])
        tsv0 = df0.to_csv(sep='\t')
        with open(f'../data/20th/bill/list1/{i:0>3d}-{numOfRows}.tsv', 'w') as\
                f:
            f.write(tsv0)
            print(f'list/{i:0>3d}-{numOfRows}.tsv saved.')

        df1 = df.loc[::, ['billId', 'summary']].set_index('billId')
        tsv1 = df1.to_csv(sep='\t')
        # print(tsv1)
        with open(f'../data/20th/bill/description/{i:0>3d}-{numOfRows}.tsv',
                  'w') as f:
            f.write(tsv1)
            print(f'description/{i:0>3d}-{numOfRows}.tsv saved.')

# pprint(df)
