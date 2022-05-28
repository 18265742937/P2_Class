# coding=utf-8

import turtle
from datetime import *  # 导入datetime模块
#准备设置
turtle.screensize(400, 300)  # 设置画布大小
turtle.setup(840, 500)  # 设置主窗口的大小为840*500
#抬起画笔，向前运动一段距离放下


def Skip(step):  # 由于表盘刻度不连续，需频繁抬起画笔，放下画笔
    turtle.penup()  # 落笔
    turtle.forward(step)  # 向当前画笔方向移动"step"像素长度，具体的参数由后面方法传入
    turtle.pendown()  # 提笔

#定义指针几何形状。


def mkHand(name, length):
    turtle.reset()  # 重置turtle状态为初始状态
    Skip(-length * 0.1)  # 调用Skip()方法，移动的长度为"-length*0.1"像素
    turtle.begin_poly()  # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    turtle.forward(length * 1.1)  # 向当前画笔方向移动"length*1.1"像素长度
    turtle.end_poly()  # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    handForm = turtle.get_poly()  # 返回最后记录的多边形。
    turtle.register_shape(name, handForm)  # 注册handForm为合法的turtle外形

#初始化表针和文本对象


def Init():
    global secHand, minHand, hurHand, printer
    turtle.mode("logo")  # 重置Turtle指向北
    mkHand("secHand", 145)  # 建立三个表针Turtle并初始化，设置secHand即秒针长度为135像素
    mkHand("minHand", 120)  # 设置minHand即分针长度为125像素
    mkHand("hurHand", 90)  # 设置hurHand即时针长度为90像素
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")

    for hand in secHand, minHand, hurHand:  # 遍历secHand, minHand, hurHand三个序列
        hand.shapesize(1, 1, 3)  # 设置表征形状大小为3像素
        hand.speed(0)  # 设置表针的速度为0
    printer = turtle.Turtle()  # 建立输出文字Turtle
    printer.hideturtle()  # 隐藏画笔的turtle形状
    printer.penup()  # 下笔


def SetupClock(radius):  # 建立表的外框,表盘半径radius为参数
    turtle.reset()  # 重置turtle状态为初始状态
    turtle.pensize(7)  # 设置画笔的大小为7像素
    turtle.pencolor("#0A0A0A")  # 设置画笔的颜色为黑色
    turtle.fillcolor("green")  # 绘制图形的填充颜色为绿色

#定义一个i值，遍历i值，根据条件画出钟的各个点与1到12的数字
    for i in range(60):  # 创建一个从0到59的整数列表
        Skip(radius)  # 调用Skip()方法，radius为参数
        if i % 5 == 0:  # “%”运算符为返回除法的余数，则如果i除以5余数为0
            turtle.forward(20)  # 向当前画笔方向移动20像素长度
            Skip(-radius - 20)  # 调用Skip()方法，向当前画笔方向移动"-radius-20"像素长度，即效果图中粗的点
            Skip(radius + 20)  # 调用Skip()方法，向当前画笔方向移动"radius + 20"像素长度，即返回原位

            if i == 0:  # 如果i等于0
                # 写下数字12，水平居中，font（字体名称，大小，加粗）为设置字体参数
                turtle.write(int(12), align="center",
                             font=("Courier", 14, "bold"))
            elif i == 30:  # elif语句，当遍历到对应的条件语句后，后面所有的elif和else都不会再被执行。如果i等于30
                Skip(25)  # 调用Skip()方法，向当前画笔方向移动25像素长度
                # 写下数字6，水平居中，font（字体名称，大小，加粗）为设置字体参数
                turtle.write(int(i / 5), align="center",
                             font=("Courier", 14, "bold"))
                Skip(-25)  # 调用Skip()方法，向当前画笔方向移动-25像素长度,即返回原位
            elif (i == 25 or i == 35):  # “or”为布尔"或"，如果i等于25，它返回i等于25，否则它返回 i等于35。
                Skip(20)  # 调用Skip()方法，向当前画笔方向移动20像素长度
                # 写下数字5/7，水平居中，font（字体名称，大小，加粗）为设置字体参数
                turtle.write(int(i / 5), align="center",
                             font=("Courier", 14, "bold"))
                Skip(-20)  # 调用Skip()方法，向当前画笔方向移动-20像素长度，即返回原位
            else:
                # 写下数字1、2、3、4、8、9、10、11，水平居中，font（字体名称，大小，加粗）为设置字体参数
                turtle.write(int(i / 5), align="center",
                             font=("Courier", 14, "bold"))
            Skip(-radius - 20)  # 调用Skip()方法，向当前画笔方向移动"-radius-20"像素长度
        else:
            turtle.dot(5)  # 绘制一个指定直径为5的圆点
            Skip(-radius)  # 调用Skip()方法，向当前画笔方向移动"-radius"像素长度
        turtle.right(6)  # 画笔的角度向右转6度
#绘制表针的动态显示


def Tick():
    t = datetime.today()  # 获取时间
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)
    turtle.tracer(False)
    printer.home()
    turtle.tracer(True)
    turtle.ontimer(Tick, 100)  # 100ms后继续调用tick
#定义执行的程序的main（）方法


def main():
    turtle.tracer(True)
#打开/关闭快速绘图动画，并为更新图纸设置延迟，False为不显示绘画过程，True为显示绘画过程
    Init()  # 执行定义的Init()方法
    SetupClock(180)  # 执行定义的SetupClock()方法，设置钟表盘半径参数radius为180
    Tick()  # 执行定义的Tick()方法
    turtle.mainloop()  # 启动事件循环


if __name__ == "__main__":
    main()  # 执行定义的main()方法
