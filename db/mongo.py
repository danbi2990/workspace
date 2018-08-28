import socket
from pymongo import MongoClient, UpdateOne
import pandas as pd

from lib.util import print_bulk_result


class MyMongo:
    def __init__(self):
        con_str = self.get_connection_string()
        self.client = MongoClient(con_str)
        print('<--Mongo Connected.')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.client.close()
        print('Mongo Connection Closed.-->')

    def update_one_bulk(self, schema, collection, docs, *key):
        obj = self.get_table_obj(schema, collection)
        queries = []
        for doc in docs:
            key_made = {k: doc[k] for k in key}
            queries.append(UpdateOne(key_made,
                           {'$set': doc}, upsert=True))

        if queries:
            result = obj.bulk_write(queries)
            print_bulk_result(result)
        else:
            print('Record Not Found.')

    def delete_and_insert_df(self, schema, collection, df):
        docs = df.to_dict(orient='records')
        self.delete_and_insert(schema, collection, docs)

    def find(self, schema, collection, filter={}):
        obj = self.get_table_obj(schema, collection)
        return obj.find(filter)

    def delete_and_insert(self, schema, collection, docs, filter={}):
        del_result = self.delete_many(schema, collection, filter)
        print(f'Deleted rows: {del_result.deleted_count}')
        ins_result = self.insert_many(schema, collection, docs)
        print(f'Inserted rows: {len(ins_result.inserted_ids)}')

    def delete_many(self, schema, collection, filter={}):
        obj = self.get_table_obj(schema, collection)
        print(filter)
        return obj.delete_many(filter)

    def insert_many(self, schema, collection, docs):
        obj = self.get_table_obj(schema, collection)
        return obj.insert_many(docs)

    def get_table_obj(self, schema, table):
        return getattr(getattr(self.client, schema), table)

    def archive_complement_and_dump_new(self, prev, new, on, schema,
                                        main_table, archive_table):
        if new.empty:
            raise ValueError('New Data Not Found.')

        main = self.get_table_obj(schema, main_table)
        if not prev.empty:
            intersection = pd.merge(prev, new, how='left', on=on)
            complement = prev[intersection.isnull().any(axis=1)]
            # union = pd.merge(prev, new, how='outer', on='num')
            if not complement.empty:
                arch = self.get_table_obj(schema, archive_table)
                arch.insert_many(complement.to_dict(orient='records'))
                print(f'Complement Data Archived in \'{archive_table}\'.')

            main.delete_many({})
            print(f'Old Data Removed from \'{main_table}\'.')

        main.insert_many(new.to_dict(orient='records'))
        print(f'New Data Dumped to \'{main_table}\'.')

    def get_df_from_table(self, schema, table, args={}):
        tb_obj = self.get_table_obj(schema, table)
        return pd.DataFrame(list(tb_obj.find(args)))

    def get_connection_string(self):
        hname = socket.gethostname()
        con_str = ''
        if hname == 'ideapad':
            file_path = '/home/jake/Private/local_mongo_connection.txt'
        elif hname == 'danbi-mac.local':
            file_path = '/Users/jake/Private/mongo_connection_to_ideapad.txt'

        with open(file_path) as f:
            con_str = f.read()
        return con_str.strip()
