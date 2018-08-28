import socket
import urllib.parse
from pprint import pprint

import requests
import pandas as pd
from xmltodict import parse

pd.set_option('display.expand_frame_repr', False)


def get_public_portal_api_key():
    hname = socket.gethostname()
    api_key = ''
    if hname == 'ideapad':
        file_path = '/home/jake/Private/public_portal_api_key.txt'
    elif hname == 'danbi-mac.local':
        file_path = '/Users/jake/Private/public_portal_api_key.txt'

    with open(file_path) as f:
        api_key = f.read()
    return api_key.strip()


def add_params_to_base_url(url, params):
    api_key = get_public_portal_api_key()
    query_params = urllib.parse.urlencode(params)
    return f'{url}?ServiceKey={api_key}&{query_params}'


def refine_raw_dict(d):
    res = d.get('response')
    header = None if res is None else res.get('header')
    body = None if res is None else res.get('body')
    total = 0 if body is None else body.get('totalCount')
    items = None if body is None else body.get('items')
    item = None if items is None else items.get('item')

    sres = d.get('OpenAPI_ServiceResponse')
    cmmMsgHeader = None if sres is None else sres.get('cmmMsgHeader')
    errMsg = None if cmmMsgHeader is None else cmmMsgHeader.get('errMsg')
    returnAuthMsg = None if cmmMsgHeader is None else cmmMsgHeader\
        .get('returnAuthMsg')
    returnReasonCode = None if cmmMsgHeader is None else cmmMsgHeader\
        .get('returnReasonCode')
    # print(res, header, body, total, items, item, sres, cmmMsgHeader, errMsg,
    # returnAuthMsg, returnReasonCode)
    result = {
        'header': header,
        'body': body,
        'totalCount': total,
        'items': items,
        'item': item,
        'sres': sres,
        'cmmMsgHeader': cmmMsgHeader,
        'errMsg': errMsg,
        'returnAuthMsg': returnAuthMsg,
        'returnReasonCode': returnReasonCode,
    }
    return result


def get_raw_dict_from_url(url, params={}):
    """
    Returns: {header, body, total, items, item, sres, cmmMsgHeader, errMsg
                returnAuthMsg, returnReasonCode}
    """
    if params:
        url = add_params_to_base_url(url, params)
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = parse(r.text)
    return d


def get_refined_dict_from_url(url, params={}):
    raw_dict = get_raw_dict_from_url(url, params)
    refined_dict = refine_raw_dict(raw_dict)
    return refined_dict


def get_items_from_dict(d):
    try:
        items = d['item']
    except AttributeError:
        pprint(d)
    return items


def get_df_from_dict(d):
    # h = d['header']
    # if h is None or h['resultCode'] != '00':
    #     pprint(d)
    #     return False
    items = get_items_from_dict(d)
    if isinstance(items, dict):
        items = [items]
    df = pd.DataFrame(items)
    return df


def get_df_from_url(url, params={}):
    d = get_refined_dict_from_url(url, params)
    return get_df_from_dict(d)


def get_df_as_per_total(url, params):
    refined_dict = get_refined_dict_from_url(url, params)
    total = refined_dict['totalCount']
    if total is None:
        return get_df_from_dict(refined_dict)
    params['numOfRows'] = total.strip()
    return get_df_from_url(url, params)


def save_tsv_with_multiple_pages(url, pars, path, total, numOfRows):
    pars['numOfRows'] = numOfRows
    p_cnt = int(total / numOfRows) + 1
    for i in range(p_cnt):
        pars['pageNo'] = p_cnt - i
        df = get_df_from_url(url, pars)
        tsv = df.to_csv(sep='\t', index=False)
        with open(f'{path}/{i:0>3d}-{numOfRows}.tsv', 'w') as f:
            f.write(tsv)
            print(f'{i:0>3d}-{numOfRows}.tsv saved.')


def save_tsv_from_df(file_name, df):
    df.to_csv(file_name, sep='\t', index=False)


def write_log(file, msg):
    with open(file, 'a') as f:
        f.write(msg)
