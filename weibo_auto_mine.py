from selenium import webdriver
import time
import random

browser = webdriver.Edge()
script="window.scrollTo(0,document.body.scrollHeight)"

# 小散爱涨停 UID
uid = '6148104254'
urls=[]
browser.get('https://weibo.com/'+str(uid))
browser.maximize_window()
time.sleep(40)


emojis=['[雪容融]','[哈哈]','[可爱]','[抓狂]','[爱你]','[色]','[笑而不语]','[嘻嘻]','[鲜花]','[许愿虎]','[挤眼]','[2022]','[凯洛伦]','[心]','[男孩儿]','[作揖]','[赞啊]','[小黄人委屈]','[小黄人高兴]','[小黄人微笑]','[哪吒开心]','[冰墩墩]','[金牌]','[谜语人]','[虎爪比心]','[互粉]','[打call]','[抱一抱]','[亲亲]','[喵喵]','[杰瑞]','[中国赞]','[坏笑]','[舔屏]','[害羞]','[哆啦A梦吃惊]','[伴我同行]','[美国队长]','[羞嗒嗒]','[给力]','[haha]','[兔子]','[赞]','[good]','[耶]','[奥特曼]','[干杯]','[拳头]','[弗莱见钱眼开]','[给你小心心]','[棒棒糖]','[好喜欢]','[佩奇]','[加油]','[飞机]']
texts=['小蔡牛逼','小蔡威武','蔡蔡女神','蔡大美女','爱你','蔡蔡','蔡大','大佬','优秀','完美','高手','厉害','100%的准确率','一起发财','简直是不可或缺！','感谢蔡神','没亏过，哈哈哈','2022一起发财！','简直是不可思议！','没亏过','感谢蔡神','感谢蔡女神','感谢蔡蔡','小蔡蔡','虎年发财','感谢相遇','小散保护神哇！','相见恨晚。。。','完美','非常完美','简直了','爱涨停！','冲击涨停','冲啊','加油！','加油干！','一个字，干','二营长，我的意大利炮','我的意大利炮呢？','非常感谢','感谢','不骄不躁','稳定收益','非常棒','棒棒哒!','送你一朵小红花!']
# 评论组装
def get_content():
    global count
    timestr = time.strftime("%M%S")
    emoji=''.join(random.sample(emojis, random.randint(0,3)))
    text=''.join(random.sample(texts+emojis, 1))
    if random.choice([True, False]):
        content=text+emoji
    else:
        content=emoji+text
    if(content is None or len(content)==0):
        content='播报时间啦，' + time.strftime("%Y-%m-%d %H:%M:%S") + '[哈哈][哈哈]'
    return content

# 给指定某条微博添加内容
def add_comment(weibo_url):
    browser.get(weibo_url)
    browser.implicitly_wait(2)
    time.sleep(10)
    # 刷新页面内容
    for index in range(5):
        browser.execute_script(script)
        time.sleep(5)
    # 点赞
    buttons = browser.find_elements_by_xpath('//span[@class="woo-like-count"]/..')
    for button in buttons:
        clazz = button.get_attribute("class")
        if clazz.find('IconList_likebox')>=0:
            browser.execute_script("arguments[0].click()", button)
            time.sleep(2)
    # 评论的评论
    # browser.refresh()
    time.sleep(10)
    content_is=browser.find_elements_by_css_selector("i[class='woo-font woo-font--comment']")
    for content_i in content_is:
        browser.execute_script("arguments[0].click()", content_i)
        time.sleep(2)
        content = get_content()
        browser.find_element_by_css_selector("textarea[placeholder='发布你的回复']").clear()
        browser.find_element_by_css_selector("textarea[placeholder='发布你的回复']").send_keys(content)
        time.sleep(2)
        zpl_button=browser.find_element_by_xpath('//span[text()="回复" and @class="woo-button-content"]/../..')
        browser.execute_script("arguments[0].click()", zpl_button)
        time.sleep(120)
    # 本博评论
    browser.refresh()
    time.sleep(60)
    content = get_content()
    browser.find_element_by_css_selector("textarea[placeholder='发布你的评论']").clear()
    browser.find_element_by_css_selector("textarea[placeholder='发布你的评论']").send_keys(content)
    time.sleep(2)
    pl_button=browser.find_element_by_xpath('//span[text()="评论" and @class="woo-button-content"]/../..')
    browser.execute_script("arguments[0].click()", pl_button)
    time.sleep(60)

# 指定用户爬取最近20条微博
def excetue(uid):
    # browser.execute_script("document.body.style.zoom='0.5'")
    browser.get('https://weibo.com/u/'+str(uid))
    for k in range(3):
        browser.execute_script(script)
        time.sleep(5)
    hrefs = browser.find_elements_by_css_selector("a[href^='https://weibo.com/"+str(uid)+"/']")
    for href in hrefs:
        url=href.get_attribute('href')
        urls.append(url)
    time.sleep(5)
    for url in urls:
        add_comment(url)
        
        print("=====================>",url)

excetue(uid)
print("-----------------END_JOB-----------------")
browser.quit()