"""
一个基本的网页请求
"""
# 导入工具
from urllib import request
# 获取请求
re = request.urlopen("https://www.guazi.com")
# 输出未解析结果
# print(re)
# 输出解析后的所有字节数据
print(re.read())   # 读取所有的字节,所有的字节数
# print(re.readline())   # 读取一行数据
# print(re.readlines())   # 读取多行
# 获取的信息是目标网站准备好发给你的假数据, 因为知道你是爬虫
