
with open("登鹳雀楼.txt", "r", encoding="utf8") as f:
    r1 = f.read()            #     读所有
    print(r1)

with open("登鹳雀楼.txt", "r", encoding="utf8") as f:
    r1 = f.readline()        #     按行读
    print(r1)

with open("登鹳雀楼.txt", "r", encoding="utf8") as f:
    r1 = f.readlines()       #     读所有行，返回列表
    print(r1)




