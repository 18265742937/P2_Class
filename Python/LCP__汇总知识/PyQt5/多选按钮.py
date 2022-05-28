from VipCode import *  # *代表全部的意思

class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(650, 500)
        self.setWindowTitle("小窗口 !")
        self.setBackgroundColor("#7FFFD4")
        self.Multiple_buttons("哈哈哈", 100, 100)
        self.bt.stateChanged.connect(self.Button_status)

    # 创建多选按钮
    def Multiple_buttons(self, text,x,y):
        # 添加多选按钮
        self.bt = QCheckBox(text, self)
        # 位置移动
        self.bt.move(x,y)

    # 获取多选按钮的状态
    def Button_status(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('选中了!')
        else:
            self.setWindowTitle('没选中!')  # python

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec_()






