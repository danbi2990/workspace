import pandas as pd
from db.mongo import MyMongo

org = pd.read_csv('data_/parking_org.tsv', sep='\t')
edu = pd.read_csv('data_/parking_edu.tsv', sep='\t')

# print(org.columns)

with MyMongo() as db:
    db.delete_and_insert_df('parking', 'organization', org)
    db.delete_and_insert_df('parking', 'education', edu)
