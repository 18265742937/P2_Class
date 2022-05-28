import requests, sys
from bs4 import BeautifulSoup

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
# req = requests.get(url='https://gp.qq.com/cp/a20190522gamedata/pc_list.shtml', headers=headers)
# req.encoding = 'GBK'
# print(req.text)

# 控制台- Network - xhr
# 获取图片数据

from vpscrapy import SL 

sl = SL()
sl.get('https://gp.qq.com/cp/a20190522gamedata/pc_list.shtml')

# sl.waitUntil('.qiang-0')

# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(html)