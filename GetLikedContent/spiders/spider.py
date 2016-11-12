# -*- coding: utf-8 -*-
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import scrapy
import logging
import seleniumTest
import lxml
import scrapy.selector


class QuotesSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ['www.zhihu.com']
    start_url = "https://www.zhihu.com/people/xiao-hui-30-76"

    def start_requests(self):
        urls = [
            'https://www.zhihu.com/people/xiao-hui-30-76',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        html = (open('test.html', 'r')).read()
        HtmlResponse.replace(html, response)
        titlelist = response.css('div.zm-profile-section-main a.post-link::text').extract()
        linklist = response.css('div.zm-profile-section-main a.post-link::attr(href)').extract()
        for title in response.css('div.zm-profile-section-main a.question_link::text').extract():
            logging.info(title)
            titlelist.append(title)
        for link in response.css('div.zm-profile-section-main a.question_link::attr(href)').extract():
            linklist.append(link)
        contentlist = response.css('div.post-content textarea.content::text').extract()
        filename = 'zhihu-%s.html' % page
        with open(filename, 'wb') as f:
            for i in xrange(len(titlelist)):
                #logging.info(titlelist[i])
                f.write('<b>' + titlelist[i].encode('utf-8').strip() + '<b><br>' + '\n' + linklist[i].encode('utf-8').strip() + '<br>\n'
                        #+ contentlist[i].encode('utf-8').strip()
                        + '\n\n')
        self.log('Saved file %s' % filename)

    @staticmethod
    def get_information(url):
        driver = webdriver.Chrome()
        driver.accept_untrusted_certs = True
        #driver.get("https://www.zhihu.com/people/xiao-hui-30-76")
        driver.get(url)
        driver.find_element_by_class_name("switch-to-login").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath('''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[1]/input''')
        # elem.clear()
        elem.send_keys("akagilnc@gmail.com")
        elem = driver.find_element_by_xpath('''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[2]/input''')
        # elem.clear()
        elem.send_keys("091128aa")
        elem = driver.find_elements_by_xpath('''//*[@id="captcha"]''')
        elem = elem[1]
        captcha = str(raw_input("captcha"))
        elem.send_keys(captcha)
        driver.find_element_by_xpath('''//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[4]/input''').click()
        # assert "Python" in driver.title
        for i in xrange(2):
            time.sleep(7)
            elem = driver.find_element_by_class_name("zu-button-more").click()
            print "click done %d" % i

        # assert "No results found." not in driver.page_source

        # print result + '\n\n\n\n\n\n\n'
        source_code = driver.page_source

        return source_code
