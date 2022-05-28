from VipCode import *  # *代表全部的意思

class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(650, 500)
        self.setWindowTitle("小窗口 !")
        self.setBackgroundColor("#7FFFD4")
        self.addLabel(0, 0, 200, 200, "background.png")

    #添加标签(label)
    def addLabel(self, x, y, width, till, back_picture):
        # 设置标签组件的(位置)和(尺寸)
        self.lable = PyQt5_Qlabel(self, x, y, width, till)
        # 给标签添加背景图片
        self.lable.setBackground(back_picture)
        # 添加背景颜色
        # self.lable.setBackgroundColor(back_color)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec_()
