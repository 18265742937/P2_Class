import requests
from bs4 import BeautifulSoup

#爬取搜狗百科
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
url='https://baike.sogou.com/v29998.htm?fromTitle=狗'
req = requests.get(url=url, headers=headers)
req.encoding="utf-8"
html = BeautifulSoup(req.text, 'html.parser')
# 搜狗百科的标题和介绍
title = html.find_all('h1')[0].get_text()
content = html.find_all('div', class_='abstract')[0].get_text()


######python操作MySQL#####################################################

import pymysql
#打开数据库连接,指定用户、密码、数据库、输入格式
conn = pymysql.connect('localhost',user = "root",passwd = "934911535",db="bk",charset="utf8")
# print("连接成功")
#获取游标
cursor=conn.cursor()

#sql语句
# sql='''CREATE TABLE baike(
#             id INT PRIMARY KEY AUTO_INCREMENT,
#             title CHAR(100) NOT NULL,
#             content TEXT NOT NULL
#     )'''

# sql="insert into baike(title,content) value('%s','%s')"%(title,content)

# sql="select * from baike"

# sql="truncate table baike"


cursor.execute(sql)   #执行sql语句

conn.commit()    # 提交到数据库
results = cursor.fetchall()
print(results)



