import re
from io import StringIO
from bs4 import BeautifulSoup as bs
import pandas as pd

from db.mongo import MyMongo
from lib.scrape import get_soup_from_url


def save_rollbook(mid, title, c1):
    body = "mid\t회차\tpid\t이름\t정당\t출석여부\n"
    c1_str = str(c1)
    c1_l = c1_str.split("attend_div")
    for c1 in c1_l[1:]:
        c1_t = bs(c1, "html.parser")
        c1_type_raw = c1_t.find("td").previous_element.previous_element
        c1_type = re.search(r"\w+", c1_type_raw)[0]
        c1_s = str(c1_t)
        pt_l = c1_s.split('<span style="color: Array; font-size: 110%;">')
        for pt in pt_l[1:]:
            pt_t = bs(pt, "html.parser")
            pt_name = re.search(r"\w+", pt_t.find("strong").string)[0]
            per_l = pt_t.find_all("a")
            line = ""
            for per in per_l:
                p_id = re.search(r"\d+", per['href'])[0]
                p_name = per.string.strip()
                line += f"{mid}\t{title}\t{p_id}\t{p_name}\t{pt_name}\t{c1_type}\n"
            body += line
    tsv_IO = StringIO(body)
    body_df = pd.read_csv(tsv_IO, sep="\t")
    docs = body_df.to_dict(orient='record')
    with MyMongo() as db:
        db.delete_and_insert('assembly', 'watch_main_meeting_rollbook', docs, {'mid': int(mid)})


def save_main_meeting(mid, soup):
    # soup = bs(content, "html.parser")
    title = soup.find("option", selected=True)
    if title:
        title = title.string.strip()
    c1 = soup.find("div", id="collapseOne")

    save_rollbook(mid, title, c1)


with MyMongo() as db:
    main_meeting = db.get_df_from_table('assembly', 'watch_main_meeting', {'rollbook_fetched': False})

try:
    id_list = main_meeting['id'].tolist()
except KeyError as e:
    id_list = []

# print(id_list)

for mid in id_list:
    url = f"http://watch.peoplepower21.org/index.php?mid=Session&meeting_id=\
        {mid}"
    soup = get_soup_from_url(url)
    save_main_meeting(mid, soup)


"""main meeting seq info
828, 825,
18th: 590, 595, 600, 610, 615
19th: 620 ~ 828 (inclusive)
"""
