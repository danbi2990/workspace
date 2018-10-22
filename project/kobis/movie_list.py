from pprint import pprint

# import pandas as pd
# from pymongo import MongoClient

from common import (get_url, fetch_data)

# mvs = pd.read_csv('../data/top_500_movies.tsv', sep='\t')
# print(mvs)


def get_movie_list(dict):
    return dict['movieListResult']['movieList']


url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieLi\
st.json'
params = dict(
    movieNm='',
    openStartDt='',
    openEndDt='',
)

params['movieNm'] = '명량'
# 명량: 20129370

url0 = get_url(url, params)
data = fetch_data(url0)
pprint(data['movieListResult']['movieList'])

# client = MongoClient()
# db = client.kobis
# mvs = db.movies
# mvs.insert_many(get_movie_list(data))
# client.close()


'''
{'movieListResult': {'movieList': [{'companys': [{'companyCd': '20123063',
                                                  'companyNm': '(주)빅스톤픽쳐스'}],
                                    'directors': [{'peopleNm': '김한민'}],
                                    'genreAlt': '사극,액션',
                                    'movieCd': '20129370',
                                    'movieNm': '명량',
                                    'movieNmEn': 'Roaring Currents',
                                    'nationAlt': '한국',
                                    'openDt': '20140730',
                                    'prdtStatNm': '개봉',
                                    'prdtYear': '2013',
                                    'repGenreNm': '사극',
                                    'repNationNm': '한국',
                                    'typeNm': '장편'},
                                   {'companys': [{'companyCd': '20123063',
                                                  'companyNm': '(주)빅스톤픽쳐스'}],
                                    'directors': [{'peopleNm': '정세교'},
                                                  {'peopleNm': '김한민'}],
                                    'genreAlt': '다큐멘터리',
                                    'movieCd': '20157431',
                                    'movieNm': '명량: 회오리 바다를 향하여',
                                    'movieNmEn': 'Roaring Currents: The Road '
                                                 'of the Admiral',
                                    'nationAlt': '한국',
                                    'openDt': '20150507',
                                    'prdtStatNm': '개봉',
                                    'prdtYear': '2015',
                                    'repGenreNm': '다큐멘터리',
                                    'repNationNm': '한국',
                                    'typeNm': '장편'}],
                     'source': '영화진흥위원회',
                     'totCnt': 2}}
[Finished in 1.5s]
'''
