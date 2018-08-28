# %%
from pprint import pprint
from db.mongo import MyMongo

# %%
with MyMongo() as db:
    # res = db.find('summer', 'shelter')
    # shelter = list(res)
    shelter = db.get_df_from_table('summer', 'shelter')

# %%
pprint(len(shelter))
pprint(shelter)

# %%
types = shelter.groupby('시설종류').agg({'시설종류': 'count'}).sort_values('시설종류', ascending=False)
print(types)

# %%
types.to_csv('~/Documents/summer_disease/무더위쉼터_시설종류.tsv', sep='\t')

# %%
# %%
# %%
# %%
# %%
# %%
