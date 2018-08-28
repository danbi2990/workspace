# %%
from db.mongo import MyMongo

# %%
with MyMongo() as db:
    main_rollbook = db.get_df_from_table('assembly', 'watch_main_meeting_rollbook')

main_rollbook

# %%
leehaechan = main_rollbook.loc[main_rollbook['이름']=='이해찬']
leehaechan

# %%
leehaechan['출석여부'].value_counts()

# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%







