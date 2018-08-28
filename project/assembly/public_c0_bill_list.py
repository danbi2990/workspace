from pprint import pprint
import requests
from xmltodict import parse
from common import get_items, get_data_frame, KEY


def get_url(numOfRows=10, pageNo=1):
    url = f'http://apis.data.go.kr/9710000/BillInfoService/getBillInfoList?'
    url += f'ServiceKey={KEY}&numOfRows={numOfRows}&pageNo={pageNo}'
    url += '&start_ord=20&end_ord=20'
    return url

r = requests.get(get_url())
d = parse(r.text)
# print(d)
d1 = get_items(d)
print(d1['total'])
if d1['total'] == 0:
    print(d1['header'])

numOfRows = 200
pageCnt = int(int(d1['total']) / numOfRows) + 1
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
