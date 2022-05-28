import requests
from bs4 import BeautifulSoup
import pymysql

#连接数据库
conn = pymysql.connect(host='localhost',user = "root",passwd = "934911535",db="bk",charset="utf8")
cursor = conn.cursor()

# 创建数据表
sql="""
    create table animal(
        id int not null primary key auto_increment,
        animal_name char(10),
        introduce text);
"""

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"}
# url="http://baike.baidu.com/fenlei/%E5%8A%A8%E7%89%A9"
url = "https://baike.baidu.com/item/%E7%8C%AB/22261"
re=requests.get(url=url,headers=header)
re.encoding="utf-8"
html=BeautifulSoup(re.text,"html.parser")

title=[]
content=[]

h4=html.find_all("h4")
for a in h4:
    title1=a.get_text()
    title.append(title1)

p=html.select(".hotcontent p")
for b in p:
    content1=b.get_text()
    content.append(content1)
###########挑战###########################################################
href=html.select(".photo a")
for i in href:
    url="http://baike.baidu.com"+i.get("href")
    req=requests.get(url=url,headers=header)
    req.encoding="utf-8"
    html=BeautifulSoup(req.text,"html.parser")
    title2=html.find_all("h1")[0].get_text()
    title.append(title2)
    content2=html.select(".lemma-summary .para")[0].get_text()
    content.append(content2)

# print(len(title))
# print(len(content))


# 存入抓取的数据
for x in range(0,15):
    animal_name=title[x]
    introduce = content[x]
    sql="insert into animal(animal_name, introduce) values('%s','%s')"%(animal_name,introduce)
    #执行sql语句
    cursor.execute(sql)
    # 提交到数据库
    conn.commit()

    
