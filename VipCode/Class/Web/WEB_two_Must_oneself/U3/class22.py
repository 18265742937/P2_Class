import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
url='https://baike.sogou.com/city/map.v'
r = requests.get(url=url, headers=headers)
r.encoding='utf-8'
# print(r.text)

html = BeautifulSoup(r.text, 'html.parser')
alists = html.select(".yb_city_list a")
# print(alists)

hrefList = []
for a in alists:
    url='https://baike.sogou.com/'+a.get('href')
    hrefList.append(url)
print(hrefList)


