#%%
import pandas as pd
from db.mongo import MyMongo
from urllib.parse import urlsplit

with MyMongo() as db:
    df = db.get_df_from_table('public_website', 'only_urls')
    url_all = set(df['url'])
    df2 = db.get_df_from_table('public_website', 'website_login')
    url_already = set(df2['url'])
    # urls = list(db.find('public_website', 'only_urls'))

url_new = url_all - url_already
print(len(url_all), len(url_already), len(url_new))

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%





