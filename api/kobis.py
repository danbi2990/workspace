from urllib.parse import urlencode
# from pprint import pprint
# import socket

import requests


def get_url(url, params={}):
    KEY = '8ed1be3a773c6b4e6bccb8fe28296f98'
    query_params = urlencode(params)
    return f'{url}?key={KEY}&{query_params}'


def get_json_from_url(url, params={}):
    """
    Returns: {header, body, total, items, item, sres, cmmMsgHeader, errMsg
                returnAuthMsg, returnReasonCode}
    """
    url2 = get_url(url, params)
    r = requests.get(url2)
    res = r.json()
    return res
