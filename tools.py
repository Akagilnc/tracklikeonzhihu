# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Tools:
    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome()


    def init_web_driver(self):

        self.driver.accept_untrusted_certs = True
        link = str(raw_input("link: "))
        # driver.get("https://www.zhihu.com/people/xiao-hui-30-76")
        self.driver.get(link)
        return self.driver

    def login(self, driver):
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
        while len(driver.find_elements_by_xpath('''//*[@id="captcha"]''')) > 0 and EC.element_to_be_clickable(
                driver.find_elements_by_xpath('''//*[@id="captcha"]''')[1]) and elem is not None:

            if 'is-ignoreValidation' not in (driver.find_elements_by_xpath('''//*[@id="captcha"]'''))[1].get_attribute(
                    'class'):
                captcha = str(raw_input("captcha: "))
                elem.click()
                elem.clear()
                elem.send_keys(captcha)
                elem = driver.find_element_by_xpath(
                    '''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[4]/input''')
                elem.click()
                time.sleep(2)
            else:
                elem = driver.find_element_by_xpath(
                    '''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[4]/input''')
                elem.click()
                time.sleep(2)
                break

        time.sleep(2)
        return driver

    def click_more(self, driver):
        i = 0
        while True:

            try:
                driver.find_element_by_class_name("zu-button-more").click()
                i = i + 1
                print "click done %d" % i
                time.sleep(5)
            except NoSuchElementException, e:
                break

        return driver

    def found_action_type(self, elemHTML):
        if elemHTML is not None:
            if 'member_voteup_answer' in elemHTML:
                action_type = 'like answer'
            elif 'member_voteup_article' in elemHTML:
                action_type = 'like article'
            elif 'member_follow_question' in elemHTML:
                action_type = 'follow question'
            elif 'member_collect_article' in elemHTML:
                action_type = 'favorite article'
            elif 'member_collect_answer' in elemHTML:
                action_type = 'favorite answer'
            elif 'member_follow_column' in elemHTML:
                action_type = 'follow column'
            else:
                action_type = 'unknown'
        else:
            action_type = "failed"
        return action_type

    def get_context(self, elem):
        if 'post-link' in elem.get_attribute('innerHTML'):
            elem = elem.find_element_by_class_name('post-link')
        elif 'question_link' in elem.get_attribute('innerHTML'):
            elem = elem.find_element_by_class_name('question_link')
        elif 'column_link' in elem.get_attribute('innerHTML'):
            elem = elem.find_element_by_class_name('column_link')
        else:
            elem = elem.find_element_by_xpath('//*[@id="zh-profile-activity-page-list"]/div[1]/div/a')
        print elem
        title = elem.get_attribute('innerHTML').encode('utf-8').strip()
        print title
        url = elem.get_attribute('href').encode('utf-8').strip()
        print url
        return {"title": title, "url": url}

    def write_to_file(self, resultlist):
        file = open('test.html', 'wb')
        for result in resultlist:
            file.write(result[0] + '\n' + result[1].get('title') + '\n' + result[1].get('url') + '\n\n')
