# %%
from db.mongo import MyMongo

# %%
with MyMongo() as db:
    df = db.get_df_from_table('public_website', 'website')

# %%
pageNo = df.groupby('pageNo').agg({'pageNo': 'count'})

# %%
err = pageNo.loc[pageNo['pageNo'] < 10]

# %%
len(err)
# 2121 page는 빠져야함 (마지막)

# %%
df.columns

# %%
# print(type(only_urls))
with MyMongo() as db:
    db.delete_and_insert_df('public_website', 'only_urls', df[['url', 'name']])
    # db.delete_many('public_website', 'only_urls')
    # db.insert_many('public_website', 'only_urls', only_urls)

# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%

