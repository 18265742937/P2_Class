# 获取网页源代码
# requests ---> 用于请求网页
import requests

# 目标网址
url = "https://www.baidu.com/"

# 浏览器信息(请求头)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"}

# 向目标网页发起请求
r = requests.get(url=url, headers=headers)

# 设置请求编码--->跟随目标网站
r.encoding = "utf-8"

# 获取网页源码
print(r.text)
