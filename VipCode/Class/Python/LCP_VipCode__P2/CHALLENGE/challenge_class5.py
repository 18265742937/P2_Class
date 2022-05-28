from VipCode import *

class UI_TiePi(PyQt5_QDialog):

    # 创建窗口的方法
    def showDialog(self):
        self.show()
        
    # 美化窗口的方法
    def setupUI(self):
        # 设置窗口的大小
        self.setFixedSize(400, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口类对象
    dialog = UI_TiePi()
    # 美化窗口的方法
    dialog.setupUI()
    # 显示窗口
    dialog.showDialog()
    # 让应用一直保持运行状态
    app.exec_()
