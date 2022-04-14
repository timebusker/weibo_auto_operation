from selenium import webdriver
import time
import random
import pymysql

browser = webdriver.Edge()
script="window.scrollTo(0,document.body.scrollHeight)"

# select count(*) from weibo_auto where auto_type='评论' limit 10;
# mysql数据库连接
class MysqlDb():
    def __init__(self, host, port, user, passwd, db):
        # 建立数据库连接
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db
        )
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    def __del__(self): # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()
    def select_db(self, sql):
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data
    def execute_db(self, sql):
        try:
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()

database = MysqlDb("127.0.0.1", 3306, "root", "timebusker", "weibo")

# 日志插入
def insertLog(auto_type,weibo_url):
    timestr = time.strftime("%Y%m%d%H%M%S")
    insert_sql = 'insert into weibo_auto(datetimestr, auto_type,weibo_url) values(\"'+ timestr +'\",\"'+ auto_type +'\",\"'+ weibo_url +'\")'
    database.execute_db(insert_sql)

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

# 给指定微博评论
def auto_comment(weibo_url):
    browser.get(weibo_url)
    browser.implicitly_wait(2)
    time.sleep(10)
    for cnt in range(10):
        content = get_content()
        browser.find_element_by_css_selector("textarea[placeholder='发布你的评论']").clear()
        browser.find_element_by_css_selector("textarea[placeholder='发布你的评论']").send_keys(content)
        time.sleep(2)
        button=browser.find_element_by_xpath('//span[text()="评论" and @class="woo-button-content"]/../..')
        browser.execute_script("arguments[0].click()", button)
        time.sleep(120)
        insertLog('评论',weibo_url)

# 给指定微博评论回复
def auto_reply(weibo_url):
    browser.get(weibo_url)
    browser.implicitly_wait(2)
    time.sleep(10)
    # 回复
    replys=browser.find_elements_by_css_selector("i[class='woo-font woo-font--comment']")
    for reply in replys:
        time.sleep(20)
        browser.execute_script("arguments[0].click()", reply)
        time.sleep(10)
        content = get_content()
        browser.find_element_by_css_selector("textarea[placeholder='发布你的回复']").clear()
        browser.find_element_by_css_selector("textarea[placeholder='发布你的回复']").send_keys(content)
        time.sleep(2)
        button=browser.find_element_by_xpath('//span[text()="回复" and @class="woo-button-content"]/../..')
        browser.execute_script("arguments[0].click()", button)
        time.sleep(60)
        insertLog('回复',weibo_url)

# 给指定微博点赞
def auto_liked(weibo_url):
    browser.get(weibo_url)
    browser.implicitly_wait(2)
    time.sleep(10)
    # 点赞
    buttons = browser.find_elements_by_xpath('//span[@class="woo-like-count"]/..')
    for button in buttons:
        clazz = button.get_attribute("class")
        if clazz.find('IconList_likebox')>=0:
            browser.execute_script("arguments[0].click()", button)
            time.sleep(10)
            insertLog('点赞',weibo_url)


# 指定用户爬取最近20条微博
def excetue(uid):
    # browser.execute_script("document.body.style.zoom='0.75'")
    browser.get('https://weibo.com/u/'+str(uid))
    for k in range(5):
        browser.execute_script(script)
        time.sleep(10)
    hrefs = browser.find_elements_by_css_selector("a[href^='https://weibo.com/"+str(uid)+"/']")
    for href in hrefs:
        url=href.get_attribute('href')
        urls.append(url)
    time.sleep(5)
    for url in urls:
        auto_liked(url)
        auto_reply(url)
        auto_comment(url)



if __name__ == '__main__':
    while True:
        try:
            excetue(uid)
            print("-----------------END_JOB-----------------")
            time.sleep(1800)
        except Exception as e:
            print("操作出现错误：{}".format(e))