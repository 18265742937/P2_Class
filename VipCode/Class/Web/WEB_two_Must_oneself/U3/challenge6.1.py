###挑战一###############################################################
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
url='https://baike.baidu.com/vbaike/%E4%BC%97%E5%BF%97%E6%88%90%E5%9F%8E%20%E5%85%B1%E6%8A%97%E7%96%AB%E6%83%85/56861'
req = requests.get(url=url, headers=headers)
req.encoding='utf-8'
# print(req.text)
html = BeautifulSoup(req.text, 'html.parser')
imgs=html.select(".gallary img")
print(imgs)
for i in imgs:
    url=i.get("data-src")
    img=requests.get(url=url).content
    with open("images\\众志成城 抗疫情"+str(imgs.index(i))+".jpg","wb")as f:
        f.write(img)

######挑战二####################################################################


header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
url="http://699pic.com/best_album/20/152/1.html"
r=requests.get(url=url,headers=header)
r.encoding="utf-8"
# print(r.text)
html=BeautifulSoup(r.text,"html.parser")
img=html.select(".album-item img")

for a in img:
    url=("http:"+a.get("src"))
    content=requests.get(url=url).content
    with open("images\\水墨山水图"+str(img.index(a))+".jpg",'wb') as f:
        f.write(content)