from VipCode import *

class Anim_Dialog(PyQt5_QDialog):
    def showDialog(self):
        self.show()
    def setupUI(self):
        self.setFixedSize(1000,600)
        # 设置窗口的背景
        self.setBackground("background.png")



if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建窗口
    dialog =Anim_Dialog()
    # 设置窗口的属性
    dialog.setupUI()
    # 显示窗口
    dialog.showDialog()
    # 保持应用运行
    app.exec_()