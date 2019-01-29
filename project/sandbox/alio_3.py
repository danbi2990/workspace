import re

import pandas as pd

from lib.scrape import get_soup_from_url

url = 'http://www.alio.go.kr/managementItem.do'

soup = get_soup_from_url(url)

all_a = soup.select('.left a')
print(all_a)

org_name_and_code = {a.text: re.search(r'C\d\d\d\d', str(a)).group(0) for a in all_a}
print(org_name_and_code)

# print([re.search(r'C\d\d\d\d', str(a)).group(0) for a in all_a])
