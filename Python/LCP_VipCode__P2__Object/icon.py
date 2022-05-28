# @Author: 茄子
# @Date: 2019-07-30 11:47:08
# @Last Modified by:   茄子
# @Last Modified time: 2019-07-30 11:47:08
# @Description:  "第二课 第一个窗口"


#导入工具
from VipCode import *  # *代表全部的意思

#创建一个类
class Dialog_First(PyQt5_QDialog):
    #定义显示窗口的函数   self代表当前的窗口
    def show_Dialog(self):
        #显示这个窗口
        self.show()

    #定义美化窗口的函数
    def ui_Dialog(self):
        #设置窗口的尺寸,不可拖动更改尺寸 (宽,高)
        # self.setFixedSize(500,500)
        #设置窗口的位置以及尺寸
        self.setGeometry(0, 0, 500, 500)
        #设置窗口的标题
        self.setWindowTitle("我的窗口!")
        #设置窗口的背景
        self.setBackground("mainBg.png")
        #设置背景颜色
        # self.setBackgroundColor("red")
        #设置窗口的图标(icon)
        self.setWindowIcon(QIcon(r"C:\Users\LCP\Desktop\love.ico"))


#程序的入口(大门)
if __name__ == "__main__":
    #通过QApplication来创建程序
    app = QApplication(sys.argv)
    #创建一个窗口类对象
    dialog = Dialog_First()
    #通过对象调用美化窗口的函数
    dialog.ui_Dialog()
    #通过对象去调用显示这个窗口的函数
    dialog.show_Dialog()
    #让程序持续保持运行
    app.exec_()
