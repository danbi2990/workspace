# from pprint import pprint
from datetime import datetime
import pandas as pd

from api.public_portal import get_df_from_url, get_df_as_per_total
from db.mongo import MyMongo

url_comm = 'http://apis.data.go.kr/9710000/BillInfoService/getCommitPeti\
tionList'
params_comm = {
    'numOfRows': 10,
    'pageNo': 1,
    # 'gbn': 'C06',
    'start_age_cd': 20,
}
new_comm = get_df_from_url(url_comm, params_comm)
time_stamp = datetime.now()
new_comm['update_on'] = time_stamp
# cur_comm_list = new_comm.loc[(new_comm['committeecode'].str[0:2] == '97'), ['committeecode', 'committeename']]
new_comm_mem = pd.DataFrame()

# print(new_comm)

for index, row in new_comm.iterrows():
    url_comm_mem = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoSe\
rvice/getCommMemberCurrStateList'
    params_comm_mem = {
        'numOfRows': 10,
        'pageNo': 1,
        'dept_cd': row['committeecode'],
    }
    comm_mem_tmp = get_df_as_per_total(url_comm_mem, params_comm_mem)
    comm_mem_tmp['committeecode'] = row['committeecode']
    comm_mem_tmp['committeename'] = row['committeename']
    comm_mem_tmp['update_on'] = time_stamp
    new_comm_mem = new_comm_mem.append(comm_mem_tmp)

with MyMongo() as db:
    mem = db.get_df_from_table('assembly', 'member')
    new_comm_mem = new_comm_mem.merge(mem[['hjNm', 'num']], how='left',
                                      on='hjNm')
    new_comm_mem = new_comm_mem[['committeename', 'empNm', 'num', 'hjNm',
                                'committeecode', 'update_on']]

    prev_comm = db.get_df_from_table('assembly', 'committee')
    db.archive_complement_and_dump_new(prev_comm, new_comm, 'committeename',
                                       'assembly', 'committee',
                                       'committee_archive')

    prev_comm_mem = db.get_df_from_table('assembly', 'committee_member')
    db.archive_complement_and_dump_new(prev_comm_mem, new_comm_mem,
                                       ['committeename', 'num'], 'assembly',
                                       'committee_member',
                                       'committee_member_archive')

'''
gbn code
1.처리의안 검색  gbn=C01
2.계류의안 검색 gbn =C02
3.본회의요청안건검색 gbn =C03
4.청원처리 검색 gbn =C04
5.청원계류 검색 gbn =C05
6.의안목록 검색 gbn=C06

bill_kind_cd
의안종류
1.헌법개정 B01
2.예산안 B02
3.결산 B03
4.법률안 B04
5.동의안 B05
6.승인안 B06
7.결의안 B07
8.건의안 B08
9.규칙안 B09
10.선출안 B10
11.중요동의 B11
12.의원징계 B12
13.의원자격심사 B13
14.윤리심사 B14
15.기타안 B15
16.기타 B16
'''
