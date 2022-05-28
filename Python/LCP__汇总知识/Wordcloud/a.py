import wordcloud
import jieba


f = open(r"D:\Code\P2_CLASS\LCP_VipCode_知识\Wordcloud\a.txt", "r", encoding="utf8")
a = f.read()
b = " ".join(jieba.lcut(a))
# print(b)


w = wordcloud.WordCloud()
w.generate(b)
w.to_file("图.jpg")
