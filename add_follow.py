from selenium import webdriver
import time
import sys
import json
import re
browser = webdriver.Edge()
script="window.scrollTo(0,document.body.scrollHeight)"

browser.get('https://weibo.com/u/'+str(uid))
time.sleep(20)

# 添加指定的用户
def add_follow(uid):
    browser.execute_script(script)
    time.sleep(30)
    browser.execute_script(script)
    time.sleep(30)
    hrefs = browser.find_elements_by_css_selector("a[href ^='https://weibo.com/"+str(uid)+"/']")
    time.sleep(1)
    for href in hrefs:
        url=href.get_attribute('href')
        print("=====>",url)

# 读取json文件
def read_json(file_name, coding="utf-8"):
    file = open(file_name, "r", encoding=coding).read()
    try:
        content = json.loads(file)
    except:
        print("{} 文件格式错误 ，程序退出".format(file_name))
        sys.exit()
    return content


def CookiestoDic(str):
    result = {}
    cookies = str.split(";")
    cookies_pattern = re.compile("(.*?):(.*)")
    for cook in cookies:
        cook = cook.replace(" ", "")
        header_name = cookies_pattern.search(cook).group(1)
        header_value = (cookies_pattern.search(cook).group(2))
        result[header_name] = header_value
    return result

onfig_filename = "./config.json"
config = read_json(config_filename)
cookies_str = config["cookies"]
cookies = CookiestoDic(cookies_str)
for cookie in listCookies:
    cookie_dict = {
      'domain': '.weibo.com',
      'name': cookie.get('name'),
      'value': cookie.get('value'),
      "expires": '',
      'path': '/',
      'httpOnly': False,
      'HostOnly': False,
      'Secure': False
    }
    browser.add_cookie(cookie_dict)
    
 # 刷新网页,cookies才成功
 browser.refresh()
# 小散爱涨停 UID
uid = '6148104254' 
add_follow(uid)