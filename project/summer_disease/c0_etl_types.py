# %%
import os
import re
# from collections import defaultdict

import pandas as pd

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

# print(years.keys())

# %%
y2017 = years['2017']
y2018 = years['2018']
# print(y2017)
# y2018 = years['2018']

# %%
place_2017 = y2017[-2]
place_2018 = y2018[-1]
places = [
    '계', '소계(실외)', '작업장(실외)', '운동장(공원)', '논/밭', '산',
    '강가/해변', '길가', '주거지주변', '기타(실외)', '소계(실내)', '집',
    '건물', '작업장', '비닐하우스', '찜질방(사우나)', '기타(실내)'
]
value_place_2017 = place_2017.iloc[2, 1::]
value_place_2018 = place_2018.iloc[2, 1::]
# print(place_2017.iloc[2, 1::])
# print(place_2018.iloc[2, 1::])
# print(place_2018)
# del place_cols
place_years = pd.DataFrame(
    # columns=['장소', '2017', '2018'],
    data={
        '장소': places,
        '2017': value_place_2017.tolist(),
        '2018': value_place_2018.tolist()
    },
)
place_years['증가율'] = (place_years['2018'].astype(int) - place_years['2017'].astype(int)) / place_years['2017'].astype(float) * 100
# print(place_years)
place_years.to_csv('data_/온열질환자-장소별-증가율.tsv', sep='\t', index=False)

# %%
job_2017 = y2017[-1]
job_2018 = y2018[-2]
jobs = job_2018.loc[0, 1::]
value_job_2017 = job_2017.iloc[1, 1::]
value_job_2018 = job_2018.iloc[1, 1::]
# print(jobs)
# print(value_job_2018)
job_years = pd.DataFrame(
    data={
        '직업': jobs,
        '2017': value_job_2017.tolist(),
        '2018': value_job_2018.tolist(),
    }
)
job_years['증가율'] = (job_years['2018'].astype(int) - job_years['2017'].astype(int)) / job_years['2017'].astype(float) * 100

# print(job_years)
job_years.to_csv('data_/온열질환자-직업별-증가율.tsv', sep='\t', index=False)

# %%
# %%
# %%
# %%
# %%
# %%
# %%
