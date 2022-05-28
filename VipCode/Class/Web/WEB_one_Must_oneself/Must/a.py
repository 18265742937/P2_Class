import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
url='http://www.521609.com/meinvxiaohua/'
req = requests.get(url=url, headers=headers)
req.encoding='utf-8'
# print(req.text)
html = BeautifulSoup(req.text, 'html.parser')
imgs = html.select(".index_img .list_center img")
print(imgs)