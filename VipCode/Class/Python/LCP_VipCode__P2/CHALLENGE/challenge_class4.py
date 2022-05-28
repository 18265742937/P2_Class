from VipCode import *
import operator


password = [1,2,3,4,5,6]
pwd = []

class UI_TiePi(PyQt5_QDialog):

    def showDialog(self):
        self.show()
    
    def setupUI(self):

        self.setFixedSize(400, 550)
        self.setWindowTitle("模拟手机数字解锁")
        self.setBackground("challengeBg_4.png")

        self.one = PyQt5_QPushButton(self, 65, 150, 57, 57)
        self.one.setBackground("1.png")
        self.one.setPressedBackground("11.png")
        self.one.clicked.connect(lambda:self.ButtonClicked(1))

        self.two = PyQt5_QPushButton(self, 165, 150, 57, 57)
        self.two.setBackground("2.png")
        self.two.setPressedBackground("22.png")
        self.two.clicked.connect(lambda: self.ButtonClicked(2))
        
        self.three = PyQt5_QPushButton(self, 265, 150, 57, 57)
        self.three.setBackground("3.png")
        self.three.setPressedBackground("33.png")
        self.three.clicked.connect(lambda: self.ButtonClicked(3))

        self.four = PyQt5_QPushButton(self, 65, 250, 57, 57)
        self.four.setBackground("4.png")
        self.four.setPressedBackground("44.png")
        self.four.clicked.connect(lambda:self.ButtonClicked(4))
        
        self.six = PyQt5_QPushButton(self, 265, 250, 57, 57)
        self.six.setBackground("6.png")
        self.six.setPressedBackground("66.png")
        self.six.clicked.connect(lambda:self.ButtonClicked(6))

        self.eight = PyQt5_QPushButton(self, 165, 350, 57, 57)
        self.eight.setBackground("8.png")
        self.eight.setPressedBackground("88.png")
        self.eight.clicked.connect(lambda:self.ButtonClicked(8))

        self.nine = PyQt5_QPushButton(self, 265, 350, 57, 57)
        self.nine.setBackground("9.png")
        self.nine.setPressedBackground("99.png")
        self.nine.clicked.connect(lambda:self.ButtonClicked(9))

    def ButtonClicked(self,data):
        addCon = data
        content = ''
        content = self.yanzheng(addCon)
        if content:
            QMessageBox.information(self, "提示信息", content)
            pwd.clear()
    
    def yanzheng(self,addCon):
        pwd.append(addCon)
        self.len = len(pwd)
        if self.len >= 6:
            if(operator.eq(password,pwd)):
                return '密码正确'
            else:
                return '密码错误'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_TiePi()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()
