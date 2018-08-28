import pandas as pd

from db.mongo import MyMongo
from lib.scrape import get_soup_from_url

with MyMongo() as db:
    df = db.get_df_from_table('kindergarten', 'violator')

for idx, srs in df.iterrows():
    # if idx == 2:
    #     break
    url = srs['detail_url']
    soup = get_soup_from_url(url)
    table = soup.find('table', class_='table_childcare2')
    tds = table.find_all('td', colspan='5')
    violation, result = (td.get_text().strip() for td in tds)
    df.at[idx, 'violation'] = violation
    df.at[idx, 'result'] = result

with MyMongo() as db:
    db.delete_and_insert_df('kindergarten', 'violator', df)
