from db.mongo import MyMongo

with MyMongo() as db:
    cvs = db.get_df_from_table('cvs', 'cvs')



