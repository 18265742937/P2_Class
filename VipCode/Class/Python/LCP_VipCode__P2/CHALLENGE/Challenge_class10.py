from VipCode import *

class UI_TiePi(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(400, 600)
        self.title = PyQt5_Qlabel(self, 70, 170, 200, 30)
        self.title.setText("设置窗口标题:")
        self.title.setFont(QFont("手札体-简",18,QFont.Bold))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_TiePi()
    # 设置窗口的属性
    dialog.setupUI()
    # 显示窗口
    dialog.showDialog()
    app.exec_()
