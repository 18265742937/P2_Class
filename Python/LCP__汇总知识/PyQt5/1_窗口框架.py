#导入工具
from VipCode import *  # *代表全部的意思


#创建一个类
class Dialog_First(PyQt5_QDialog):
    #定义显示窗口的函数   self代表当前的窗口
    def show_Dialog(self):
        #显示这个窗口
        self.show()


#程序的入口(大门)
if __name__ == "__main__":
    #通过QApplication来创建程序
    app = QApplication(sys.argv)
    #创建一个窗口类对象
    dialog = Dialog_First()
    #通过对象去调用显示这个窗口的函数
    dialog.show_Dialog()
    #让程序持续保持运行
    app.exec_()

   