import re

from lib.scrape import get_soup_from_url
from db.mongo import MyMongo

# with open("sample/main_meeting.html") as f:
#     content = f.read()

url = 'http://watch.peoplepower21.org/Session'

# soup = bs(content, "html.parser")
soup = get_soup_from_url(url)

meetings = soup.find("select", id="meeting")
meeting_info = meetings.find_all("option", value=re.compile(r"[\d]+"))

# header = ["회의\tid\n"]

with MyMongo() as db:
    meeting_already_exists = db.get_df_from_table('assembly', 'watch_main_meeting')

try:
    ids_already_exists = set(meeting_already_exists['id'])
except KeyError as e:
    ids_already_exists = set()

meeting_fetched = [
        {'main_meeting': meeting.string, 'id': meeting['value'], 'rollbook_fetched': False}
        for meeting in meeting_info if meeting['value'] not in ids_already_exists]

with MyMongo() as db:
    db.update_one_bulk('assembly', 'watch_main_meeting', meeting_fetched, 'id')
