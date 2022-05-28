# 将数据写入文件
a = input("请输入你需要写入文件的内容: ")
with open("test.txt", "wt") as out_file:
    out_file.write(a)

# 读取文件
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print("你写入文件的内容是: ", text)

