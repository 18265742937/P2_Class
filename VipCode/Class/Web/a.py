from VipCode import *  #*表示所有

# 创建一个类
class Dialog_First(PyQt5_QDialog):  #类的继承
    # 显示窗口的函数
    def show_Dialog(self):
        #显示窗口的指令
        self.show()
    # 美化窗口的函数
    def ui_Dialog(self):
        # 设置窗口的标题
        self.setWindowTitle("小窗口!")


# 程序的入口
if __name__ == "__main__":
    # 通过  QApplication 来创建一个程序
    app = QApplication(sys.argv)
    # 创建对象
    dialog = Dialog_First()
    # 借助对象名去使用函数
    dialog.ui_Dialog()
    # 借助对象名去使用函数
    dialog.show_Dialog()
    # 让程序持续保持运行
    app.exec_()










