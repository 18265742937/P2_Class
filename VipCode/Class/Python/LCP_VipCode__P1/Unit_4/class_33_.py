# @Author: 茄子 
# @Date: 2019-09-09 16:02:36   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-09 16:02:36  
# @Description:  "第三十三课  百变常青树"





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
        t.fd(55)
        t.lt(36)
        t.begin_fill()
        t.circle(70,steps=5)
        t.end_fill()




tree1 = Tree()   #创建对象
tree1.draw_tree(10,100)   #通过对象调用类中的函数
tree2 = Tree()   #创建对象
tree2.draw_tree(30,50)   #通过对象调用类中的函数
tree3 = Tree()   #创建对象
tree3.draw_tree(-80,20)   #通过对象调用类中的函数


turtle.mainloop()













