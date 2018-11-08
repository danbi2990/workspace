
# coding: utf-8

# # Preparation

# ## Import Packages

# In[118]:


import os
import re

import pandas as pd
import requests
from requests.exceptions import ConnectionError, ReadTimeout
from requests.exceptions import ContentDecodingError, TooManyRedirects

from db.mongo import MyMongo


def extract_name(x):
    try:
        return re.search(r'(.+)의원', x).group(1).strip()
    except AttributeError as e:
        return ''


def filter_refer(x, first_character):
    rexp = '^(' + re.escape(first_character) + ').+'

    return len(x) >= 2 and re.search(rexp, x)


def ETL_quotes(file_name, collection_name):
    data_dir = '/Users/jake/OneDrive - leverage innovative users/Documents/News_Item/Audit_quote/'
    quote_file = os.path.join(data_dir, file_name)
    quote = pd.read_csv(quote_file, sep='\t', dtype=object)
    quote.head()
    quote['url'] ="https://www.bigkinds.or.kr/news/detailView.do?docId="+quote['뉴스 식별자']+"&returnCnt=1&sectionDiv=1000&indexName="
    members = ['강길부', '강병원', '강석진', '강석호', '강창일', '강효상', '강훈식', '경대수', '고용진', '곽대훈', '곽상도', '권미혁', '권성동', '권은희', '권칠승', '금태섭', '기동민', '김경진', '김경협', '김관영', '김광림', '김광수', '김규환', '김기선', '김도읍', '김동철', '김두관', '김명연', '김무성', '김민기', '김병관', '김병기', '김병욱', '김부겸', '김삼화', '김상훈', '김상희', '김석기', '김선동', '김성수', '김성식', '김성원', '김성찬', '김성태', '김성태', '김성환', '김세연', '김수민', '김순례', '김승희', '김영우', '김영주', '김영진', '김영춘', '김영호', '김용태', '김재경', '김재원', '김정우', '김정재', '김정호', '김정훈', '김종대', '김종민', '김종석', '김종회', '김종훈', '김중로', '김진태', '김진표', '김철민', '김태년', '김태흠', '김학용', '김한정', '김한표', '김해영', '김현권', '김현미', '김현아', '나경원', '남인순', '노웅래', '도종환', '맹성규', '문진국', '문희상', '민경욱', '민병두', '민홍철', '박경미', '박광온', '박대출', '박덕흠', '박맹우', '박명재', '박범계', '박병석', '박선숙', '박성중', '박순자', '박영선', '박완수', '박완주', '박용진', '박인숙', '박재호', '박정', '박주민', '박주선', '박주현', '박지원', '박찬대', '박홍근', '백승주', '백재현', '백혜련', '변재일', '서삼석', '서영교', '서청원', '서형수', '설훈', '성일종', '소병훈', '손금주', '손혜원', '송갑석', '송기헌', '송석준', '송언석', '송영길', '송옥주', '송희경', '신경민', '신동근', '신보라', '신상진', '신용현', '신창현', '심기준', '심상정', '심재권', '심재철', '안규백', '안민석', '안상수', '안호영', '어기구', '엄용수', '여상규', '염동열', '오신환', '오영훈', '오제세', '우상호', '우원식', '원유철', '원혜영', '위성곤', '유기준', '유동수', '유민봉', '유성엽', '유승민', '유승희', '유은혜', '유의동', '유재중', '윤관석', '윤상직', '윤상현', '윤소하', '윤영석', '윤영일', '윤일규', '윤재옥', '윤종필', '윤준호', '윤한홍', '윤호중', '윤후덕', '이개호', '이군현', '이규희', '이동섭', '이만희', '이명수', '이상돈', '이상민', '이상헌', '이석현', '이수혁', '이양수', '이언주', '이완영', '이용득', '이용주', '이용호', '이우현', '이원욱', '이은권', '이은재', '이인영', '이장우', '이재정', '이정미', '이정현', '이종걸', '이종구', '이종명', '이종배', '이주영', '이진복', '이찬열', '이채익', '이철규', '이철희', '이춘석', '이태규', '이학영', '이학재', '이해찬', '이헌승', '이현재', '이혜훈', '이후삼', '이훈', '인재근', '임이자', '임재훈', '임종성', '장병완', '장석춘', '장정숙', '장제원', '전재수', '전해철', '전현희', '전혜숙', '전희경', '정갑윤', '정동영', '정병국', '정성호', '정세균', '정양석', '정용기', '정우택', '정운천', '정유섭', '정인화', '정재호', '정종섭', '정진석', '정춘숙', '정태옥', '제윤경', '조경태', '조배숙', '조승래', '조원진', '조응천', '조정식', '조훈현', '주광덕', '주승용', '주호영', '지상욱', '진선미', '진영', '채이배', '천정배', '최경환', '최경환', '최교일', '최도자', '최연혜', '최운열', '최인호', '최재성', '추경호', '추미애', '추혜선', '표창원', '하태경', '한선교', '한정애', '함진규', '홍문종', '홍문표', '홍영표', '홍의락', '홍익표', '홍일표', '홍철호', '황영철', '황주홍', '황희']

    members2 = []  # 박영 선 case
    members3 = []  # 박 영선 case

    for m in members:
        if len(m) == 3:
            members2.append(m[0:2] + ' ' + m[2])
            members3.append(m[0:1] + ' ' + m[1:3])
        else:
            members2.append(m)
            members3.append(m)

    quote['정보원_추출'] = quote['정보원'].apply(extract_name)
    idx_gt_3 = quote['정보원_추출'].str.len() >= 3; idx_gt_3
    idx_lt_2 = quote['정보원_추출'].str.len() <= 2; idx_lt_2

    recognized = []

    for i, row in quote.iterrows():
        value = row['정보원_추출']
        flag = False
        recognized_name = ''
        for m in members:
            if m in value:
                recognized.append(True)
                flag = True
                recognized_name = m
                break
        if not flag:
            for m2 in members2:
                if m2 in value:
                    recognized.append(True)
                    flag = True
                    recognized_name = m
                    break
        if not flag:
            for m3 in members3:
                if m3 in value:
                    recognized.append(True)
                    flag = True
                    recognized_name = m
                    break
        if flag:
            quote.at[i, '정보원_추출2'] = recognized_name
        else:
            recognized.append(False)

    idx_recognized = pd.Series(recognized)
    idx_unknown = ~idx_recognized
    idx_len_1 = quote['정보원_추출'].str.len() == 1

    idx_error = []
    status_error = []
    requests_error = []

    for i, row in quote.loc[idx_len_1, ['뉴스 식별자', '정보원_추출']].iterrows():
    #     if i == 14:
    #         break
        news_id = row['뉴스 식별자']
        url = f'https://www.bigkinds.or.kr/news/detailView.do?docId={news_id}&returnCnt=1&sectionDiv=1000&indexName='

        try:
            response = requests.get(url, timeout=3, verify=False)

        except ReadTimeout:
            requests_error.append(i)
            continue
        except ContentDecodingError:
            requests_error.append(i)
            continue
        except TooManyRedirects:
            requests_error.append(i)
            continue

        if str(response.status_code)[0] == '4':
            status_error.append(i)
        people = response.json()['detail']['TMS_NE_PERSON']

        try:
            first_character = row['정보원_추출'][0]
        except IndexError as e:
            idx_error.append(i)
            continue

        people_list = list(filter(lambda x: filter_refer(x, first_character), people.split('\n')))
        people_only_legislator = [p for p in people_list if p in members]

        if len(people_only_legislator) == 1:
            result = people_only_legislator[0]
        else:
            result = ''

        quote.at[i, '정보원_추출2'] = result

    quote['정보원_추출2'] = quote['정보원_추출2'].fillna('')
    idx_not_empty = quote['정보원_추출2'] != ''
    idx_empty = ~idx_not_empty
    quote = quote.rename(columns={'정보원_추출2': '국회의원'})
    quote.columns

    with MyMongo() as db:
        db.delete_and_insert_df('audit_quote', collection_name, quote.loc[idx_not_empty])

    print(requests_error)
    print(quote.loc[idx_empty]['정보원'].tolist())

