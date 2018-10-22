import pandas as pd
from db.mongo import MyMongo

market = pd.read_csv('data_/market.tsv', sep='\t')

print(market.columns)

with MyMongo() as db:
    db.delete_and_insert_df('market', 'traditional', market)
