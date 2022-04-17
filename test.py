# -*- coding: utf-8 -*-
# @Author: HUAWEI
# @Date:   2022-03-01 16:09:22
# @Last Modified by:   HUAWEI
# @Last Modified time: 2022-04-17 14:11:02

import selenium
import time
from selenium import webdriver

# C:\Users\HUAWEI\AppData\Local\Programs\Python\Python310

driver = webdriver.Edge()
driver.implicitly_wait(3)
script="var query=document.documentElement.scrollTop=20000"
driver.get("https://www.jiucaigongshe.com/")
# driver.execute_script(script)
element=driver.find_element_by_xpath('//a[text()="泽宇智能"]/..')
print(element)
print(element.get_attribute("class"))
time.sleep(30)