import requests
from bs4 import BeautifulSoup

# 浏览器信息
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"}
movie_list = []

for x in range(0, 10):
    url = "https://movie.douban.com/top250?start={0}&filter=".format(x * 25)
    # 向目标网页发起请求
    r = requests.get(url=url, headers=headers, timeout=10)
    # print(x + 1, "页面状态码:", r.status_code)
    soup = BeautifulSoup(r.text, "lxml")
    div_list = soup.find_all("div", class_="hd")
    # print(div_list)
    for i in div_list:
        movie = i.a.span.text.strip()
        movie_list.append(movie)

print(movie_list)
