import requests


url = "https://www.baidu.com/"

# 浏览器信息  //
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"}


r = requests.get(url=url, headers=headers)

# 获取网页状态码
print(r)

















