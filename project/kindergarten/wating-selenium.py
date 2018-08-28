from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)

url = 'http://www.childcare.go.kr/cpms/enterwait/EntWaitReqstNsrChoiseSIL.jsp'

driver.get(url)
driver.find_element_by_id('ctprvn').select_by_visible_text('서울특별시')
driver.find_element_by_id('signgu').select_by_visible_text('종로구')
driver.find_element_by_link_text('검색').click()

print(driver.text)
# print(elem)

driver.quit()
