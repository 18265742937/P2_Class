from VipCode import * 

class UI(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(200,200)
        self.setWindowTitle("播放音效")

       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()