# -*- coding: utf-8 -*-
# @Author: HUAWEI
# @Date:   2022-04-07 23:35:54
# @Last Modified by:   HUAWEI
# @Last Modified time: 2022-04-08 09:22:23


# 安装mysql依赖
# pip install PyMySQL

import pymysql

# create table weibo_auto(
#     id int(8) primary key not null auto_increment,
#     datetimestr varchar(32) not null,
#     auto_type varchar(32) not null,
#     weibo_url varchar(128) not null
# );


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


if __name__ == '__main__':
    db = MysqlDb("127.0.0.1", 3306, "root", "timebusker", "weibo")
    select_sql = 'select * from weibo_auto'
    # update_sql = 'UPDATE user SET username = "张三2" WHERE id = 1'
    insert_sql = 'INSERT INTO weibo_auto(datetimestr, auto_type) VALUES("20220408", "回复")'
    # delete_sql = 'DELETE FROM user WHERE id = 11'
    data = db.select_db(select_sql)
    print(data)
    # db.execute_db(update_sql)
    db.execute_db(insert_sql)
    # db.execute_db(delete_sql)
    data = db.select_db(select_sql)
    print(data)