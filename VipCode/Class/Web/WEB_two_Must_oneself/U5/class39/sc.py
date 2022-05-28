import requests, pymysql, time
from bs4 import BeautifulSoup
import pymysql

# 数据库相关
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='12345678', db='bk',charset='utf8')
cursor = conn.cursor() 

fetchcity = "select name from city;"
cursor.execute(fetchcity)
data = cursor.fetchall()
print(data)
citys = []
for i in data:
    citys.append(i[0])
print(citys)


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

for c in citys:
    url = 'https://baike.sogou.com/city/' + str(c) +'.v'
    print('开始抓取:', url)
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf8'
    html = BeautifulSoup(req.text, 'html.parser')
    title = html.find_all('h1')[0].get_text()
    content = html.find_all('div', class_='abstrat_text')[0].get_text()
    reptext = content.replace("'", "\\'")
    print(reptext)

    # 存入数据库
    sql = "update city set description='%s' where name='%s';"%(reptext, c)
    cursor.execute(sql)
    conn.commit()
    