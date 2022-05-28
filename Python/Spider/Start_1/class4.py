import requests
from bs4 import BeautifulSoup

# 目标网址
url = "https://movie.douban.com/top250?start='+str(i*25)"
# 浏览器信息
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
# 向目标网站发起请求
r = requests.get(url=url, headers=headers)
# 设置请求编码--->跟随目标网站
r.encoding = "gbk"
# 对目标网站进行解析, 获取源码
soup = BeautifulSoup(r.text, "html.parser")
# 获取源码中的目标数据
title = soup.find("h3", class_="cover-title").get_text()
title2 = soup.find("h2", class_="cover-name").get_text()
# print(title)

with open(r"./"+title2+".txt", "a+", encoding="utf-8") as f:
    f.write(title)



