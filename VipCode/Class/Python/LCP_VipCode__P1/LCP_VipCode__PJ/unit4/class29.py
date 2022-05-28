import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)


def pixel():
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()


#左眼
t.color("grey")
t.penup()
t.goto(-150, 0)
pixel()

t.color("black")
t.penup()
t.goto(-100, 0)
pixel()

#右眼
t.color("black")
t.penup()
t.goto(50, 0)
pixel()

t.color("grey")
t.penup()
t.goto(100, 0)
pixel()


#嘴巴
t.color("brown")
t.penup()
t.goto(-50, -50)
pixel()

t.color("brown")
t.penup()
t.goto(0, -50)
pixel()

t.color("brown")
t.penup()
t.goto(-50, -100)
pixel()

t.color("brown")
t.penup()
t.goto(0, -100)
pixel()
