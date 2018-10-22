from db.mongo import MyMongo

with MyMongo() as db:
    market = db.get_df_from_table('market', 'traditional')

# print(cemetry.columns)
# print(enshrinement.columns)
# print(natural.columns)
a = len(market)
print(a)

market.to_csv('data_/전국_전통시장.tsv', sep='\t')
