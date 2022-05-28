# @Author: 茄子 
# @Date: 2019-09-09 16:50:25   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-09 16:50:25  
# @Description:  "第三十五课  微信小表情(二)"


import turtle  #导入工具, 需要最上边

class Face:  #创建一个类

    def get_pen(self):  #创建一个方法   #必须加self
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.pensize(2)
        return t

    def draw_face_circle(self, x, y):  # 画圆脸，(x,y)为笔的坐标
        t = self.get_pen()
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.circle(30)
        return x - 20, y + 43

    def draw_face_square(self, x, y):  # 画方脸
        t = self.get_pen()
        t.right(45)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.circle(50, steps=4)
        return x + 15, y + 48

    def draw_eyes_happy(self, x, y):  # 高兴眼睛
        t = self.get_pen()
        t.penup()
        t.goto(x + 10, y - 8)
        t.pendown()
        t.begin_fill()
        t.circle(4)
        t.end_fill()
        t.penup()
        t.goto(x + 30, y - 8)
        t.pendown()
        t.begin_fill()
        t.circle(4)
        t.end_fill()

    def draw_eyes_angry(self, x, y):  # 生气眼睛
        t = self.get_pen()
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x + 15, y - 15)
        t.penup()
        t.goto(x + 25, y - 15)
        t.pendown()
        t.goto(x + 40, y)

    def draw_eyes_sad(self, x, y):  # 哀伤眼睛
        t = self.get_pen()
        t.penup()
        t.goto(x, y - 5)
        t.pendown()
        t.goto(x + 15, y + 2)
        t.penup()
        t.goto(x + 5, y - 10)
        t.pendown()
        t.goto(x + 10, y - 7)
        t.penup()
        t.goto(x + 25, y + 2)
        t.pendown()
        t.goto(x + 40, y - 5)
        t.penup()
        t.goto(x + 30, y - 7)
        t.pendown()
        t.goto(x + 35, y - 10)

    def draw_eyes_arrogant(self, x, y):  # 傲慢眼睛
        t = self.get_pen()
        t.penup()
        t.goto(x + 5, y - 10)
        t.pendown()
        t.circle(10)
        t.penup()
        t.goto(x + 8, y - 1)
        t.pendown()
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()
        t.goto(x + 30, y - 10)
        t.pendown()
        t.circle(10)
        t.penup()
        t.goto(x + 33, y - 1)
        t.pendown()
        t.begin_fill()
        t.circle(5)
        t.end_fill()

    def draw_mouth_happy(self, x, y):  # 高兴嘴巴
        t = self.get_pen()
        t.penup()
        t.goto(x + 5, y - 23)
        t.right(45)
        t.pendown()
        t.circle(20, 100)

    def draw_mouth_angry(self, x, y):  # 生气嘴巴
        t = self.get_pen()
        t.penup()
        t.goto(x + 10, y - 35)
        t.pendown()
        t.goto(x + 20, y - 22.5)
        t.goto(x + 30, y - 35)

    def draw_mouth_sad(self, x, y):  # 哀伤嘴巴
        t = self.get_pen()
        t.penup()
        t.goto(x + 30, y - 25)
        t.left(160)
        t.pendown()
        t.circle(25, 40)

    def draw_mouth_arrogant(self, x, y):  # 傲慢嘴巴
        t = self.get_pen()
        t.penup()
        t.goto(x + 32, y - 20)
        t.pendown()
        t.right(180)
        t.circle(30, 50)
        t.penup()
        t.goto(x + 35, y - 26)
        t.pendown()
        t.goto(x + 30, y - 26)
#括号里面的都叫参数, 参数使用逗号分隔        
face = Face()   #创建对象  face是对象名
face.draw_face_square(0,0)  #通过对象名来调用方法, 并传入参数
face.draw_mouth_sad(15,40)
face.draw_eyes_arrogant(19,40)



turtle.mainloop()













