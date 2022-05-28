from VipCode import *

class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(555, 555)
        self.setWindowTitle("茄子最棒 !")
        self.setBackground("mainBg.png")
        #添加文本框
        self.create_textbox(20, 180, 280, 40)
        #添加按钮
        self.add_button(20, 80, 50, 50)
        self.button.setText("按钮")
        self.button.setBackgroundColor("pink")
        #连接函数
        self.button.clicked.connect(self.on_click)

    #添加按钮函数
    def add_button(self, x, y, w, h):
        self.button = PyQt5_QPushButton(
            self, x, y, w, h)  # 设置按钮的位置和大小 (self,x,y,宽,高)

    #添加文本框的函数(单行文本框)
    def create_textbox(self, x, y, w, h):
        #创建文本框的函数
        self.textbox = QLineEdit(self)
        #设置文本框位置
        self.textbox.move(x, y)
        #设置文本框尺寸
        self.textbox.resize(w, h)

    #弹窗函数
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, "Message", '内容: ' +
                             textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        #打印完毕之后清空文本框
        self.textbox.setText('')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec()