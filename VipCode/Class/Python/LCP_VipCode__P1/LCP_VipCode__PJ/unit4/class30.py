import turtle

t = turtle.Turtle()
t.speed(0)

#绘制一个小方块的函数


def pixel(x, y, color):
    t.pencolor("black")
    t.fillcolor(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for x in range(4):
        t.fd(50)
        t.lt(90)
    t.end_fill()


# #绘制三个小方块的函数
# def T():
#     pixel(0,0,"red")
#     pixel(50,0,"red")
#     pixel(100,0,"red")
#     pixel(50,50,"red")

# T()


#绘制三个小方块的函数(优化版本)
def T(x, y, color):
    pixel(x, y, color)
    pixel(x+50, y, color)
    pixel(x+100, y, color)
    pixel(x+50, y+50, color)


#调用函数
T(-200, 0, "red")
T(-50, 0, "red")
T(100, 0, "red")


turtle.mainloop()

