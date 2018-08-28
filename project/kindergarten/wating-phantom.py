from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)

driver.get("http://www.childcare.go.kr/cpms/enterwait/EntWaitReqstNsrChoiseSIL.jsp")
driver.find_element_by_id('ctprvn').select_by_visible_text('서울특별시')
driver.find_element_by_id('signgu').select_by_visible_text('종로구')
driver.find_element_by_link_text('검색').click()
print(driver.text)

driver.quit()
