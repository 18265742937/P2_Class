import requests

# 网址
url = "https://baike.sogou.com/v29867.htm?fromTitle=%E7%8C%AB"
# 请求头
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
req = requests.get(url=url, headers=headers)
# 设置编码
req.encoding="utf-8"
# 输出状态码
# print(req)
print(req.text)













