# @Author: 茄子 
# @Date: 2019-09-02 14:51:59   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-02 14:51:59  
# @Description:  "第二十九课  函数"


"""
引出函数
"""
#观察三层树冠, 寻找差别, 找到不同带你和相同点

#函数的作用: 将重复的代码封装起来, 多次调用

#函数的格式:
"""
def 函数名(参数,参数,.....):
    需要重复使用的代码
"""


"""
参数:  空号里面的数据就是参数, 参数主要分为形参和实参
"""








"""
常青树课件版本
"""
import turtle

t = turtle.Turtle()
t.ht()
t.pensize(4)


#树干
t.penup()
t.goto(-15,0)
t.pendown()
t.fillcolor("#955741")
t.begin_fill()
t.fd(30)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(50)
t.end_fill()
t.right(90)


#树冠

t.fillcolor("#3d8442")  #树冠的颜色

#创建树冠的函数 (如何创建函数)
def draw_crown(x,y,w):  #括号里面三个形参
    t.penup()
    t.goto(x,y)    
    t.pendown()
    t.begin_fill()
    for x in range(3):
        t.fd(w)
        t.lt(120)
    t.end_fill()

#调用创建树冠的函数 (如何调用函数)
draw_crown(-60,0,120)   #括号里面三个实参
draw_crown(-50,40,100)
draw_crown(-40,80,80)



# #树冠
# #第一层树冠
# t.penup()
# t.goto(-60,0)
# t.pendown()
# t.fillcolor("#3d8442")
# t.begin_fill()
# for x in range(3):
#     t.fd(120)
#     t.lt(120)
# t.end_fill()

# #第二层树冠
# t.penup()
# t.goto(-50,40)
# t.pendown()
# t.begin_fill()
# for x in range(3):
#     t.fd(100)
#     t.lt(120)
# t.end_fill()

# #第三层树冠
# t.penup()
# t.goto(-40,80)
# t.pendown()
# t.begin_fill()
# for x in range(3):
#     t.fd(80)
#     t.lt(120)
# t.end_fill()















