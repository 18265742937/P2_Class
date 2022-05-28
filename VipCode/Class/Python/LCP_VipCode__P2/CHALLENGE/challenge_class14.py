from VipCode import *

class UI_Challenge(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(600, 400)
        # 设置窗口的标题
        self.setWindowTitle("挑战")
        # 设置窗口的背景
        self.setBackground("challengeBg_14.png")

        # 添加问题标签控件， 设置位置以及大小
        self.label = PyQt5_Qlabel(self, 200, 50, 475, 45)
        # 给问题标签添加文字
        self.label.setText("以下哪位诗人被称为诗仙？")
        self.label.setFontSize(18)


if __name__ == '__main__':
    #创建一个应用
    app = QApplication(sys.argv)
    # 创建类对象
    dialog = UI_Challenge()
    # 调用美化窗口方法
    dialog.setupUI()
    # 显示窗口
    dialog.showDialog()
    #让应用一直保持运行状态
    app.exec_()

