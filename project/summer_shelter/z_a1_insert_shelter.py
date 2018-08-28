import pandas as pd

from db.mongo_connection import MyMongo

shelter = pd.read_csv('shelter_from_safekorea.tsv', sep='\t')
dct = shelter.to_dict(orient='records')
# print(dct)

with MyMongo() as db:
    sht_obj = db.get_table_obj('hot_summer', 'shelter')
    sht_obj.insert_many(dct)


