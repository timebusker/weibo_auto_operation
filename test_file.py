# -*- coding: utf-8 -*-
# @Author: HUAWEI
# @Date:   2022-04-07 22:59:19
# @Last Modified by:   HUAWEI
# @Last Modified time: 2022-04-07 23:35:48

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d/%H"
logging.basicConfig(filename='weibo.log', level=logging.INFO, format=LOG_FORMAT)


ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'timebusker';