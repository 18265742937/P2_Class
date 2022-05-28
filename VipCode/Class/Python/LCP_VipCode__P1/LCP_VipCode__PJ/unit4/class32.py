import turtle
t = turtle.Turtle()
t.hideturtle()


class Bee():
    pass


b1 = Bee()
b1.name = "皮皮"
b1.kind = "工蜂"
b1.wing = 4
b1.leg = 6


def nest(x,  y):
    t.penup()
    t.goto(x,  y)
    t.pendown()
    for x in range(6):
        t.forward(60)
        t.left(60)


print("这是一只" + b1.kind + b1.name + "。")
nest(0,  0)
nest(80, 90)

b2 = Bee()
b2.name = "大头"
b2.kind = "工蜂"
b2.wing = 4
b2.leg = 6


def honey(x, y):
    t.penup()
    t.goto(x,  y)
    t.pendown()
    t.dot(60, "orange")


print("这是一只" + b2.kind + b2.name + "。")
honey(30,  50)
