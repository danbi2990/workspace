from pprint import pprint

import pandas as pd

from common import (get_url, fetch_data)

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieI\
nfo.json'

# 명량: 20129370

params = dict(
    movieCd=20129370
)

url0 = get_url(url, params)
data = fetch_data(url0)
pprint(data)

'''
movieListResult/movieList

'''
