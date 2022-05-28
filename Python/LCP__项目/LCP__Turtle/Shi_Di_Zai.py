from turtle import *

setup(650,650)
penup()
pensize(5)
speed(10)
pencolor("#065693")
seth(180)
fd(140)
seth(-90)
fd(50)
pendown()      #起点
fillcolor("#0079C6")
begin_fill()
seth(170)
circle(-40,100)
seth(180)
fd(50)
seth(180)
circle(-10,46)
seth(130)
circle(-300,40)#耳朵外廓大圆
circle(-100,45)
right(10)
circle(-50,30)
right(10)
circle(-30,30)
left(1)
fd(2)
right(1)
fd(3)
right(4)
fd(3)
right(3)
fd(5)
right(4)
fd(6)
right(4)
fd(10)
right(4)
fd(10)
right(3)
fd(15)
right(2)
fd(20)
right(2)
fd(20)
right(4)
fd(20)
right(3)
fd(30)
right(1)
fd(40)
right(1)
fd(60)
seth(-115)
fd(5)    #脸左侧开始逆时针
circle(200,30)
end_fill()
begin_fill()
left(8)
fd(20)
left(10)
fd(20)
left(14)
circle(100,30)
left(10)
circle(150,20)
right(2)
fd(55)
left(5)
fd(40)
left(3)
fd(25)
right(3)
circle(150,20)
left(7)
circle(100,30)
fd(5)#右侧耳朵下部开始
left(3)
circle(80,30)
right(3)
circle(80,30)
right(9)
circle(100,30)
left(2)
circle(200,20)
left(3)
fd(20)
seth(108)#小毛尖儿1
circle(30,5)
right(3)
circle(200,3)
left(7)
circle(20,5)
circle(15,10)
left(5)
circle(15,20)
left(11)
circle(15,20)
left(10)
circle(15,20)
left(9)
circle(13,15)
left(10)
circle(13,15)
left(8)
circle(20,15)
seth(135)  #小毛尖2
fd(20)
circle(8,168)
right(180)  #小毛尖3
circle(7,170)
seth(-176) #顶部结尾
fd(3)
circle(100,10)
right(5)
circle(70,15)
fd(3)
right(5)
circle(100,10)
right(4)
circle(80,10)
left(5)
circle(100,5)
right(6)
circle(100,5)
left(1)
circle(50,10)
right(10)
fd(9)
seth(-115)
fd(5)
circle(200,30)
end_fill() #脸廓结束
penup()    #眼睛左开始
seth(0)
fd(15)
seth(-60)
pendown()
fillcolor("#69C4EF")
begin_fill()
circle(50,20)
left(4)
circle(55,20)
right(4)
circle(50,20)
right(4)
circle(50,20)
left(13)
circle(50,20)
left(15)
circle(50,30)
right(10)
circle(80,20)
right(10)
circle(80,20)
right(7)
circle(80,20)
left(10)
circle(80,15)
left(17)
circle(80,15)
left(30)
circle(80,15)
left(10)
circle(80,15)
circle(80,15)
right(8)
circle(80,15)
right(7)
circle(80,15)
right(7)
circle(80,6)
end_fill()
penup()   #左眼内部(黑)开始
seth(0)
fd(34)
seth(90)
fd(10)
seth(-60)
pendown()
fillcolor("black")
begin_fill()
pencolor("black")
pensize(1)
circle(80,7)
left(20)
circle(80,9)
left(25)
circle(80,9)
left(30)
circle(80,9)
left(35)
circle(80,9)
left(10)
circle(80,3)
right(15)
fd(13)
left(15)
circle(80,10)
left(20)
circle(80,15)
left(25)
circle(80,10)
left(30)
circle(80,9)
left(35)
circle(80,15)
left(10)
circle(80,9)
circle(80,15)
end_fill() #左眼内部（黑）结束
penup()  #左眼内部（白）开始
seth(90)
fd(47)
seth(0)
fd(12)
pendown()
fillcolor("white")
begin_fill()
circle(-10,360)
end_fill() #左眼整体结束
penup()    #右眼开始
seth(0)
fd(237)
seth(-90)
pensize(5)
pencolor("#065693")
fillcolor("#69C4EF")
begin_fill()
pendown()
right(10)
circle(80,11)
right(30)
circle(80,11)
right(35)
circle(80,15)
right(35)
circle(80,12)
right(20)
circle(80,9)
right(37)
circle(80,9)
right(40)
circle(80,9)
right(38)
circle(80,9)
right(15)
circle(80,9)
fd(7)
right(11)
circle(80,9)
right(11)
circle(80,9)
right(12)
circle(80,9)
right(14)
circle(80,9)
right(16)
circle(80,5)
right(16)
circle(80,5)
right(18)
circle(80,5)
right(23)
circle(80,5)
right(25)
circle(80,5)
right(28)
circle(80,5)
right(5)
circle(80,5)
right(12)
circle(80,5)
right(15)
circle(80,5)
right(17)
circle(80,5)
right(15)
circle(80,5)
right(13)
circle(80,5)
right(13)
circle(80,9)
right(11)
circle(80,9)
right(11)
circle(80,5)
right(10)
circle(80,5)
right(10)
circle(80,9)
end_fill() #右眼外框结束
penup()    #右眼内部开始
seth(180)
fd(70)
seth(87)
pensize(1)
pencolor("black")
fillcolor("black")
begin_fill()
pendown()
circle(80,8)
right(15)
circle(80,7)
right(18)
circle(80,5)
right(23)
circle(80,5)
right(23)
circle(80,5)
right(23)
circle(80,5)
right(28)
circle(80,5)
right(35)
circle(80,5)
right(35)
circle(80,6)
right(37)
circle(80,6)
fd(5)
left(5)
circle(80,5)
right(3)
fd(5)
right(10)
circle(80,5)
right(15)
circle(80,5)
right(18)
circle(80,5)
right(25)
circle(80,5)
right(37)
circle(80,5)
right(38)
circle(80,7)
right(42)
circle(80,9)
right(38)
circle(80,9)
right(40)
fd(5)
end_fill()
penup() #右眼内部（白）开始
seth(0)
fd(22)
seth(90)
fd(10)
pendown()
pensize(1)
pencolor("white")
fillcolor("white")
begin_fill()
circle(10,360)
end_fill()#右眼内部（白）结束
penup()   #鼻子外开始
seth(180)
fd(167)
seth(-90)
fd(60)
pencolor("#07548C")
seth(0)
pendown()
fillcolor("#07548C")
begin_fill()
left(83)
circle(-80,30)
right(15)
circle(-80,30)
fd(5)
left(2)
circle(-80,15)
circle(-80,10)
circle(-80,20)
left(2)
circle(-80,9)
right(20)
circle(-80,20)
right(25)
circle(-80,20)
right(10)
circle(-80,15)
right(8)
circle(-80,12)
seth(-175)
fd(9)
left(2)
fd(6)
left(2)
fd(8)
right(3)
circle(-80,10)
right(3)
circle(-80,12)
circle(-80,10)
right(3)
circle(-80,10)
right(7)
circle(-80,10)
right(6)
circle(-80,8)
right(6)
circle(-80,8)
right(7)
circle(-80,7)
end_fill()#鼻子外结束
penup()#鼻子内开始
seth(8)
fd(20)
seth(-90)
fd(45)
pensize(1)
pencolor("#0A3873")
pendown()
fillcolor("#0A3873")
begin_fill()
seth(-30)
fd(20)
seth(110)
fd(20)
left(70)
circle(10,100)
end_fill()
penup()
seth(3)
fd(87)
seth(-90)
fd(5)
seth(47)
begin_fill()
pendown()
fd(20)
seth(227)
fd(20)
right(150)
fd(20)
right(70)
circle(-10,100)
end_fill()#鼻子结束
penup()#右耳朵开始
seth(0)
fd(95)
seth(90)
fd(45)
pendown()
fillcolor("#0079C6")
begin_fill()
pensize(5)
pencolor("#065693")
seth(20)
circle(40,95)
right(100)
fd(50)
circle(10,46)
seth(45)
circle(300,40)
circle(100,45)
left(10)
circle(50,30)
left(10)
circle(30,30)
right(1)
fd(2)
left(1)
fd(3)
left(4)
fd(3)
left(3)
fd(5)
left(4)
fd(6)
left(4)
fd(10)
left(4)
fd(10)
left(3)
fd(15)
left(2)
fd(20)
left(2)
fd(20)
left(4)
fd(20)
left(3)
fd(30)
left(1)
fd(40)
left(1)
fd(60)
left(3)
fd(51)
left(70)
pensize(1)
fd(8)
right(3)
fd(8)
right(3)
fd(8)
right(3)
fd(5)
right(3)
fd(5)
right(2)
fd(5)
right(2)
fd(5)
right(3)
fd(9)
right(3)
fd(10)
right(3)
fd(9)
right(5)
fd(9)
right(6)
fd(6)
right(6)
fd(6)
right(7)
fd(6)
right(7)
fd(6)
end_fill()#右耳朵外廓完成
penup()#右耳内廓开始
seth(0)
fd(6)
seth(90)
fd(20)
seth(45)
pendown()
pensize(1)
pencolor("#F7CEDC")
fillcolor("#F7CEDC")
begin_fill()
circle(40,75)
right(106)
fd(53)
circle(10,40)
seth(47)
circle(310,40)
left(10)
circle(80,45)
left(25)
circle(40,30)
left(23)
circle(30,20)
seth(-145)
right(1)
fd(2)
left(1)
fd(3)
left(4)
fd(3)
left(3)
fd(5)
left(4)
fd(6)
left(4)
fd(10)
left(4)
fd(10)
left(3)
fd(15)
left(2)
fd(20)
left(2)
fd(20)
left(3)
fd(20)
left(2)
fd(30)
left(2)
fd(30)
left(2)
fd(40)
left(3)
fd(30)
left(1)
fd(7)
left(2)
fd(7)
left(12)
fd(2)
left(8)
fd(20)
left(10)
fd(10)
left(15)
fd(10)
right(2)
fd(20)
right(10)
fd(15)
right(8)
fd(10)
end_fill()#右耳内廓结束
penup()
seth(180)
fd(327)
seth(-90)
fd(34)
pendown()
begin_fill()
seth(140)
circle(-40,75)
left(113)
fd(53)
circle(-7,40)
seth(130)
circle(-310,40)
right(17)
circle(-80,45)
right(20)
circle(-40,30)
right(23)
circle(30,20)
seth(-47)
left(3)
fd(2)
right(2)
fd(3)
right(2)
fd(3)
right(3)
fd(5)
right(4)
fd(6)
right(4)
fd(10)
right(4)
fd(10)
right(3)
fd(15)
right(1)
fd(20)
right(1)
fd(20)
right(1)
fd(30)
right(1)
fd(40)
right(1)
fd(40)
right(11)
fd(2)
right(15)
left(20)
right(10)
fd(20)
right(15)
fd(10)
left(5)
fd(20)
right(5)
fd(20)
left(10)
fd(20)
left(3)
fd(20)
end_fill()#脸部结束
penup()#身体开始
seth(0)
fd(70)
seth(-90)
fd(80)
pensize(5)
pencolor("#065693")
fillcolor("#0079C6")
begin_fill()
seth(-112)
pendown()
circle(220,22)
right(86)
circle(70,40)
right(90)
fd(8)
right(33)
circle(10,160)
right(9)
fd(8)
right(50)
fd(9)
right(28)
fd(6)
circle(8,160)
left(5)
fd(6)
right(85)
fd(9)
right(28)
fd(6)
circle(6,110)
fd(4)
right(23)
fd(5)
left(2)
circle(80,10)
left(2)
circle(80,5)
left(4)
circle(80,10)
left(7)
circle(80,10)
left(7)
circle(80,10)
right(2)
fd(5)
right(1)
circle(80,10)
left(4)
circle(80,10)
right(10)
circle(-80,10)
right(8)
circle(-80,10)
right(11)
circle(-80,10)
right(90)
fd(5)
right(5)
circle(10,180)
fd(2)
right(130)
fd(5)
left(5)
circle(10,130)
fd(5)
right(80)
fd(5)
circle(10,180)
seth(0)
fd(65)
right(180)
circle(10,190)
fd(5)
right(90)
fd(5)
circle(10,150)
left(10)
fd(5)
right(90)
fd(2)
circle(10,180)
right(20)
fd(3)
right(125)
circle(-80,10)
right(11)
circle(-80,10)
right(8)
circle(-80,10)
right(10)
circle(80,10)
left(4)
circle(80,10)
right(1)
fd(5)
right(2)
circle(80,10)
left(7)
circle(80,10)
left(7)
circle(80,10)
left(4)
circle(80,5)
left(2)
circle(80,10)
left(2)
fd(5)
right(23)
fd(4)
circle(6,110)
fd(6)
right(28)
fd(9)
right(85)
fd(6)
left(5)
circle(8,160)
fd(6)
right(28)
fd(9)
right(50)
fd(8)
right(9)
circle(10,160)
right(33)
fd(8)
right(90)
circle(70,40)
right(92)
circle(210,22)
fd(16)#身体外廓结束
left(90)
circle(-80,5)
right(1)
circle(-80,5)
right(1)
circle(80,5)
right(1)
circle(80,5)
right(2)
fd(5)
right(1)
fd(5)
right(1)
fd(5)
right(3)
fd(5)
right(2)
fd(5)
right(3)
fd(7)
right(2)
fd(7)
right(2)
fd(7)
left(2)
fd(5)
left(2)
fd(7)
right(3)
fd(7)
left(2)
fd(7)
right(2)
fd(7)
left(2)
fd(7)
right(2)
fd(7)
left(2)
fd(7)
right(2)
fd(7)
left(2)
fd(7)
right(2)
fd(7)
left(2)
fd(7)
right(5)
fd(7)
left(2)
fd(7)
right(7)
fd(7)
left(2)
fd(7)
right(8)
fd(6)
end_fill()#身体外廓结束
penup()#身体内部开始
seth(0)
fd(48)
right(65)
pendown()
fillcolor("#69C4EF")
begin_fill()
circle(-300,24)
circle(10,90)
seth(0)
fd(50)
circle(10,90)
left(9)
circle(-300,26)
fd(3)
seth(-167)
fd(5)
right(1)
fd(7)
left(1)
fd(7)
right(2)
fd(7)
left(1)
fd(7)
right(3)
fd(7)
left(2)
fd(7)
right(3)
fd(7)
right(3)
fd(7)
left(2)
fd(7)
right(4)
fd(7)
left(2)
fd(7)
right(3)
fd(7)
left(2)
fd(7)
right(2)
fd(7)
left(3)
fd(7)
left(3)
fd(5)
end_fill()#身体外廓中间结束
penup()
seth(-90)
fd(154)
seth(0)
fd(4)
pensize(1)
fillcolor("#065693")
pencolor("#065693")
pendown()
begin_fill()
seth(-155)
fd(8)
right(120)
fd(8)
right(90)
circle(-10,50)
end_fill()
penup()
seth(0)
fd(16)
seth(-120)
pendown()
fd(8)
begin_fill()
right(113)
fd(8)
right(90)
circle(-10,57)
end_fill()
penup()
seth(0)
fd(10)
seth(90)
fd(10)
pendown()
begin_fill()
seth(-45)
fd(8)
right(120)
fd(8)
right(90)
circle(-10,57)
end_fill()
penup()
seth(0)
fd(72)
seth(-90)
fd(2)
seth(-115)
pendown()#
begin_fill()
fd(8)
left(90)
circle(10,57)
end_fill()
penup()
seth(0)
fd(4)
seth(-90)
fd(6)
seth(-70)
pendown()
begin_fill()
fd(8)
left(90)
circle(10,57)
end_fill()
penup()
seth(0)
fd(4)
seth(90)
fd(5)
seth(0)
pendown()
begin_fill()
fd(8)
left(90)
circle(10,57)
end_fill()#手结束
penup()#左脚掌开始
seth(180)
fd(237)
seth(-90)
fd(10)
seth(180)
pendown()
fillcolor("#065693")
begin_fill()
circle(-17,360)
end_fill()#左脚掌结束
seth(180)#左脚丫开始
penup()
fd(20)
seth(90)
fd(7)
seth(180)
right(15)
pendown()
begin_fill()
fd(9)
right(120)
fd(9)
right(120)
fd(9)
end_fill()
penup()
seth(90)
fd(20)
seth(180)
right(53)
pendown()
begin_fill()
fd(9)
right(120)
fd(9)
right(120)
fd(9)
end_fill()
penup()
seth(0)
fd(10)
seth(90)
fd(10)
right(20)
pendown()
begin_fill()
fd(9)
right(120)
fd(9)
right(120)
fd(9)
end_fill()#左脚丫结束
penup()#右脚掌开始
seth(0)
fd(345)
seth(-90)
fd(12)
seth(0)
pendown()
begin_fill()
circle(17,360)
end_fill()#右脚掌结束
penup()#右脚丫开始
fd(23)
seth(90)
fd(4)
seth(0)
left(90)
pendown()
begin_fill()
fd(9)
right(120)
fd(9)
right(120)
fd(9)
end_fill()
penup()
seth(90)
fd(25)
seth(0)
left(127)
pendown()
begin_fill()
fd(9)
right(120)
fd(9)
right(120)
fd(9)
end_fill()
penup()
seth(180)
fd(27)
seth(90)
fd(12)
seth(0)
pendown()
begin_fill()
left(4)
fd(9)
left(120)
fd(9)
left(120)
fd(9)
end_fill()
penup()#右脚丫结束
fd(200)

mainloop()



