from db.mongo import MyMongo

with MyMongo() as db:
    org = db.get_df_from_table('parking', 'organization')
    edu = db.get_df_from_table('parking', 'education')

# print(cemetry.columns)
# print(enshrinement.columns)
# print(natural.columns)
a = len(org)
b = len(edu)
print(a)
print(b)

org['타입'] = '자치단체'
edu['타입'] = '교육청'

parking = org.append(edu)

print(len(parking))
print(a + b)

parking.to_csv('data_/전국_개방주차장.tsv', sep='\t')
