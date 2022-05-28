"""
有时候拿到一个url, 需要对其各个部分进行分割, 那么这个时候就可以使用urlparse或者是urlsplit进行分割
"""
from urllib import parse

# 网页
url = "https://pic.sogou.com/pics?ie=utf8&p=40230504&interV=kKIOkrELjboLmLkEkrsTkKIMkbELjbgQmLkElbcTkKILmrELjb8TkKIKmrELjbkImTbxFE4ElKJ6wu981qR7zOMTKVeRFKIPjflHxOVNj+lHzrEMkL8RMifrLEWPjb0ElbkRmqR7zOM=_907194807&query=%E5%AE%89%E5%85%B6%E6%8B%89&"
# 对网页进行解析
request = parse.urlparse(url)
# 打印全部解析内容
print(request)
# 打印协议
print(request.scheme)
# 打印域名
print(request.netloc)
# 等等



















