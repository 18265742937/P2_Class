import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
url='https://baijiahao.baidu.com/s?id=1599683720343953472&wfr=spider&for=pc'
req = requests.get(url=url, headers=headers)
req.encoding='utf-8'
# print(req.text)
html = BeautifulSoup(req.text, 'html.parser')
imgs=html.select(".article-content img")
print(imgs)
for i in imgs:
    url=i.get("src")
    img=requests.get(url=url).content
    with open("images\\"+str(imgs.index(i))+".jpg","wb")as f:
        f.write(img)


