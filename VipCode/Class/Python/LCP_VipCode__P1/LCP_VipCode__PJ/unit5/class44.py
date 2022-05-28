#导入工具
import turtle
import random
import time

#设置画笔
t = turtle.Turtle()
t.pensize(1)
t.ht()
t.speed(0)
t1 = turtle.Turtle()
t1.ht()
t1.left(90)

#绘制小方格的函数
def square(x, y, c):
    t.color(c)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for x in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()


#创建列表存放位置,分别是左上, 右上, 左下, 右下
# local = [[-25, 25], [25, 25], [-25, -25], [25, -25]]

#调用函数绘制四个小方格
square(-50, 50, "pink")
square(0, 50, "green")
square(-50, 0, "orange")
square(0, 0, "purple")

#控制海龟位置的函数
def drawer(x):
    t1.penup()
    if x == 1:
        t1.goto(-25, 25)
    elif x == 2:
        t1.goto(25, 25)
    elif x == 3:
        t1.goto(-25, -25)
    else:
        t1.goto(25, -25)
    t1.pendown()
    t1.st()
    t1.shape("turtle")
    time.sleep(0.5)
    t1.ht()

#开始---------------------------------------------------------------
# #调用函数让小海龟移动
# drawer(1)
# drawer(2)
# drawer(3)
# drawer(4)
t2 = turtle.Turtle()
while True:
    s = ""
    for x in range(4):
        area = random.randint(1, 4)
        drawer(area)
        s += str(area)

    a = input("请输入海龟的出现次序: ")
    if s == a:
        t2.write("祝贺你, 回答正确", font=("arial", 12))
        break
    else:
        t2.write("别灰心, 再试一次", font=("arial", 12))
        time.sleep(3)
        t2.clear()

#结束-----------------------------------------------
#持续显示
turtle.done()
