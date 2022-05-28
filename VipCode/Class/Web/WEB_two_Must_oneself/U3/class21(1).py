# 任务############################################################
import requests
from bs4 import BeautifulSoup

# 获取百度百科的其中一页
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
url='https://baijiahao.baidu.com/s?id=1599683720343953472&wfr=spider&for=pc'
req = requests.get(url=url, headers=headers)
req.encoding='utf-8'
print(req.text)

# html = BeautifulSoup(req.text, 'html.parser')
# title = html.find_all('h2')[0].get_text()
# title = html.find_all('h2')
# print(title)
# movie = html.find_all('div', class_='article-content')[0].get_text()
# print(movie)

# with open('电影系列.txt', 'a', encoding='utf-8') as f:
#     f.write(title)
#     f.write(movie)
