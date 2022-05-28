# @Author: 茄子 
# @Date: 2019-09-09 18:47:12   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-09 18:47:12  
# @Description:  "第三十九课  时钟(三)"


import turtle
from time import localtime, strftime, sleep   #添加代码-------------------------
#开始------------------------------
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
#结束------------------------------
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
        for x in range(12):
            t.fd(70)
            t.down()
            t.fd(30)
            t.up()
            t.back(100)
            t.right(30)
    def draw_watchHand(self):
        #t1 = turtle.Turtle()
        t1.ht()
        t1.speed(0)
        t1.seth(90)
        #t2 = turtle.Turtle()
        t2.ht()
        t2.speed(0)
        t2.seth(90)
        t2.width(2)
        #t3 = turtle.Turtle()
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

#开始----------------------------------------
    def start(self):
        while True:
            tt = strftime("%I:%M:%S", localtime())
            ts = tt.split(":")
            h = int(ts[0])
            m = int(ts[1])
            s = int(ts[2])
            t1.seth(90)
            t1.up()
            t1.goto(0, 0)
            t1.right(s*6)
            t1.fd(60)
            t1.st()
            if s == 0:
                t2.clear()
                t3.clear()
                t2.seth(90)
                t2.up()
                t2.goto(0, 0)
                t2.right(m*6)
                t2.down()
                t2.fd(50)
                t3.seth(90)
                t3.up()
                t3.goto(0, 0)
                t3.right(h*30+m*0.5)
                t3.down()
                t3.fd(30)
            sleep(1)
            t1.ht()


a = Watch()
a.draw_watchPlate()
a.draw_watchHand()
a.start()

