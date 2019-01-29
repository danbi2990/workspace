import re
import os

import pandas as pd

from lib.scrape import get_soup_from_url


url = 'http://www.alio.go.kr/managementItem.do'
soup = get_soup_from_url(url)
all_a = soup.select('.left a')
# print(all_a)
org_name_and_code = {a.text: re.search(r'C\d\d\d\d', str(a)).group(0) for a in all_a}
# print(org_name_and_code)

# df = pd.DataFrame(columns=['기관명', 'code', '신분', '1인당 복리후생비'])


if not os.path.exists('welfare.tsv'):
    with open('welfare.tsv', 'w') as f:
        f.write('기관명\tcode\t신분\t1인당 복리후생비\n')

df = pd.read_csv('welfare.tsv', sep='\t')

for org_name, code in org_name_and_code.items():
    if code in df['code'].tolist():
        print(org_name, ': already exists, skipped.')
        continue

    url2 = f'http://www.alio.go.kr/popReportTerm.do?apbaId={code}&reportFormRootNo=20801#toc-127'
    # url2 = f'http://www.alio.go.kr/popReportTerm.do?apbaId=C0268&reportFormRootNo=20801#toc-127'

    try:
        tables = pd.read_html(url2)
    except ValueError as e:
        print(org_name, ' : No welfare.')
        continue

    collected = []
    for i, table in enumerate(tables):
        if ('연도' in table.columns) and (table['연도']=='2017년').any().any() and (table['연도']=='학자금').any().any():
            data = {}
            data['기관명'] = org_name.replace('# ', '')
            data['code'] = code
            # print(tables[i-1].index)
            # print(tables[i-1].columns)
            data['신분'] = tables[i-1].loc[0::, 0].values[0]
            data['1인당 복리후생비'] = tables[i].loc[tables[i]['연도']=='소계']['항목'].values[0]
            # data['1인당 복리후생비']
            df2 = pd.DataFrame([data])
            df = df.append(df2, ignore_index=True)

            # print(tables[i-1])
            # print(tables[i])
            # print(data)
    df.to_csv('welfare.tsv', sep='\t', index=False)
    print('file saved.')
