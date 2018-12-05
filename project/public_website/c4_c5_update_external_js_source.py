#%%
import re
from urllib.parse import urlparse
from urllib3.exceptions import ReadTimeoutError

import requests
from requests.exceptions import ConnectionError, ReadTimeout
from requests.exceptions import ContentDecodingError, TooManyRedirects
import pandas as pd

from db.mongo import MyMongo


def write_log(msg):
    print(msg)
    with open('c_external_js_log.txt', 'a') as f:
        f.write(msg + '\n')


with MyMongo() as db:
    js_files = db.get_df_from_table('public_website', 'c4_js_files_processed')
    js_already = db.get_df_from_table('public_website', 'c5_js_code_external')

js_files_2 = pd.DataFrame(columns=['netLoc', 'jsFile', 'jsSource'])
with open('c_external_js_log.txt', 'r') as f:
    log = f.read()

js_error = re.findall(r'(http.+)\n', log)
web_path_already = []

if len(js_already) != 0:
    web_path_already = js_already['webPath'].tolist()
    web_path_already.extend(js_error)


for idx, row in js_files.iterrows():
    web_path = ''
    net_loc = row['netLoc']
    file_path = row['jsFile']
    if file_path.startswith('//'):
        web_path = urlparse(net_loc)[0] + ':' + file_path
    elif file_path.startswith('http'):
        web_path = file_path
    else:
        web_path = '/'.join([net_loc.strip('/'), file_path.strip('/')])

    # print(web_path)
    if web_path not in web_path_already:
        try:
            response = requests.get(web_path, verify=False, timeout=5)
        except ConnectionError:
            msg = f'ConnectionError. Address: {web_path}'
            write_log(msg)

            web_path_s = 'https://' + '/'.join([net_loc, file_path])
            if web_path_s not in web_path_already:
                try:
                    response = requests.get(web_path_s, verify=False, timeout=5)
                except ConnectionError:
                    msg = f'ConnectionError. Address: {web_path_s}'
                    write_log(msg)
                    continue
                except (ReadTimeout, ReadTimeoutError):
                    msg = f'ReadTimeout. Address: {web_path_s}'
                    write_log(msg)
                    continue
                except ContentDecodingError:
                    msg = f'DecodingError. Address: {web_path_s}'
                    write_log(msg)
                    continue
                except TooManyRedirects:
                    msg = f'TooManyRedirects. Address: {web_path_s}'
                    write_log(msg)
                    continue

            continue
        except (ReadTimeout, ReadTimeoutError):
            msg = f'ReadTimeout. Address: {web_path}'
            write_log(msg)
            continue
        except ContentDecodingError:
            msg = f'DecodingError. Address: {web_path}'
            write_log(msg)
            continue
        except TooManyRedirects:
            msg = f'TooManyRedirects. Address: {web_path}'
            write_log(msg)
            continue

        js_files_2 = js_files_2.append({'netLoc': net_loc, 'jsFile': file_path, 'webPath': web_path, 'jsSource': response.text}, ignore_index=True)

    if len(js_files_2) > 9:
        with MyMongo() as db:
            db.update_one_bulk('public_website', 'c5_js_code_external', js_files_2.to_dict(orient='records'), 'webPath')

        js_files_2 = pd.DataFrame(columns=['netLoc', 'jsFile', 'jsSource'])


with MyMongo() as db:
    db.update_one_bulk('public_website', 'c5_js_code_external', js_files_2.to_dict(orient='records'), 'webPath')




