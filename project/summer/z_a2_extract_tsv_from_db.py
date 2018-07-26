import pandas as pd
from db.mongo_connection import MyMongo
pd.set_option('display.expand_frame_repr', False)

with MyMongo() as db:
    obj = db.get_table_obj('hot_summer', 'shelter')

filtered = list(obj.find({'filter2': {'$exists': True}}))
# filtered = list(obj.find({'lat': {'$ne': float('nan')}}))

# print(len(filtered))
# print(filtered)

df = pd.DataFrame(filtered)
df = df.drop(columns=['_id'])
df.to_csv('shelter_from_mongo2.tsv', sep='\t', index=False)
print(df)
