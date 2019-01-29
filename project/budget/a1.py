from collections import defaultdict
from collections import Counter

from konlpy.tag import Mecab, Kkma
import pandas as pd

directory = '/Users/jake/OneDrive - leverage innovative users/Documents/예산/'
file = '2019년_경제정책방향.txt'

with open(directory + file, 'r') as f:
    raw = f.read()

mecab = Mecab()
list_of_pos = mecab.pos(raw)

dict_of_pos = defaultdict(list)

for p in list_of_pos:
    dict_of_pos[p[1]].append(p[0])

# print(len(dict_of_pos.keys()))
# print(dict_of_pos['NNG'])
# print(dict_of_pos['NNG'])

counters = {}

for tag, words in dict_of_pos.items():
    cnter = Counter(words)
    counters[tag] = cnter

# print(len(counters.keys()))
print(counters['NNG'])

# df = pd.DataFrame.from_dict(counters)
# print(df[['NNG','NNP']].head(5))

# nng_counter = Counter(dict_of_pos['NNG'])
# nnp_counter = Counter(dict_of_pos['NNP'])
# vv_counter = Counter(dict_of_pos['VV'])
# print(nng_counter.most_common())

"""
NNG 일반 명사
NNP 고유 명사
NNB 의존 명사
NNBC    단위를 나타내는 명사
NR  수사
NP  대명사

VV  동사

VA  형용사
VX  보조 용언
VCP 긍정 지정사
VCN 부정 지정사

MM  관형사
MAG 일반 부사
MAJ 접속 부사
"""
