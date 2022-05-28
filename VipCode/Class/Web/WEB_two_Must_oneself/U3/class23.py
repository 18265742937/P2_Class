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
# print(hrefList)

#======class05===========================================================
for url in hrefList:
    print('开始抓取:', url)
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf8'
    # print(req.text)
    html = BeautifulSoup(req.text, 'html.parser')
    title = html.find_all('h1')[0].get_text()
    print(title)
    content = html.find_all('div', class_='abstrat_text')[0].get_text()
    print(content)

#  # 存为文件
    with open('城市列表.txt', 'a', encoding='utf-8') as f:
        f.write(title+"\n")
        f.write(content)
        f.write('\n\n')  
