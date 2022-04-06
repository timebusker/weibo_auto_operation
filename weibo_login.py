from selenium import webdriver
import time
import json
browser = webdriver.Edge()

browser.get('https://passport.weibo.cn/signin/login')

# 登录微博
def log_csdn(browser):
  with open('微博_cookies', 'r', encoding='utf8') as file:
    listCookies = json.loads(file.read())
  # 往browser里添加cookies
  for cookie in listCookies:
    cookie_dict = {
      'domain': '.weibo.cn',
      'name': cookie.get('name'),
      'value': cookie.get('value'),
      "expires": '',
      'path': '/',
      'httpOnly': False,
      'HostOnly': False,
      'Secure': False
    }
    browser.add_cookie(cookie_dict)
  time.sleep(3)
  browser.refresh() # 刷新网页,cookies才成功

def weibo_login(username, password):
     # 打开微博登录页
     browser.get('https://passport.weibo.cn/signin/login')
     browser.implicitly_wait(5)
     time.sleep(10)
     # 填写登录信息：用户名、密码
     browser.find_element_by_id("loginName").send_keys(username)
     browser.find_element_by_id("loginPassword").send_keys(password)
     time.sleep(20)
     # 点击登录
     browser.find_element_by_id("loginAction").click()
     time.sleep(60)

     dictCookies = browser.get_cookies() # 获取list的cookies
     jsonCookies = json.dumps(dictCookies) # 转换成字符串保存
     with open('微博_cookies', 'w') as file:
          file.write(jsonCookies)
     print('cookies保存成功！')

     # 开始微博评论
     browser.get(weibo_url)
     browser.implicitly_wait(5)
     content_textarea = browser.find_element_by_css_selector("textarea.W_input").clear()
     content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
     time.sleep(20)
     comment_button = browser.find_element_by_css_selector(".W_btn_a").click()
     time.sleep(10)


# 设置用户名、密码
username = '15198874943'
password = "timebusker@123"
weibo_url = 'https://weibo.com/6148104254/LhK3gjtn2'
content = 'Gook Luck! 好运已上路！'
# weibo_login(username, password)
log_csdn(browser)
