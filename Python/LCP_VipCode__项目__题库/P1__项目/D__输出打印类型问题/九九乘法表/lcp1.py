for x in range(1, 10):  # 外循环--控制行数
    s = ""
    for y in range(1, x+1):  # 内循环--控制每一行的内容
        a = x * y
        s += str(y) + "*" + str(x) + "=" + str(a) + " "
    print(s)
