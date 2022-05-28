####挑战#################################################
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
url='https://baike.baidu.com/tashuo/browse/content?id=84d19be0f8bf0b324a4bdf13&fromModule=pcArticleMoreRecommend'

req = requests.get(url=url, headers=headers)
req.encoding='utf-8'
print(req.text)

html = BeautifulSoup(req.text, 'html.parser')
title=html.find_all('div',class_="caption")[0].get_text()
# print(title)
content_1=html.find_all('div',class_="article-summary")[0].get_text()
# print(content_1)
content_2=html.find_all('div',class_="main-text")[0].get_text()
print(content_2)
