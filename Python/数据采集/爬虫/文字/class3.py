# post 提交方式
import requests

# 目标网址
url = "https://www.baidu.com/"

# 浏览器信息(请求头)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"}

# 向目标网页发起请求   post 提交方式
r = requests.post(url=url, headers=headers)

# 设置请求编码--->跟随目标网站
r.encoding = "utf-8"

# 获取网页状态码
print(r)

# 获取服务器使用的文本编码
print(r.encoding)

# 获取网页状态码, 如果返回是200就表示请求成功了!
print(r.status_code)

# 获取网址
print(r.url)
