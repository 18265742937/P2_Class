from VipCode import *
from challenge_class11_two import *

class Jump(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(400, 300)
        self.setWindowTitle("跳转界面")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Jump()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()