from selenium import webdriver
import time
import random

browser = webdriver.Edge()
script="window.scrollTo(0,document.body.scrollHeight)"

# 登录微博
def weibo_login(username, password):
     # 打开微博登录页
     # browser.get('https://passport.weibo.cn/signin/login')
     browser.get('https://weibo.com/6148104254/')
     # browser.implicitly_wait(5)
     # time.sleep(10)
     # # 填写登录信息：用户名、密码
     # browser.find_element_by_id("loginName").send_keys(username)
     # browser.find_element_by_id("loginPassword").send_keys(password)
     # time.sleep(10)
     # # 点击登录
     # browser.find_element_by_id("loginAction").click()
     # time.sleep(10)
# 设置用户名、密码
# username = '15198874943'
username = ''
password = ""
weibo_login(username, password)
time.sleep(30)
browser.maximize_window()

# 小散爱涨停 UID
uid = '6148104254' 
count=0
urls=[]

# 组装评论
def get_content():
    global count
    timestr = time.strftime("%Y%m%d%H%M%S")
    emoji=''.join(random.sample(['[雪容融]','[哈哈]','[可爱]','[抓狂]','[爱你]','[色]','[笑而不语]','[嘻嘻]','[鲜花]','[许愿虎]','[挤眼]','[2022]','[凯洛伦]','[心]','[男孩儿]','[作揖]','[赞啊]','[小黄人委屈]','[小黄人高兴]','[小黄人微笑]','[哪吒开心]','[冰墩墩]','[金牌]','[谜语人]','[虎爪比心]','[互粉]','[打call]','[抱一抱]','[亲亲]','[喵喵]','[杰瑞]','[中国赞]','[坏笑]','[舔屏]','[害羞]','[哆啦A梦吃惊]','[伴我同行]','[美国队长]','[羞嗒嗒]','[给力]','[haha]','[兔子]','[赞]','[good]','[耶]','[奥特曼]','[干杯]','[拳头]','[弗莱见钱眼开]','[给你小心心]','[棒棒糖]','[好喜欢]','[佩奇]','[加油]','[飞机]'], random.randint(1,5)))
    text=''.join(random.sample(['小蔡牛逼','小蔡威武','蔡蔡女神','蔡大美女','爱你','蔡蔡','蔡大','大佬','优秀','完美','高手','厉害','100%的准确率','一起发财','简直是不可或缺！','感谢蔡神','没亏过',''], random.randint(0,1)))
    content=text+emoji
    return content

# 给指定某条微博添加内容
def add_comment(weibo_url):
    browser.get(weibo_url)
    browser.implicitly_wait(2)
    time.sleep(10)
    # 点赞
    buttons = browser.find_element_by_xpath('//span[@class="woo-like-count"]/../..')
    for button in buttons:
        button.click()
        time.sleep(2)
    # 评论的评论
    browser.refresh()
    time.sleep(10)
    content_is=browser.find_elements_by_css_selector("i[class='woo-font woo-font--comment']")
    for content_i in content_is:
        content_i.click()
        time.sleep(2)
        content = get_content()
        browser.find_element_by_css_selector("textarea[placeholder='发布你的回复']").clear()
        browser.find_element_by_css_selector("textarea[placeholder='发布你的回复']").send_keys(content)
        time.sleep(2)
        browser.find_element_by_xpath('//span[text()="回复" and @class="woo-button-content"]/../..').click()
        time.sleep(200)
    # 本博评论
    browser.refresh()
    time.sleep(60)
    content = get_content()
    browser.find_element_by_css_selector("textarea[placeholder='发布你的评论']").clear()
    browser.find_element_by_css_selector("textarea[placeholder='发布你的评论']").send_keys(content)
    time.sleep(2)
    browser.find_element_by_xpath('//span[text()="评论" and @class="woo-button-content"]/../..').click()
    time.sleep(200)

# 指定用户爬取最近20条微博
def excetue(uid):
    browser.get('https://weibo.com/u/'+str(uid))
    for k in range(20):
        browser.execute_script(script)
        time.sleep(10)
    hrefs = browser.find_elements_by_css_selector("a[href ^='https://weibo.com/"+str(uid)+"/']")
    for href in hrefs:
        url=href.get_attribute('href')
        urls.append(url)
    time.sleep(5)
    for url in urls:
        add_comment(url)

excetue(uid)
print("-----------------END_JOB-----------------")
browser.quit()