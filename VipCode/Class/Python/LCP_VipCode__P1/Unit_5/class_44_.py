# @Author: 茄子 
# @Date: 2019-09-11 16:12:40   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-11 16:12:40  
# @Description:  "第四十四课  点球大战(二)"


import random
import turtle  #添加代码--------------------------------------------

#开始------------------------------------------
t = turtle.Turtle()
t.ht()
t.speed(0)
t.pensize(10)
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
#结束--------------------------------------------------------

score = [0, 0]
direction = [1, 2, 3, 4]  #修改代码---------------------------------


def shoot(c):
    if c == 0:
        print('==== 轮到你来射门了！ ====')
    else:
        print('==== 轮到你来防守了！ ====')
    a = int(input('选择方向:1/2/3/4'))  #修改代码------------------------------------
    b = random.choice(direction)
    if a != b:
        print('射门成功！')
        score[c] += 1
    else:
        print('防守成功！')
    print('得分: %d(玩家) - %d(电脑)' % (score[0], score[1]))

#开始--------------------------------------------------
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
#结束-------------------------------------------------

if score[0] > score[1]:
    print('你击败了电脑！')
else:
    print('我还会回来的！')



