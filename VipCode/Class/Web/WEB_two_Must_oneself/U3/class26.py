import requests
from bs4 import BeautifulSoup


# 控制台查找数据：控制台- Network - xhr
# 了解并导入selenuim的方法
from vpscrapy import SL

# 使用导入的方法，并打开浏览器访问页面
sl = SL()
sl.get('https://gp.qq.com/cp/a20190522gamedata/pc_list.shtml')
#######class08############################################################
# 本节课网页的动态加载部分
# 根据类名等待加载动态的部分（要求学生可以通过修改类名来加载其他的网页的动态数据）
# sl.waitUntil('.qiang-0')

# 抓取加载后的HTML文档并抓取HTML文档写入HTML文件查看
# html = sl.pageSource()

# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(html)

# 解析并利用层级根据类名和标签名匹配标签
# bf = BeautifulSoup(html,'html.parser')
# imgs=bf.select("#section-container img")

# 循环获取每一个标签中的src并拼接url，发起请求并抓取图片存入文件夹(要求学生熟悉图片抓取保存的流程)
# for a in imgs:
#   url="http:"+a.get("src")
#   content=requests.get(url=url).content
#   with open("images\\"+i+str(imgs.index(a))+".png",'wb') as f:
#       f.write(content)
sl.waitUntil('.qiang-0')
# 让程序模拟用户点击页面中的元素
lists = ['武 器', '配 件', '物 资', '载 具', '地 图']
for i in lists:
    # 根据文字匹配到文字的可点击链接（要求学生会使用findLinkByText方法）
    target = sl.findLinkByText(i)
    #利用js将定位到的元素拖动到可见区域（要求学生了解runScript方法和里面的js参数）
    sl.runScript('arguments[0].scrollIntoView();', target)
    target.click()         # 给添加点击事件

    # 挑战：试着修改代码，实现在其他网页中实现模拟用户点击的效果（复制到新的文件中修改）

