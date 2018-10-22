#%%
from pprint import pprint
from collections import defaultdict
import pandas as pd
from db.mongo import MyMongo
from urllib.parse import urlsplit

#%%
with MyMongo() as db:
    js = list(db.find('public_website', 'website_login'))

#%%
# wizvera
keywords = ['wizvera', 'anysign4pc', 'touchen', 'ipinside', 'softcamp', 'nprotect', 'astx', 'ksign', 'initech']
result = defaultdict(list)

for item in js:
    for keyword in keywords:
        for file in item['jsFile']:
            if keyword in file.lower():
                result[keyword].append(item['url'])

#%%
result

#%%
ax_url = []
for k, v in result.items():
    for url in v:
        ax_url.append((k, url))

ax_url

#%%
df_ax_url = pd.DataFrame(columns=['ActiveX', 'URL'], data=ax_url)
# df['netLoc']
df_ax_url.to_csv('~/Dev/workspace/project/public_website/data_/ActiveX_URL.tsv', sep='\t', index=False)

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%












