"""
任务要求: 爬取王者荣耀官网所有英雄的名字, 并存放到本地文件 英雄.txt

"""








import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
url='https://pvp.qq.com/web201605/herolist.shtml'
r = requests.get(url=url, headers=headers)
r.encoding='gbk'

# print(r.text)
# herolist clearfix

html = BeautifulSoup(r.text, 'html.parser')
alists = html.select(".herolist-content img")
print(alists)
print("英雄个数:",len(alists))
for x in alists:
    names = x.get("alt")
    print(names)
















