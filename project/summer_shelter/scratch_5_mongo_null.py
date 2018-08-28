from pprint import pprint

from db.mongo import MyMongo

with MyMongo() as db:
    res = db.find('summer', 'shelter')
    shelter = list(res)

# pprint(shelter[:10])
for doc in shelter:
    if doc['도로명주소'] == '':
        print(doc)
