# %%
import os
import pandas as pd
from db.mongo import MyMongo

# %%
with MyMongo() as db:
    violator = db.get_df_from_table('kindergarten', 'violator')

violator
# %%
ctprvn = violator['시도']
ctprvn

# %%
vio_count_per_ctp = ctprvn.value_counts()

# %%
violation = violator['violation']; violation

# %%
abusing = [x for x in violation if '학대' in x]; abusing
fake = [x for x in violation if '허위' in x]; fake
whatelse = [x for x in violation if '학대' not in x and '허위' not in x]; whatelse

# %%
print(len(violation))
print(len(abusing), len(fake))

# %%
base_path = '/Users/jake/OneDrive - leverage innovative users/Documents/kindergarten'
location_file = '전국어린이집표준데이터.csv'
population_file = '아동인구.tsv'
location_path = os.path.join(base_path, location_file)
population_path = os.path.join(base_path, population_file)

kinder = pd.read_csv(location_path, sep=','); kinder
population = pd.read_csv(population_path, sep='\t');population
# %%
ctprvn2 = kinder['시도명']; ctprvn2

# %%
kinder_count_per_ctp = ctprvn2.value_counts()
kinder_count_per_ctp.index
# %%
def get_vio_ratio(row):
    return row['위반'] / row['개수'] * 100

vio_and_kinder = pd.concat([vio_count_per_ctp, kinder_count_per_ctp], axis=1); vio_and_kinder
vio_and_kinder.fillna(0, inplace=True); vio_and_kinder
vio_and_kinder.rename(columns={'시도': '위반', '시도명': '개수'}, inplace=True); vio_and_kinder
vio_and_kinder['비율'] = vio_and_kinder.apply(get_vio_ratio, axis=1); vio_and_kinder
vio_and_kinder.sort_values('비율', ascending=False)

# %%
# %%
# %%
# %%
# %%
