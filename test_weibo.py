from selenium import webdriver
import time
import sys
import json
import re
browser = webdriver.Edge()
script="window.scrollTo(0,document.body.scrollHeight)"

# 添加指定的用户
def add_follow(uid):
    browser.get('https://weibo.com/u/'+str(uid))
    time.sleep(30)
    for k in range(30):
        browser.execute_script(script)
        time.sleep(10)
    hrefs = browser.find_elements_by_css_selector("a[href ^='https://weibo.com/"+str(uid)+"/']")
    time.sleep(1)
    index = 0
    for href in hrefs:
        index = index + 1
        url=href.get_attribute('href')
        print("=====>",url,'____',index)

# 小散爱涨停 UID
uid = '6148104254' 
add_follow(uid)