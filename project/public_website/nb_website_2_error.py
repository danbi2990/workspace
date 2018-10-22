#%%
from pprint import pprint
from collections import defaultdict
import pandas as pd
from db.mongo import MyMongo
from urllib.parse import urlsplit

#%%
with MyMongo() as db:
    df_all = db.get_df_from_table('public_website', 'only_urls')
    df_success = db.get_df_from_table('public_website', 'website_login')
    df_error = db.get_df_from_table('public_website', 'website_error')
    url_all = set(df_all['url'])
    url_success = set(df_success['url'])
    url_error = set(df_error['url'])
    url_remain = url_all - url_success - url_error

#%%
len(url_remain)
url_remain

#%%
never_succeeded = url_error - url_success

#%%
df_never = pd.DataFrame(columns=['url'], data=list(never_succeeded))
df_never

#%%
df_never_status = df_never.merge(df_error, on='url', how='left')
df_never_status

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%












