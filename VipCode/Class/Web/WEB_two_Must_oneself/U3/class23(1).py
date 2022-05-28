import requests
from bs4 import BeautifulSoup

# 任务一
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
url='https://baike.sogou.com/city/map.v'
r = requests.get(url=url, headers=headers)
r.encoding='utf-8'
# print(r.text)
html = BeautifulSoup(r.text, 'html.parser')
con=html.select(".yb_city_left h3 a")
# print(con)
# 抓取标题
for i in con:
    # 抓取标题
    title=i.get_text()
    # print(title)
    # 抓取href属性
    href=i.get("href")
    url="https://baike.sogou.com"+href
    # 任务二
    req=requests.get(url=url,headers=headers)
    req.encoding="utf-8"
    # print(req.text)
    lable = BeautifulSoup(req.text, 'html.parser')
    scenic=lable.find_all("div",class_="lemma-intro")[0].get_text()
    # print(scenic)
    with open("著名景点.txt","a",encoding="utf-8")as f:
        f.write(title)
        f.write(scenic)