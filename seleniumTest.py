# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.accept_untrusted_certs = True
link = str(raw_input("link: "))
#driver.get("https://www.zhihu.com/people/xiao-hui-30-76")
driver.get(link)
driver.find_element_by_class_name("switch-to-login").click()
time.sleep(1)
elem = driver.find_element_by_xpath('''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[1]/input''')
# elem.clear()
account = str(raw_input("account: "))
elem.send_keys(account)
elem = driver.find_element_by_xpath('''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[2]/input''')
# elem.clear()
password = str(raw_input("password: "))
elem.send_keys(password)
elem = driver.find_elements_by_xpath('''//*[@id="captcha"]''')
elem = elem[1]
#
captcha = str(raw_input("captcha: "))
elem.clear()
elem.send_keys(captcha)
driver.find_element_by_xpath('''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[4]/input''').click()

# assert "Python" in driver.title
i = 0
while True:
    time.sleep(2)
    try:
        elem = driver.find_element_by_class_name("zu-button-more").click()
        i = i + 1
        print "click done %d" % i
        time.sleep(1)
    except NoSuchElementException, e:
        break

#elem = driver.find_element_by_id('zh-top-nav-count-wrap').click()

# assert "No results found." not in driver.page_source
titlelist = driver.find_elements_by_class_name('post-link')
file = open('test.html', 'wb')
for elem in titlelist:
    title = elem.get_attribute('innerHTML').encode('utf-8').strip()
    url = elem.get_attribute('href').encode('utf-8').strip()
    file.write(title + '\n' + url + '\n\n')

titlelist = driver.find_elements_by_class_name('question_link')
for elem in titlelist:
    title = elem.get_attribute('innerHTML').encode('utf-8').strip()
    url = elem.get_attribute('href').encode('utf-8').strip()
    file.write(title + '\n' + url + '\n\n')
# print result + '\n\n\n\n\n\n\n'
#source_code = driver.page_source


