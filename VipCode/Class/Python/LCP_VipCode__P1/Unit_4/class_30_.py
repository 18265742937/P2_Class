# @Author: 茄子 
# @Date: 2019-09-02 15:14:55   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-02 15:14:55  
# @Description:  "第三十课 五彩多边形"



# """
# 创建一个函数用来绘制多边形 (课件版本)
# """
# import turtle

# t = turtle.Turtle()

# #创建函数
# def draw(s,c):   #s代表多边型的边数, c代表画笔的颜色
#     t.color(c)  #改变画笔的颜色
#     for i in range(s):  #根据多边形的边数确定循环次数
#         t.fd(120)  #多边形边长
#         t.lt(360/s)  #转角多少度

# #调用函数
# draw(5,"blue")






# """
# 创建一个函数用来绘制多边形 (个人版本)
# """
# import turtle

# t = turtle.Turtle()

# #创建函数
# def draw2(s,c):  #s代表多边型的边数, c代表画笔的颜色
#     t.color(c)
#     t.circle(100,steps=s)

# #调用函数
# draw2(5,"blue")










# """
# 创建一个函数用来绘制多边形 (课件输入升级版本)
# """
# import turtle

# t = turtle.Turtle()
# t.width(5)

# #创建函数
# def draw(s,c):   #s代表多边型的边数, c代表画笔的颜色
#     t.color(c)  #改变画笔的颜色
#     for i in range(s):  #根据多边形的边数确定循环次数
#         t.fd(120)  #多边形边长
#         t.lt(360/s)  #转角多少度

# a = input("请输入您想绘制图形的边数: ")  #边数为int类型
# b = input("请输入您想绘制图形的颜色: ")  #颜色为str类型

# #调用函数
# draw(int(a),b)










