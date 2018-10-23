#%%
import os
import requests

import pandas as pd

from db.mongo import MyMongo

#%%
with MyMongo() as db:
    js_files = db.get_df_from_table('public_website', 'website_js_domain_proccessed')

# print(js_files.head(1))
#%%
with MyMongo() as db:
    js_already = db.get_df_from_table('public_website', 'website_external_js_source')

#%%
js_files_2 = pd.DataFrame(columns=['netLoc', 'jsFile', 'jsSource'])

web_path_already = js_already['webPath'].tolist()
for idx, row in js_files.iterrows():
    # if idx == 4:
    #     break

    net_loc = row['netLoc'].strip('/')
    file_path = row['jsFile'].strip('/')
    web_path = 'http://' + '/'.join([net_loc, file_path])

    # print(web_path)
    if web_path not in web_path_already:
        try:
            response = requests.get(web_path)
        except TypeError:
            print(web_path)
            continue
        js_files_2 = js_files_2.append({'netLoc': net_loc, 'jsFile': file_path, 'webPath': web_path, 'jsSource': response.text}, ignore_index=True)

    if len(js_files_2) > 10:
        with MyMongo() as db:
            db.update_one_bulk('public_website', 'website_external_js_source', js_files_2.to_dict(orient='records'), 'webPath')

        js_files_2 = pd.DataFrame(columns=['netLoc', 'jsFile', 'jsSource'])



# print(response.text)
# js_files_2
#%%
# result =
# js_files_2.head()

#%%
with MyMongo() as db:
    db.update_one_bulk('public_website', 'website_external_js_source', js_files_2.to_dict(orient='records'), 'webPath')


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



