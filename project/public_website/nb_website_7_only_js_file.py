#%%
from pprint import pprint
from collections import defaultdict
import pandas as pd
from db.mongo import MyMongo
# from urllib.parse import urlsplit

#%%
with MyMongo() as db:
    url_script = db.find('public_website', 'website_login_not_from_db')

#%%
without_js_script = []

for item in url_script:
    item.pop('jsScript')
    without_js_script.append(item)

#%%
without_js_script[0]

#%%
with MyMongo() as db:
    db.delete_and_insert('public_website', 'website_login_without_script', without_js_script)

#%%

domain_unique_js_file = defaultdict(set)

for item in without_js_script:
    domain = item['netLoc']
    if item['jsFile']:
        js_files = set(item['jsFile'])
        domain_unique_js_file[domain] = domain_unique_js_file[domain].union(js_files)

#%%
import os

df_data = []
i = 0
for domain, unique_files in domain_unique_js_file.items():
    # if i == 2:
    #     break
    # i += 1
    # print(domain, unique_files)
    for file in unique_files:
        # file_path = os.path.join(domain, file)
        df_data.append((domain, file))

#%%
df_files_per_domain = pd.DataFrame(columns=['netLoc', 'jsFile', 'filePath'], data=df_data)

#%%
df_files_per_domain.head()

#%%
df_files_per_domain['path'] = os.path.join(df_files_per_domain['netLoc'], df_files_per_domain['jsFile'])

#%%
with MyMongo() as db:
    db.delete_and_insert_df('public_website', 'website_js_files_per_domain', df_files_per_domain)

#%%
# len(df_files_per_domain)
df_wo_jquery = df_files_per_domain.loc[~df_files_per_domain['jsFile'].str.contains('jquery')]

#%%
# len(df_wo_jquery)
df_wo_jquery.head()

#%%
df_wo_j_min = df_wo_jquery.loc[~df_wo_jquery['jsFile'].str.contains('.min')]

#%%
# len(df_wo_j_min)
df_wo_j_min.head()


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

