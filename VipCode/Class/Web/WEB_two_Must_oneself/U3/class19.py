#导入工具
import requests
from bs4 import BeautifulSoup

# 获取百度百科的其中一页
#HTTP请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
#网址地址
url = 'https://baike.sogou.com/v29998.htm?fromTitle=狗'
#发起请求
req = requests.get(url=url, headers=headers)
#编码格式
req.encoding = "utf-8"
#获取网页源码内容
# print(req.text)

#设置解析器
html = BeautifulSoup(req.text, 'html.parser')
#解析源代码
title = html.find_all('h1')[0].get_text()
#获取标题
print(title)




	



