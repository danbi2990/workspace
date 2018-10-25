#%%
import re
from pprint import pprint
from collections import defaultdict
import pandas as pd
from db.mongo import MyMongo
# from urllib.parse import urlsplit

#%%
with MyMongo() as db:
    url_script = db.find('public_website', 'pages')


#%%
# url_script.count()
url_script[0]

#%%
def remove_comment(script):
    script = re.sub(r'(\/\/.*\n)', '', script)
    script = re.sub(r'(\/\*[\s\S]*?\*\/)', '', script)
    return script


def get_comment_string(script):
    one_line = re.findall(r'(\/\/.*\n)', script)
    multi_line = re.findall(r'(\/\*[\s\S]*?\*\/)', script)

    # return string
    return '\n'.join(one_line) + '\n' + '\n'.join(multi_line)


def get_active_x_name_list(script):
    return re.findall(r'ActiveXObject\((.*)\)', script)


test_str = '''
var ExcelApp = new ActiveXObject("Excel.Application");
var ExcelApp = new ActiveXObject("Excel.test");
// hihi hihi
hihihi
/*dd
hihi
var ExcelApp = new ActiveXObject("Excel.Application");
*/
hihi
/*
hiihi2
*/
hihi
'''


def analyze_script(ax_list, script):
    new_list = get_active_x_name_list(script)
    if new_list:
        ax_list.extend(new_list)


# res = remove_comment(test_str)
res_str = get_comment_string(test_str)
ax_list = get_active_x_name_list(res_str)
print(ax_list)

#%%
url_activated = defaultdict(dict)

for u in url_script:
    active_x_in_comment = []
    active_x_in_non_comment = []
    for script in u['jsScript']:
        comment_string = get_comment_string(script)
        analyze_script(active_x_in_comment, comment_string)

        script_string = remove_comment(script)
        analyze_script(active_x_in_non_comment, script_string)

    url_activated[u['url']]['active_x_in_comment'] = active_x_in_comment
    url_activated[u['url']]['active_x_in_non_comment'] = active_x_in_non_comment

#%%
with MyMongo() as db:
    # db.delete_and_insert('public_website', 'active_x', url_activated)
    obj = db.get_table_obj('public_website', 'active_x')
    obj.insert_one(url_activated)

#%%
# len(url_activated)

df_data = []

url_non_comment = {}
for url, script in url_activated.items():
    for active_x in script['active_x_in_non_comment']:
        df_data.append((url, active_x))

df_data[:3]
# url_non_comment

#%%
df_ax_script = pd.DataFrame(columns=['url', 'activex'], data=df_data)

#%%
df_ax_script.head()


#%%
df_ax_script.groupby('activex').agg({'activex': 'count'})

#%%


#%%


#%%


#%%


#%%












