# %%
import os
import re
from collections import defaultdict

import pandas as pd
# import numpy as np

# %%
PATH = '/Users/jake/OneDrive - leverage innovative users/document/summer_disease/'

files = os.listdir(PATH)
filtered = sorted([f for f in files if f.endswith('.html')])

years = {}
for file in filtered:
    file_name = re.search(r'(.+)\.html', file).group(1)

    with open(os.path.join(PATH, file)) as f:
        content = f.read()  # for encoding
        dfs = pd.read_html(f)
        years[file_name] = dfs

print(years.keys())

# %%
y2014 = years['2014'][0]

# %%
cities = [
    '전국', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종',
]

for i, c in enumerate(cities):
    idxs = [i*2+1, i*2+2]
    for k, v in years.items():
        v[0].at[0, idxs] = c

y2014

# %%
zipped = list(zip(y2014.loc[0, ::], y2014.loc[1, ::])); zipped

# %%
multi_index = pd.MultiIndex.from_tuples(zipped); multi_index
multi_index.levels[1]

# %%
y2014.columns = multi_index; y2014
y2014_col = y2014.drop([0, 1]).reset_index(drop=True); y2014_col

# %%
multi_index.levels[0]

zip_year_col = list(zip(['2014']*2, y2014_col['서울'].columns)); zip_year_col
m_idx_year_col = pd.MultiIndex.from_tuples(zip_year_col)
test = y2014_col['서울']
test.columns = m_idx_year_col
test

# %%
cities_df = defaultdict(pd.DataFrame)

for k, v in years.items():
    v[0].columns = multi_index
    df_col = v[0].drop([0, 1]).reset_index(drop=True)
#     print(df_col)

    for city in cities:
        zip_year_col = list(zip([k]*2, ['온열질환자', '사망자']))
        m_idx_year_col = pd.MultiIndex.from_tuples(zip_year_col)
        tmp = df_col[city]
        tmp.columns = m_idx_year_col

        cities_df[city] = pd.concat([cities_df[city], tmp], axis=1)

cities_df['전국']

# %%
disease_type = ['온열질환자', '온열사망자']
output = defaultdict(pd.DataFrame)
# print(cities_df.keys())

for k, v in cities_df.items():

    for i, v2 in enumerate(disease_type):
        content = cities_df[k].iloc[:, i::2]
        try:
            content.columns = content.columns.droplevel(level=1)
        except AttributeError:
            print(content)
            print(k, v2)

#         if k == '전체' and v2 == '온열질환자':
        cols = content.columns
        for i2, v3 in content[2:].iterrows():
            for col in cols:
                try:
                    content.loc[i2, col] = float(content.loc[i2, col]) + float(content.loc[i2-1, col])
                except ValueError:
                    print(k, v2)
                    print(content)
#         print(content[1:])
        content.index.name = f'{v2} 연도별 추이'
        content.index = content.index.map(lambda x: str(x) + '주차')
        content['지역'] = k
#         output = pd.concat([output, content[1:]], axis=0)

        if k == '전국':
            content[1:].to_csv(f'data_/{v2}-전국.tsv', sep='\t')
            pass
        else:
            output[v2] = pd.concat([output[v2], content[1:]], axis=0)

output['온열질환자'].to_csv(f'data_/온열질환자-지역.tsv', sep='\t')
# output['온열사망자'].to_csv(f'data_/온열사망자-지역.tsv', sep='\t')

# %%
disease = output['온열질환자']
disease_recent = disease.loc[disease.index=='12주차', ['2018', '지역']]
# print(disease_recent)
# print(type(disease_recent))
disease_recent.to_csv(f'data_/온열질환자-지역-최근.tsv', sep='\t', index=False)

# %%
# death = output['온열사망자']
# death_recent = death.loc[disease.index=='12주차', ['2018', '지역']]
# death_recent.to_csv(f'data_/온열사망자-지역-최근.tsv', sep='\t', index=False)

# %%
# %%
# %%






