import pandas as pd
from db.mongo import MyMongo

cemetry = pd.read_csv('data_/burial_cemetry.tsv', sep='\t')
enshrine = pd.read_csv('data_/burial_enshrinement.tsv', sep='\t')
natural = pd.read_csv('data_/burial_natural.tsv', sep='\t')

# print(cemetry)

with MyMongo() as db:
    db.delete_and_insert_df('burial', 'cemetry', cemetry)
    db.delete_and_insert_df('burial', 'enshrinement', enshrine)
    db.delete_and_insert_df('burial', 'natural_burying', natural)
