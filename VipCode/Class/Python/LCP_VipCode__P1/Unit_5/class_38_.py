# @Author: 茄子 
# @Date: 2019-09-09 18:44:44   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-09 18:44:44  
# @Description:  "第三十八课  时钟(二)"


import turtle
from time import localtime, strftime


class Watch:
    def draw_watchPlate(self):
        t = turtle.Turtle()
        t.ht()
        t.speed(0)
        t.width(5)
        t.up()
        t.goto(0, -100)
        t.down()
        t.circle(100)
        t.up()
        t.goto(0, 0)
        t.width(3)
        t.up()
        t.goto(0, 0)
        t.width()
        for x in range(12):
            t.fd(70)
            t.down()
            t.fd(30)
            t.up()
            t.back(100)
            t.right(30)

    def draw_watchHand(self):
        t1 = turtle.Turtle()
        t1.ht()
        t1.speed(0)
#开始----------------------------------------
        t1.seth(90)
        t2 = turtle.Turtle()
        t2.ht()
        t2.speed(0)
        t2.seth(90)
        t2.width(2)
        t3 = turtle.Turtle()
        t3.ht()
        t3.speed(0)
        t3.width(3)
        t3.seth(90)
        tt = strftime('%I:%M:%S', localtime())
        ts = tt.split(':')
        h = int(ts[0])
        m = int(ts[1])
        s = int(ts[2])
        t1.up()
        t1.right(s * 6)
        t1.fd(60)
        t1.st()
        t2.right(m * 6)
        t2.fd(50)
        t3.right(h * 30 + m * 0.5)
        t3.fd(30)
#开始------------------------------------

a = Watch()
a.draw_watchPlate()
a.draw_watchHand()








turtle.mainloop()






