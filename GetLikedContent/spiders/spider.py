# -*- coding: utf-8 -*-

import scrapy
import logging


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


        def parse_more(self, response):
            pass