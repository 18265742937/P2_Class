

"""
#标准库(模块)
    random
        randint()
        choice()
        ......
    turtle
    time
    .....

(1)有哪些常用的库?
(2)库里面有哪些常用的函数
(3)函数的使用注意事项
    传参(参数的个数/参数的数据类型/参数的顺序)

#如何查看库里面有哪些函数?   dir()
import random

a = dir(random)
print(a)


#方式一
import random #导入库

a = random.randint(10,20)
print(a)


#方式二
from random import randint   #导入库里面的指定函数

a = randint(10,20)
print(a)


#方式三
    别名   as
from random import randint as r  #导入库里面的指定函数并取一个别名

a = r(10,20)
print(a)


#方式四
from random import *#导入库

a = randint(10,20)
print(a)


"""


"""
1,#python的错误与异常
    #错误(语法错误)--->结构上的错误
    if 3>9
        print("大了")

    #异常
    print(4/2)  #异常 ---> ZeroDivisionError: division by zero

    a = [5,6,7]
    print(a[3])   #IndexError: list index out of range


2, 方式一
    try:
        a = 4/0
    except IndexError:
        print("茄子")
    except ZeroDivisionError:
        print("你错了")
    else:
        print("奥利给")


3,方式二
    try:
        a = 4/0
    except (IndexError,ZeroDivisionError):
        print("你错了")
    else:
        print("奥利给")





try:
    a = 4/0
except (IndexError,ZeroDivisionError):
    print("你错了")
else:
    print("奥利给")


"""































