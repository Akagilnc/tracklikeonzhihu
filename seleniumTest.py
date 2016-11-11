from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.accept_untrusted_certs = True
driver.get("https://www.zhihu.com/people/xiao-hui-30-76")
driver.find_element_by_class_name("switch-to-login").click()
time.sleep(1)
elem = driver.find_element_by_name("account")
elem.clear()
elem.send_keys("akagilnc@gmail.com")
elem = driver.find_element_by_xpath('''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[2]/input''')
#elem.clear()
elem.send_keys("091128aa")
elem = driver.find_elements_by_xpath('''//*[@id="captcha"]''')
elem = elem[1]
captcha = str(raw_input("captcha"))
elem.send_keys(captcha)
driver.find_element_by_xpath('''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[4]/input''').click()
#assert "Python" in driver.title
for i in xrange(1):
    elem = driver.find_element_by_class_name("zu-button-more").click()
    print "click done %d" % i
    time.sleep(5)

#assert "No results found." not in driver.page_source
#result = str(driver.page_source().encode('utf-8').strip())
#print result + '\n\n\n\n\n\n\n'
print driver