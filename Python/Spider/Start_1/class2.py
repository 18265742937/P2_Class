import requests

url = "https://www.baidu.com/"
r = requests.get(url=url)
r.encoding = "utf-8"
print("文本编码:", r.encoding)
print("响应状态码:", r.status_code)
print(r.url)
print("字符串方式的响应体:", r.text)


















