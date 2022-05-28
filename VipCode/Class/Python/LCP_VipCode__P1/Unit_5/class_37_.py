# @Author: 茄子 
# @Date: 2019-09-09 18:34:11   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-09 18:34:11  
# @Description:  "第三十七课  时钟(一)"


import turtle
from time import localtime, strftime

class Watch:

    #绘制表盘的方法
    def draw_watchPlate(self):
        t = turtle.Turtle()
        t.ht()
        t.speed(0)
        t.width(5)
        t.up()
        t.goto(0,-100)
        t.down()
        t.circle(100)
        t.up()
        t.goto(0,0)
        t.width(3)
        t.up()
        t.goto(0,0)
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
        t1.up()
        t1.goto(-14,-5)
        t1.down()
        tt = strftime("%I:%M:%S",localtime())
        t1.write(tt)


a = Watch()
a.draw_watchPlate()
a.draw_watchHand()








turtle.mainloop()









