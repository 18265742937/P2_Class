import requests
from bs4 import BeautifulSoup


url = "https://baike.baidu.com/item/%E7%8C%AB/22261"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"}


r = requests.get(url=url, headers=headers)

# 将网页源码进行解析
soup = BeautifulSoup(r.text, "html.parser")
title = soup.find("h1").text
print(title)



