from VipCode import *
class Anim_Dialog(PyQt5_QDialog):
    def showDialog(self):
        self.show()
    def setupUI(self):

        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(960, 600)
        # 设置窗口的背景
        self.setBackground("mainBg.png")
        # 第一个足球
        self.ball1 = PyQt5_Qlabel(self,200,300,50,50)
        self.ball1.setBackground("ball.png")
        # 添加开始按钮
        self.button = PyQt5_QPushButton(self,460,500,100,100)
        self.button.setBackground("start.png")
        # 添加开始按钮的点击事件
        self.button.clicked.connect(self.click)
     

    def click(self):
        # 调用足球移动到原位置
        self.ball1.move(200,300)

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