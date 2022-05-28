#导入工具
from VipCode import *  # *代表全部的意思

#创建一个类
class Dialog_Second(PyQt5_QDialog):  #修改类名---------------------------------------
    #定义显示窗口的函数   self代表当前的窗口
    def show_Dialog(self):
        #显示这个窗口
        self.show()

#程序的入口(大门)
if __name__ == "__main__":
    #通过QApplication来创建程序
    app = QApplication(sys.argv)
    #创建一个窗口类对象
    dialog = Dialog_Second()  #修改类名----------------------------------------------
    #通过对象去调用显示这个窗口的函数
    dialog.show_Dialog()
    #让程序持续保持运行
    app.exec_()


    #模块
    """
    import turtle  导入海龟模块
    from random import randint  从随机数模块导入随机整数函数   
    什么是模块?   模块就是一个  .py文件



    """