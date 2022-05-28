# @Author: 茄子 
# @Date: 2019-09-09 16:13:20   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-09 16:13:20  
# @Description:  "第三十四课  微信小表情(一)"



import turtle

#定义类
class Face:
    #定义脸庞的方法
    def draw_face(self):
        t1 = turtle.Turtle()
        t1.speed(0)
        t1.ht()
        t1.circle(100)

    #定义绘制难过表情的方法
    def draw_sad(self):
        #嘴巴
        t2 = turtle.Turtle()
        t2.speed(0)
        t2.ht()
        t2.penup()
        t2.goto(-30,20)
        t2.pendown()
        t2.lt(45)
        t2.fd(40)
        t2.rt(90)
        t2.fd(40)

        #左眼睛
        t2.penup()
        t2.goto(-30,100)
        t2.pendown()
        t2.backward(60)

        #右眼睛
        t2.penup()
        t2.goto(30,100)
        t2.pendown()
        t2.lt(90)
        t2.fd(60)


    # #定义绘制开心表情的方法
    # def draw_happy(self):



    # #定义绘制生气表情的方法
    # def draw_angry(self):







a = Face()   #类实例化
a.draw_face()   #调用方法
a.draw_sad()   #调用方法


















turtle.mainloop()



