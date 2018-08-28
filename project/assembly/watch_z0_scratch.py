from db.mongo import MyMongo
from lib.util import print_bulk_result

with MyMongo() as db:
    obj = db.get_table_obj('assembly', 'watch_main_meeting')
    result = obj.update_many({}, {'$set': {'rollbook_fetched': True}})
    # result = obj.update_many({}, {'$set': {'rollbook_fetched': True}})
    # print_bulk_result(result)
