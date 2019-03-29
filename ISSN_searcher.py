from selenium import webdriver
from bs4 import BeautifulSoup

f=open('SCI_20190329/p1.txt')
dat = f.read().split('\n')
f.close()

# open webpage and accept the terms of use
driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('http://cassi.cas.org/includes/splash.jsp?placeValuesBefore')
driver.implicitly_wait(10)

driver.find_elements_by_xpath('//*[@id="page_content"]/div/input')[0].click()

# search cyvcle

ISSNlist = []
for ISSN in dat:

    driver.find_element_by_xpath('//select[@name="searchIn"]/option[@value="issns"]').click()
    driver.find_element_by_name('searchFor').send_keys(ISSN)
    driver.find_element_by_name('exactMatch').click()
    driver.find_element_by_xpath('//input[@value="Search"]').send_keys(u'\ue007') # enter key

    if len(driver.find_elements_by_id('publication')):
        table = driver.find_element_by_id('publication').get_attribute('innerHTML')
        soup = BeautifulSoup(table,'html.parser')
        names = soup.find_all('td',attrs={'class':'name'}) 
        vals = soup.find_all('td',attrs={'class':'value'})
        templist = []
        for k in range(len(vals)):
            templist.append(names[k].text + ': ' + vals[k].text)
        ISSNlist.append('\t'.join(templist))

        driver.get('http://cassi.cas.org/search.jsp')
        driver.implicitly_wait(2)
    else:
        driver.get('http://cassi.cas.org/search.jsp')
        driver.implicitly_wait(2)

    

f2 = open('SCI_20190329/p1info.txt','w')
f2.write('\n'.join(ISSNlist))
f2.close()