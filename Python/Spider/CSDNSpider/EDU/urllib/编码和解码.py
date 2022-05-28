from urllib import parse

data = {"name": "茄子", "age": 18, "message": "hello world!"}
# 进行编码
js = parse.urlencode(data)   
print("编码后:", js)
# 进行解码
js2 = parse.parse_qs(js)
print("解码后", js2)



