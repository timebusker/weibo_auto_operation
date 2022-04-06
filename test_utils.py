# -*- coding: utf-8 -*-
# @Author: HUAWEI
# @Date:   2022-03-02 00:42:35
# @Last Modified by:   HUAWEI
# @Last Modified time: 2022-03-12 20:51:54

import random
import time
import datetime

print(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], random.randint(0,1))))
print("====>",random.randint(0,999))
print("====>",random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))
print(time.localtime())
print (time.strftime("%H:%M:%S"))
print(datetime.date.today())

print(datetime.date.today(),'',time.strftime("%H:%M:%S"))
print (time.strftime("%Y%m%d%H%M%S"))





for index in range(10):
    print(index)


emojis=['[雪容融]','[哈哈]','[可爱]','[抓狂]','[爱你]','[色]','[笑而不语]','[嘻嘻]','[鲜花]','[许愿虎]','[挤眼]','[2022]','[凯洛伦]','[心]','[男孩儿]','[作揖]','[赞啊]','[小黄人委屈]','[小黄人高兴]','[小黄人微笑]','[哪吒开心]','[冰墩墩]','[金牌]','[谜语人]','[虎爪比心]','[互粉]','[打call]','[抱一抱]','[亲亲]','[喵喵]','[杰瑞]','[中国赞]','[坏笑]','[舔屏]','[害羞]','[哆啦A梦吃惊]','[伴我同行]','[美国队长]','[羞嗒嗒]','[给力]','[haha]','[兔子]','[赞]','[good]','[耶]','[奥特曼]','[干杯]','[拳头]','[弗莱见钱眼开]','[给你小心心]','[棒棒糖]','[好喜欢]','[佩奇]','[加油]','[飞机]']
texts=['小蔡牛逼','小蔡威武','蔡蔡女神','蔡大美女','爱你','蔡蔡','蔡大','大佬','优秀','完美','高手','厉害','100%的准确率','一起发财','简直是不可或缺！','感谢蔡神','没亏过，哈哈哈','2022一起发财！','简直是不可思议！','没亏过','感谢蔡神','感谢蔡女神','感谢蔡蔡','小蔡蔡','虎年发财','感谢相遇','小散保护神哇！','相见恨晚。。。','完美','非常完美','简直了','爱涨停！','冲击涨停','冲啊','加油！','加油干！','一个字，干','二营长，我的意大利炮','我的意大利炮呢？','非常感谢','感谢','不骄不躁','稳定收益','非常棒','棒棒哒!','送你一朵小红花!']


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
        


for index in range(100):
    print("---------------->",get_content())

print(random.choice([True, False]))