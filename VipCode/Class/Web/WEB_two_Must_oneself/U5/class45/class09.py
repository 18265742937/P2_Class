import requests
from bs4 import BeautifulSoup

from vpscrapy import SL 
sl = SL()

sl.get("https://pvp.qq.com/web201605/herolist.shtml")
target = sl.findLinkByText("英雄") 
sl.runScript('arguments[0].scrollIntoView();', target)
sl.waitUntil("herolist-content")
html = sl.pageSource()
bf = BeautifulSoup(html,'html.parser')
thumb=bf.select(".herolist-content ul li a")
# print(thumb)
for i in thumb:
    url="https://pvp.qq.com/web201605/"+i.get("href")
    # print(url)
    sl.get(url)
    hero = sl.pageSource()
    herohtml = BeautifulSoup(hero,'html.parser')
    heroName=herohtml.find_all("h2")[0].get_text()
    print(heroName)
    heroStory=herohtml.select("#hero-story p")
    # print(heroStory)
    for j in heroStory:
        content=j.get_text()
        # print(text)
        with open(heroName+".text","a",encoding="utf-8")as f:
            f.write(heroName+"\n\n")
            f.write(content)






