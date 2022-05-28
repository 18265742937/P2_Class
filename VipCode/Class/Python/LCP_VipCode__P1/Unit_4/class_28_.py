# @Author: 茄子 
# @Date: 2019-09-02 14:28:38
# @Last Modified by:  茄子
# @Last Modified time: 2019-09-02 14:28:38
# @Description:  "第二十八课 常青树"



# """
# 常青树个人版本
# """

# import turtle

# t = turtle.Turtle()
# t.speed(0)
# t.ht()
# t.pensize(2)
# t.lt(180)

# #画树冠
# for x in range(1,4):
#     t.penup()
#     t.goto(0,x*35) #(0+(10*x)
#     t.pendown()
#     t.color("black","green")

#     t.begin_fill()
#     t.circle(100-(x*15),steps=3) #(100-(x*10)
#     t.end_fill()

# #画树干
# t2 = turtle.Turtle()
# t2.speed(10)
# t2.ht()
# t2.pensize(2)
# t2.penup()
# t2.goto(25,-93) #(0+(10*x)
# t2.pendown()

# t2.color("black","gray")
# t2.begin_fill()
# for x in range(2):
#     t2.rt(90)
#     t2.fd(100)
#     t2.rt(90)
#     t2.fd(45)
# t2.end_fill()








import turtle

t = turtle.Turtle()
t.ht()
t.pensize(4)

#树干
t.penup()
t.goto(-15,0)
t.pendown()
t.fillcolor("#955741")
t.begin_fill()
t.fd(30)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(50)
t.end_fill()
t.right(90)

#树冠
t.fillcolor("#3d8442")  #树冠的颜色

#第一层树冠
t.penup()
t.goto(-60,0)
t.pendown()
t.begin_fill()
for x in range(3):
    t.fd(120)
    t.lt(120)
t.end_fill()

#第二层树冠
t.penup()
t.goto(-50,40)
t.pendown()
t.begin_fill()
for x in range(3):
    t.fd(100)
    t.lt(120)
t.end_fill()

#第三层树冠
t.penup()
t.goto(-40,80)
t.pendown()
t.begin_fill()
for x in range(3):
    t.fd(80)
    t.lt(120)
t.end_fill()

















turtle.mainloop()
