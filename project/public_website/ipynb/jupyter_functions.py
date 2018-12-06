import re
from collections import defaultdict

import pandas as pd


def remove_js_file_contain_keyword(df, keyword):
    return df[~df['jsFile'].str.contains(keyword)]


def remove_comment(script):
    script = re.sub(r'(\/\/.*\n)', '', script)
    script = re.sub(r'(\/\*[\s\S]*?\*\/)', '', script)
    return script


def get_comment(script):
    one_line = re.findall(r'(\/\/.*\n)', script)
    multi_line = re.findall(r'(\/\*[\s\S]*?\*\/)', script)

    # return string
    return '\n'.join(one_line) + '\n' + '\n'.join(multi_line)


def get_active_x(script):
    return re.findall(r'ActiveXObject\((.*?)\)', script)


def get_exe(script):
    return re.findall(r'\/(\S*\.exe)[^c]', script)
#     return re.findall(r'\/(.*\.exe)[^c]', script)


def extend_active_x(ax_list, script):
    new_list = get_active_x(script)
    if new_list:
        ax_list.extend(new_list)


def extend_exe(exe_list, script):
    new_list = get_exe(script)
    if new_list:
        exe_list.extend(new_list)


def cursor2dict_in_page(cur):
    result = defaultdict(dict)

    for u in cur:
        ax_cmt = []
        ax_srt = []
        exe_cmt = []
        exe_srt = []
        for script in u['jsScript']:
            cmt = get_comment(script)
            extend_active_x(ax_cmt, cmt)
            extend_exe(exe_cmt, cmt)

            srt = remove_comment(script)
            extend_active_x(ax_srt, srt)
            extend_exe(exe_srt, srt)

        result[u['url']]['ax_cmt'] = ax_cmt
        result[u['url']]['ax_srt'] = ax_srt
        result[u['url']]['exe_cmt'] = exe_cmt
        result[u['url']]['exe_srt'] = exe_srt

    return result


def cursor2dict_external(cur):
    result = defaultdict(dict)

    for u in cur:
        ax_cmt = []
        ax_srt = []
        exe_cmt = []
        exe_srt = []

        script = u['jsSource']

        cmt = get_comment(script)
        extend_active_x(ax_cmt, cmt)
        extend_exe(exe_cmt, cmt)

        srt = remove_comment(script)
        extend_active_x(ax_srt, srt)
        extend_exe(exe_srt, srt)

        result[u['webPath']]['ax_cmt'] = ax_cmt
        result[u['webPath']]['ax_srt'] = ax_srt
        result[u['webPath']]['exe_cmt'] = exe_cmt
        result[u['webPath']]['exe_srt'] = exe_srt

    return result


def dict2df(d):
    df_0 = []
    df_1 = []
    df_2 = []
    df_3 = []

    for url, script in d.items():
        for name in script['ax_cmt']:
            df_0.append((url, name.strip('\'\"')))
        for name in script['ax_srt']:
            df_1.append((url, name.strip('\'\"')))
        for name in script['exe_cmt']:
            remove_garbage = name.split('/')[-1]
            df_2.append((url, remove_garbage.strip('\'\"')))
        for name in script['exe_srt']:
            remove_garbage = name.split('/')[-1]
            df_3.append((url, remove_garbage.strip('\'\"')))
    df_ax_cmt = pd.DataFrame(columns=['url', 'ax_cmt'], data=df_0)
    df_ax_srt = pd.DataFrame(columns=['url', 'ax_srt'], data=df_1)
    df_exe_cmt = pd.DataFrame(columns=['url', 'exe_cmt'], data=df_2)
    df_exe_srt = pd.DataFrame(columns=['url', 'exe_srt'], data=df_3)

    return df_ax_cmt, df_ax_srt, df_exe_cmt, df_exe_srt

