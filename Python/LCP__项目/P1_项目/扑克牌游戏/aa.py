











#检测输入是否合法
def check(a):
    for x in a:
        if a.count(x)>4:
            print("输入有误,请重新输入!")
            return 0
        else:
            return 1
#进行排序
def card(a):
    t1 = []  #出现次数为1次放入t1
    t2 = []  #出现次数为2次放入t2
    t3 = []  #出现次数为3次放入t3
    t4 = []  #出现次数为4次放入t4
    for x in a:
        if a.count(x) == 1:
            t1.append(x)
        elif a.count(x) == 2:
            t2.append(x)
        elif a.count(x) == 3:
            t3.append(x)
        else:
            t4.append(x)

    t1.sort(reverse=True)
    t2.sort(reverse=True)
    t3.sort(reverse=True)
    t4.sort(reverse=True)
    n = t4+t3+t2+t1
    print(tuple(n))

#测试数据  2,3,4,5,5,3,6,7,6,6,9,0,7,5,2,1,6,7,6,4,6

if __name__ == "__main__":
    a = input().split(",")
    b = []
    for x in a:
        b.append(int(x))
    s = check(b)
    if s==1:
        card(a)
