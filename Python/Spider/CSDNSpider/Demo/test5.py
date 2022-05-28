from urllib import request

url = "http://httpbin.org/ip"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

# # 获取ip
# op = request.urlopen(url)
# print(op.read())

# 使用代理
url = "http://httpbin.org/ip"
# 1使用ProxyHandler, 传入代理构建一个handler
handler = request.ProxyHandler({"http":"106.3.45.16:58080"})
# 2使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())





