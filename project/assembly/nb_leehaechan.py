# %%
from db.mongo import MyMongo

# %%
with MyMongo() as db:
    main_rollbook = db.get_df_from_table('assembly', 'watch_main_meeting_rollbook')
    confer = db.get_df_from_table('assembly', 'watch_conference')
    rollbook = db.get_df_from_table('assembly', 'watch_rollbook')
    watch_member = db.get_df_from_table('assembly', 'watch_member')
    bill_repr = db.get_df_from_table('assembly', 'bill_repr', {'coactKind': '대표발의'})

# %%
refill = ['김성환', '최재성', '윤준호', '맹성규', '송갑석', '이상헌', '이후삼', '이규희', '윤일규', '서삼석', '김정호']
# %%
# bill_repr.columns
len(bill_repr)

# %%
bill = bill_repr.merge(watch_member[['hjNm', '정당']], on='hjNm', how='left')

# %%
minju_bill = bill.loc[bill['정당']=='더불어민주당']; minju_bill

# %%
minju_bill_count = minju_bill.groupby('hjNm').agg({'billId': 'count'}); minju_bill_count
minju_bill_count = minju_bill_count.rename(columns={'billId': '합계'}); minju_bill_count
minju_bill_count.reset_index(inplace=True); minju_bill_count


# minju_bill_count = minju_bill_count.merge(watch_member[['hjNm', 'empNm']], on='hjNm', how='left'); minju_bill_count
# minju_bill_count.loc[minju_bill_count['empNm']=='송갑석']


# %%
# pvt_bill_stage = minju_bill.pivot_table(columns='procStageCd', index='hjNm', values='_id', aggfunc='count'); pvt_bill_stage
bill_repr.loc[bill_repr['billNo']=='2014894']






# %%
pvt_bill_raw = minju_bill.pivot_table(columns='generalResult', index='hjNm', values='_id', aggfunc='count'); pvt_bill_raw
pvt_bill = minju_bill_count.merge(pvt_bill_raw, on='hjNm', how='left'); pvt_bill
pvt_bill.fillna(0, inplace=True); pvt_bill
pvt_bill['가결'] = pvt_bill['대안반영폐기'] + pvt_bill['수정가결']\
    + pvt_bill['원안가결']; pvt_bill
pvt_bill = pvt_bill.merge(watch_member[['hjNm', 'empNm']], on='hjNm', how='left'); pvt_bill
bill_without_refill = pvt_bill.loc[~pvt_bill['empNm'].isin(refill)]; bill_without_refill

bill_without_refill.sort_values('합계', ascending=True)[:50]
# pvt_bill.sort_values('합계', ascending=True)[:50]
# pvt_bill.loc[pvt_bill['empNm']=='송갑석']
# pvt_bill.loc[pvt_bill['empNm']=='이해찬']
# bill_without_refill.to_csv('bill.tsv', sep='\t', index=False)

# %%






# %%
main = main_rollbook.drop(columns=['정당'])
main['pid'] = main['pid'].astype(str)
main = main.merge(watch_member[['seq', '정당']], left_on='pid', right_on='seq', how='left'); main

# %%
minju_main = main.loc[main['정당']=='더불어민주당']
minju_main

# %%
minju_main.columns
pvt_main = minju_main.pivot_table(columns='출석여부', index='seq', values='_id', aggfunc='count')
pvt_main.fillna(0, inplace=True); pvt_main
pvt_main['합계'] = pvt_main['결석'] + pvt_main['청가'] + pvt_main['출석'] + pvt_main['출장']; pvt_main
pvt_main['무단결석률'] = pvt_main['결석'] / pvt_main['합계'] * 100; pvt_main
pvt_main = pvt_main.merge(watch_member[['seq', 'empNm']], on='seq', how='left'); pvt_main
main_without_refill = pvt_main.loc[~pvt_main['empNm'].isin(refill)]; main_without_refill

main_without_refill.sort_values('무단결석률', ascending=False)

# main_without_refill.to_csv('main.tsv', sep='\t', index=False)





# %%
rol2 = rollbook.drop(columns=['party'])
rol2 = rol2.merge(watch_member[['seq', '정당']], on='seq', how='left')
print(len(rol2))

# %%
minju = rol2.loc[rol2['정당']=='더불어민주당']
minju
# rol_lee = minju.loc[minju['empNm']=='이해찬']
# print(len(rol_lee))

# %%
pvt_rol = minju.pivot_table(columns='attended', index='seq', values='_id', aggfunc='count')
pvt_rol.fillna(0, inplace=True); pvt_rol
pvt_rol['합계'] = pvt_rol['결석'] + pvt_rol['청가'] + pvt_rol['출석'] + pvt_rol['출장']; pvt_rol
pvt_rol['무단결석률'] = pvt_rol['결석'] / pvt_rol['합계'] * 100; pvt_rol
pvt_rol = pvt_rol.merge(watch_member[['seq', 'empNm']], on='seq', how='left'); pvt_rol
rol_without_refill = pvt_rol.loc[~pvt_rol['empNm'].isin(refill)]; rol_without_refill

rol_without_refill.sort_values('무단결석률', ascending=False)

rol_without_refill.to_csv('rol.tsv', sep='\t', index=False)

# pvt_rol.sort_values('무단결석률', ascending=False)

# 이해찬: 상임위회의 무단결석률 37.68%로 더민주당 내에서 3위

# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%







