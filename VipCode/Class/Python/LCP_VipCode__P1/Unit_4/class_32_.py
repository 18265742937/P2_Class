# @Author: 茄子 
# @Date: 2019-09-02 16:19:42   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-02 16:19:42  
# @Description:  "第三十二课 常青树森林"

import turtle

class Tree:
    def draw_tree(self,x,y):
        t = turtle.Turtle()
        #树干
        t.ht()
        t.penup()
        t.goto(x,y)
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
        t.fillcolor("#3d8442")
        t.begin_fill()
        t.fd(80)
        t.lt(120)
        t.fd(130)
        t.lt(120)
        t.fd(130)
        t.lt(120)
        t.fd(50)
        t.end_fill()




tree1 = Tree()   #创建对象
tree1.draw_tree(10,100)   #通过对象调用类中的函数
tree2 = Tree()   #创建对象
tree2.draw_tree(30,50)   #通过对象调用类中的函数
tree3 = Tree()   #创建对象
tree3.draw_tree(-80,20)   #通过对象调用类中的函数


turtle.mainloop()













"""
1, 什么是类?  是具有相同属性, 相同行为特征的,某一种类的事物;  是一个统称, 不代表单一事物, 而是代表一个群体;

2, 创建一个类的格式:
class 类型:
    类的内容

3, 什么是对象?  就是给类名起一个名字, 就是创建一个对象了!

4, self
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，
self 代表的是类的实例
"""


