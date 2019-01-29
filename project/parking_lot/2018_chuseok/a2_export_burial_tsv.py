from db.mongo import MyMongo

with MyMongo() as db:
    cemetry = db.get_df_from_table('burial', 'cemetry')
    enshrinement = db.get_df_from_table('burial', 'enshrinement')
    natural = db.get_df_from_table('burial', 'natural_burying')

# print(cemetry.columns)
# print(enshrinement.columns)
# print(natural.columns)
a = len(cemetry)
b = len(enshrinement)
c = len(natural)
print(a)
print(b)
print(c)

cemetry['타입'] = '묘지'
enshrinement['타입'] = '봉안'
natural['타입'] = '자연'

tmp = cemetry.append(enshrinement)
burial = tmp.append(natural)

print(len(burial))
print(a + b + c)
burial.to_csv('data_/전국장사시설.tsv', sep='\t')
