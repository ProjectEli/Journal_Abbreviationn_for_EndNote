from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('http://cassi.cas.org/includes/splash.jsp?placeValuesBefore')
driver.implicitly_wait(10)

driver.find_elements_by_xpath('//*[@id="page_content"]/div/input')[0].click()

driver.find_element_by_name('searchFor').send_keys('nat. commun.')
driver.find_element_by_name('exactMatch').click()
driver.find_element_by_xpath('//input[@value="Search"]').click()

table = driver.find_element_by_id('publication').get_attribute('innerHTML')
soup = BeautifulSoup(table,'html.parser')
vals = soup.find_all('td',attrs={'class':'value'})
for val in vals:
    print(val.text)