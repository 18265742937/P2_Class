import requests
from bs4 import BeautifulSoup

# 控制台查找数据：控制台- Network - xhr
# 了解并导入selenuim的方法
from vpscrapy import SL

# 使用导入的方法，并打开浏览器访问页面
sl = SL()
sl.get('https://gp.qq.com/cp/a20190522gamedata/pc_list.shtml')

# 根据类名等待加载动态的部分
sl.waitUntil('.qiang-0')

# 根据文字找到可点击文字的链接，让程序模拟用户点击
lists = ['武 器', '配 件', '物 资', '载 具', '地 图']
for i in lists:
    target = sl.findLinkByText(i)
    #利用js将定位到的元素拖动到可见区域
    sl.runScript('arguments[0].scrollIntoView();', target)
    target.click()
######class09######################################################
    # 本节课抓药是让学生熟练selenuim抓取图片的步骤

    # 抓取加载完成后的HTML代码并解析
    html = sl.pageSource()
    bf = BeautifulSoup(html, 'html.parser')
    # print(bf)

    # 根据类名和标签名匹配标签（要求学生熟练自己匹配标签）
    if lists.index(i) == 0:
        imgs = bf.select("#section-container img")
    else:
        imgs = bf.select("#section-container"+str(lists.index(i)+1)+" img")
    # print(imgs)

    # 循环获取抓取到的标签，并向每张图片的url发起请求抓取图片并保存（要求学生熟练保存图片）
    for a in imgs:
        url = "http:"+a.get("src")
        content = requests.get(url=url).content
        with open("images\\"+i+str(imgs.index(a))+".png", 'wb') as f:
            f.write(content)

