import requests
from bs4 import BeautifulSoup

# 获取百度百科的其中一页
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
url='https://baike.sogou.com/v29998.htm?fromTitle=狗'
req = requests.get(url=url, headers=headers)
req.encoding="utf-8"
# print(req.text)

html = BeautifulSoup(req.text, 'html.parser')
# 抓取标题和介绍文字
title = html.find_all('h1')[0].get_text()

#class2开始####################################################################
content = html.find_all('div', class_='abstract')[0].get_text()
# print(title,content)

# 抓取表格
th=html.select(".abstract_tbl .abstract_list th")
# print(th)
th_key=[]
for i in th:
    key=i.get_text()
    th_key.append(key)
print(th_key)
div=html.select(".abstract_tbl .abstract_list .base-info-card-value")
# print(div)
div_value=[]
for j in div:
    value=j.find(text=True).strip()
    div_value.append(value)
print(div_value)

