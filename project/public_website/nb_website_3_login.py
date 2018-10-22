#%%
from collections import defaultdict
import pandas as pd
from db.mongo import MyMongo

#%%
with MyMongo() as db:
    # df = db.get_df_from_table('public_website', 'website_login')
    dct = list(db.find('public_website', 'website_login'))

#%%
# cnt_domain = df.groupby('netLoc').agg({'netLoc': 'count'})
# print(len(cnt_domain))
# 944: login 페이지 있는게 너무 적다?

#%%
js_file_dict = defaultdict(set)

# df['jsFile']
# print(dct)
for item in dct:
    net_loc = item['netLoc']
    js_file_list = item['jsFile']

    for file in js_file_list:
        js_file_dict[net_loc].add(file)

print(js_file_dict)


#%%
print(js_file_dict['www.gov.kr'])

#%%
js_file_list = []
for net_loc, file_set in js_file_dict.items():
    for file in file_set:
        js_file_list.append((net_loc, file))

#%%
js_keyword_dict = defaultdict(set)
for net_loc, files in js_file_dict.items():
    for file in files:
        keywords = file.split('/')
        for keyword in keywords:
            # js_keyword_list.append((net_loc, keyword))
            js_keyword_dict[net_loc].add(keyword)

# print(js_keyword_list)

#%%
js_keyword_list = []
for net_loc, keyword_set in js_keyword_dict.items():
    for keyword in keyword_set:
        js_keyword_list.append((net_loc, keyword))

#%%
df = pd.DataFrame(columns=['netLoc', 'keywords'], data=js_keyword_list)

df_loc_file = pd.DataFrame(columns=['netLoc', 'file'], data=js_file_list)


#%%
# df['netLoc']
df.to_csv('~/Dev/workspace/project/public_website/data_/js_keywords.tsv', sep='\t', index=False)

#%%
df_loc_file.to_csv('~/Dev/workspace/project/public_website/data_/js_files.tsv', sep='\t', index=False)

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


