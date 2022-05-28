# @Author: 茄子 
# @Date: 2019-09-02 15:31:51   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-02 15:31:51  
# @Description:  "第三十一课 海龟赛跑"


"""
准备工作
"""
import turtle
import random  #导入随机数工具

t = turtle.Turtle()  #创建绘制跑道的画笔
t.goto(-180,-60)  #将画笔移动到指定位置
t.speed(0)  #设置画笔速度
t.color("#ee4000")  #设置跑道的颜色


#绘制长方形跑道
t.begin_fill()
t.fd(360)
t.lt(90)
t.fd(120)
t.lt(90)
t.fd(360)
t.lt(90)
t.fd(120)
t.end_fill()


#绘制跑道分割线
t.lt(90)  #转动画笔
t.penup()
t.goto(-180,0)
t.pendown()
t.color("black")   #确定分割线的颜色
t.pensize(3)
t.fd(360)  #确定分割线的长度
t.ht()  #隐藏画笔


#创建海龟1
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")  #改变海龟的颜色
t1.goto(-180,30)  #确定起跑点
t1.clear()  #清除多余的线条


#创建海龟2
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("yellow")  #改变海龟的颜色
t2.goto(-180,-30)  #确定起跑点
t2.clear()  #清除多余的线条


#投硬币赛跑
x = 0  #海龟1所跑的次数
y = 0  #海龟2所跑的次数
while x < 36 and y < 36:  #当海龟1和海龟2都没有跑道到终点的时候继续投硬币
    r = random.randint(0,1)  #扔硬币, 0代表海龟1跑, 1代表海龟2跑
    if r == 0:   #如果硬币为正面
        t1.fd(10)   #海龟1, 前进10
        t1.clear()  #清除多余线段
        x += 1   #海龟1前进次数加1
    else:
        t2.fd(10)
        t2.clear()
        y += 1


#判断输赢
if x == 36:
    print("海龟1赢了!")
else:
    print("海龟2赢了!")


"""
优化: 能不能在图上显示哪只海龟赢了 !
"""





turtle.mainloop()

