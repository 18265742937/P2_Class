# @Author: 茄子
# @Date: 2019-09-11 16:12:40
# @Last Modified by:  茄子
# @Last Modified time: 2019-09-11 16:12:40
# @Description:  "第四十五课  点球大战(三)"


import random
import turtle  

t = turtle.Turtle()
t.ht()
t.speed(0)
t.pensize(10)
#开始--------------------------------------
t1 = turtle.Turtle()
t1.ht()
t1.speed(0)
t2 = turtle.Turtle()
t2.ht()
t2.speed(0)
t2.color("red")
t2.penup()
t2.goto(-70,-50)
t2.pendown()
#结束----------------------------------------

t.left(90)
t.penup()
t.goto(-120, -30)
t.pendown()
t.fd(100)
t.right(90)
t.fd(240)
t.right(90)
t.fd(100)

t.pensize(5)
t.penup()
t.goto(0, 70)
t.pendown()
t.fd(100)
t.penup()
t.goto(-120, 20)
t.pendown()
t.left(90)
t.fd(240)

#开始--------------------------------------------------------------------------
def number(a):
    t1.penup()
    if a == 1:
        t1.goto(-60, 45)
    elif a == 2:
        t1.goto(60, 45)
    elif a == 3:
        t1.goto(-60, -5)
    else:
        t1.goto(60, -5)
    t1.pendown()
    t1.dot(18)
    t1.color("white")
    t1.shape("turtle")
    t1.seth(90)
    t1.st()
#结束---------------------------------------------------------------------
         
score = [0, 0]
direction = [1, 2, 3, 4]  


def shoot(c):
    if c == 0:
        print('==== 轮到你来射门了！ ====')
    else:
        print('==== 轮到你来防守了！ ====')
    a = int(input('选择方向:'))  
    b = random.choice(direction)
    if a != b:
        t1.color("black") #添加代码-------------------------------------------------------
        number(a) #添加代码---------------------------------------------------------
        print('射门成功！')
        score[c] += 1
    else:
        print('防守成功！')
    print('得分: %d(玩家) - %d(电脑)' % (score[0], score[1]))



i = 1

while i < 6:
    print('==== 第%d回合 ====' % i)
    shoot(0)
    shoot(1)
    i += 1

while score[0] == score[1]:
    print('==== 第%d回合 ====' % i)
    shoot(0)
    shoot(1)
    i += 1
    if i == 7:
        break
    
#开始----------------------------------------------------
if score[0] > score[1]:
    t2.write("你击败了电脑!",font=("Arial",16,"normal"))
else:
    t2.write("我还会回来的!", font=("Arial", 16, "normal"))
#结束-------------------------------------------------





turtle.mainloop()