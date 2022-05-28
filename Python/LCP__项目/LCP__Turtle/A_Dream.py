import turtle

t = turtle.Turtle()
t.speed(10)  #画笔速度
t.pensize(2)
t.ht()  #隐藏画笔

#蓝脸
t.penup()
t.goto(0,-100)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(120)
t.end_fill()
t.color("black")
t.circle(120)

#白脸
t.penup()
t.goto(0,-97)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(100)
t.end_fill()
t.color("black")
t.circle(100)

#嘴
t.penup()
t.goto(-70,-10)
t.pendown()
t.color("black")
t.rt(90)
t.circle(70,180)

#鼻子
t.penup()
t.goto(0,-80)
t.pendown()
t.fd(100)
t.rt(90)
t.color("red")
t.begin_fill()
t.circle(8)
t.end_fill()
t.color("black")
t.circle(8)

#左眼
t.color("black")
t.penup()
t.goto(-45,58)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(26)
t.end_fill()
t.color("black")
t.circle(26)
t.penup()
t.goto(-38,64)
t.pendown()
t.pensize(12)
t.circle(7)

#右眼
t.pensize(2)
t.color("black")
t.penup()
t.goto(45,58)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(26)
t.end_fill()
t.color("black")
t.circle(26)
t.penup()
t.goto(38,64)
t.pendown()
t.pensize(12)
t.circle(7)



turtle.mainloop()