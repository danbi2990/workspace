import requests

from lib.scrape import post_soup_from_url

url = 'http://www.childcare.go.kr/cpms/enterwait/EntWaitReqstNsrChoiseSIL.jsp'
data = {
    # 'alltype': 'A',
    # 'chilinnb': '',
    # 'crname': '',
    # 'crpub': '',
    # 'crspec': '',
    # 'crtype': '',
    'ctprvn': '11000',
    # 'dong': '1111065000',
    'flag': 'NsrSIL',
    'offset': '0',
    'programId': 'P001PG00010002',
    # 'road': '%EB%8C%80%ED%95%99%EB%A1%9C',
    # 'sgubun': '',
    'signgu': '11110',
}
# cookies = {
#    'cwlogger_temp_cookie': '',
#    'JSESSONID_CIS': 'CAAvcY9ctOg5IZrmmyDE8ECRWjszFE4kdXFiqQaHeFEvx9jH0KeQQuH3fqL1iadq.mwdawas01_servlet_pcms',
#    'JSESSONID_CMS': 'o6wcKwuZexKD7ahSmuB0az16mYTu63TCdUIHJcvXMj2Q4a2Q0yVBDhhOgHO5uZ3A.mwdarws02_servlet_cms',
#    'npPfsHost': '127.0.0.1',
#    'npPfsPort': '14440',
#    'uid': 'danbi2990',
#    'WMONID': 'MoCysH-JZQI',
# }
r = requests.post(url, data, verify=False)
print(r.text)
