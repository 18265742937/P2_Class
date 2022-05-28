import requests
from bs4 import BeautifulSoup
from vpscrapy import SL
sl = SL()

sl.get('https://yys.163.com/shishen/index.html')
sl.waitUntil('.pic_wrap')

html = sl.pageSource()
bf = BeautifulSoup(html, 'html.parser')
imgs = bf.select(".shishen_container img")
print(imgs)

for a in imgs:
    url = a.get("src")
    content = requests.get(url=url).content
    with open("images\\式神"+str(imgs.index(a))+".png", 'wb') as f:
        f.write(content)

