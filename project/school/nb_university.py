# %%
import pandas as pd
from db.mongo import MyMongo

pd.set_option('display.expand_frame_repr', False)

# %%
with MyMongo() as db:
    univ = db.get_df_from_table('school', 'university')

# %%
four = univ.loc[univ['schoolType']=='일반대학']; four
four.groupby(['region']).agg({'_id': 'count'})
# grp = univ.groupby(['region', 'schoolGubun']).agg({'_id': 'count'}); grp
# grp.sort_values('_id', ascending=False)

# %%
univ['schoolType'].value_counts()

# %%
# univ['region'].isna()
print(univ.columns)
null_region = univ.loc[univ['region']=='null']
null_region

# %%
# %%
# %%
# %%
# %%
# %%


