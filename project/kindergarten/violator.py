import pandas as pd

from lib.scrape import post_soup_from_url
from db.mongo import MyMongo


def create_url(name_and_url):
    url_base = 'http://info.childcare.go.kr/info/cfvp'
    return url_base + name_and_url.split('.', 1)[1]


url = 'http://info.childcare.go.kr/info/cfvp/VioltactorSlL.jsp'
data = {
    'total': '69',
    'offset': '1',
    'limit': '70',
}
soup = post_soup_from_url(url, data)
table = soup.find('table', class_='table_childcare')
data = [[''.join(td.stripped_strings)+td.a['href'] if td.find('a') else
         ''.join(td.stripped_strings)
         for td in row.find_all('td')]
        for row in table.find_all('tr')]
header = [[''.join(th.stripped_strings)
           for th in thead.find_all('th')]
          for thead in table.find_all('thead')]
df = pd.DataFrame(data[1:], columns=header[0])
df['detail_url'] = df.apply(lambda row: create_url(row['이름']), axis=1)
df['이름'] = df.apply(lambda row: row['이름'].split('.')[0], axis=1)

with MyMongo() as db:
    db.delete_and_insert_df('kindergarten', 'violator', df)
