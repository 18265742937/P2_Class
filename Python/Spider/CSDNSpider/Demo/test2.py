import requests
from bs4 import BeautifulSoup
import json

# movie_list = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"}
url = r"https://api-zero.livere.com/v1/comments/list?callback=jQuery1124022947380563393938_1619338106247&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1619338106249"
st = requests.get(url=url, headers=headers)
st.encoding = "utf-8"
# print(st.text)
# 获取json中的string
json_string = st.text
json_string = json_string[json_string.find('{') :-2]
json_data = json.loads(json_string)

# 从第一个大括号提取, 最后的两个字符-括号和分号不取
json_data = json.loads(json_string)
comment_list = json_data["results"]["parents"]
for eachone in comment_list:
    message = eachone["content"]
    print(message)



