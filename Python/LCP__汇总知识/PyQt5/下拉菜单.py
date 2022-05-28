from VipCode import *  # *代表全部的意思


class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(650, 500)
        self.setWindowTitle("小窗口 !")
        self.setBackgroundColor("#7FFFD4")
        self.addLabel(200,200,40,40,"Language")
        self.down_menu(100, 100)
        self.mn.addItem("Python")
        self.mn.addItem("C++")
        self.mn.addItem("C#")
        self.mn.addItem("Java")
        self.mn.addItem("Linux")
        self.mn.activated[str].connect(self.onActivated)

    # 添加下拉菜单
    def down_menu(self,x,y):
        self.mn = QComboBox(self)
        self.mn.move(x,y)
        

    def addLabel(self, x, y, width, till, text):
        self.lable = PyQt5_Qlabel(self, x, y, width, till)
        self.lable.setText(text)

    # 接收下拉菜单的返回
    def onActivated(self,text):
        self.lable.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec_()
