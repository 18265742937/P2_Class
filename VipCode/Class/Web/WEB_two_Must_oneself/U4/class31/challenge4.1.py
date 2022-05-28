import requests
from bs4 import BeautifulSoup
# 连接数据库
import pymysql
conn = pymysql.connect('localhost',user = "root",passwd = "123456",db="bk",charset="utf8")
cursor=conn.cursor()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
url='https://baike.sogou.com/city/map.v'
r = requests.get(url=url, headers=headers)
r.encoding='utf-8'
html = BeautifulSoup(r.text, 'html.parser')
alists = html.select(".yb_city_list a")

for a in alists:
    url='https://baike.sogou.com/'+a.get('href')
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf8'
    html = BeautifulSoup(req.text, 'html.parser')
    title = html.find_all('h1')[0].get_text()
    content = html.find_all('div', class_='abstrat_text')[0].get_text()
    # 插入数据
    # sql="insert into baike(title,content) value('%s','%s')"%(title,content)
    # sql="select * from baike"
    #执行sql语句
    # cursor.execute(sql)
    # 提交到数据库
    # conn.commit()
sql="select * from baike"
#执行sql语句
cursor.execute(sql)
# 提交到数据库
conn.commit()
results = cursor.fetchall()
print(results)