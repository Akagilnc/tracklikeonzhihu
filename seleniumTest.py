# -*- coding: utf-8 -*-
from selenium import webdriver
import time, tools
class GetInfoFromZhihu:
    from tools import Tools

    tools = Tools()
    driver = tools.init_web_driver()

    driver = tools.login(driver=driver)

    driver = tools.click_more(driver=driver)

    titlelist = driver.find_elements_by_css_selector('#zh-profile-activity-page-list > div')
    # zh-profile-activity-page-list > div:nth-child(1)
    # zh-profile-activity-page-list > div:nth-child(17) > div
    # titlelist = driver.find_elements_by_css_selector('#zh-profile-activity-page-list > div:nth-child(1) > div.zm-profile-section-main.zm-profile-section-activity-main.zm-profile-activity-page-item-main')
    print titlelist
    resultlist = []
    for elem in titlelist:

        print '++++' + elem.get_attribute('outerHTML').encode('utf-8').strip() + "++++++"
        elemHTML = elem.get_attribute('outerHTML').encode('utf-8').strip()

        # zh-profile-activity-page-list > div:nth-child(5)
        actionType = tools.found_action_type(elemHTML=elemHTML)

        context = tools.get_context(elem)
        result = [actionType, context]
        resultlist.append(result)

    tools.write_to_file(resultlist)
    # print result + '\n\n\n\n\n\n\n'
    # source_code = driver.page_source
    driver.close()
