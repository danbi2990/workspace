#%%
import os
import re
from urllib3.exceptions import ReadTimeoutError

import requests
from requests.exceptions import ConnectionError, ReadTimeout, ContentDecodingError
import pandas as pd

from db.mongo import MyMongo

#%%
with MyMongo() as db:
    js_files = db.get_df_from_table('public_website', 'website_js_domain_proccessed')
    js_already = db.get_df_from_table('public_website', 'website_external_js_source')

#%%
js_files_2 = pd.DataFrame(columns=['netLoc', 'jsFile', 'jsSource'])
with open('external_js_log.txt', 'r') as f:
    log = f.read()

js_error = re.findall(r'(http.+)\n', log)
web_path_already = js_already['webPath'].tolist()
print(len(web_path_already))
web_path_already.extend(js_error)
print(len(web_path_already))
# print(web_path_already)

# print(len(js_files))
# js_files_filtered = js_files.loc[js_files[]]

for idx, row in js_files.iterrows():
    # if idx == 4:
    #     break

    net_loc = row['netLoc'].strip('/')
    file_path = row['jsFile'].strip('/')
    web_path = 'http://' + '/'.join([net_loc, file_path])

    # print(web_path)
    if web_path not in web_path_already:
        try:
            response = requests.get(web_path, verify=False, timeout=5)
        except ConnectionError:
            msg = f'ConnectionError. Address: {web_path}'
            print(msg)
            with open('external_js_log.txt', 'a') as f:
                f.write(msg + '\n')

            web_path_s = 'https://' + '/'.join([net_loc, file_path])
            if web_path_s not in web_path_already:
                try:
                    response = requests.get(web_path_s, verify=False, timeout=5)
                except ConnectionError:
                    msg = f'ConnectionError. Address: {web_path_s}'
                    print(msg)
                    with open('external_js_log.txt', 'a') as f:
                        f.write(msg + '\n')
                    continue
                except (ReadTimeout, ReadTimeoutError):
                    msg = f'ReadTimeout. Address: {web_path_s}'
                    print(msg)
                    with open('external_js_log.txt', 'a') as f:
                        f.write(msg + '\n')
                    continue
                except ContentDecodingError:
                    msg = f'DecodingError. Address: {web_path_s}'
                    print(msg)
                    with open('external_js_log.txt', 'a') as f:
                        f.write(msg + '\n')
                    continue

            continue
        except (ReadTimeout, ReadTimeoutError):
            msg = f'ReadTimeout. Address: {web_path}'
            print(msg)
            with open('external_js_log.txt', 'a') as f:
                f.write(msg + '\n')
            continue
        except ContentDecodingError:
            msg = f'DecodingError. Address: {web_path}'
            print(msg)
            with open('external_js_log.txt', 'a') as f:
                f.write(msg + '\n')
            continue

        js_files_2 = js_files_2.append({'netLoc': net_loc, 'jsFile': file_path, 'webPath': web_path, 'jsSource': response.text}, ignore_index=True)

    if len(js_files_2) > 9:
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



