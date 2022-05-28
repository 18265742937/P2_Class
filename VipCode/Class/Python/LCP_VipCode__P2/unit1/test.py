from VipCode import *

class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()
        print(1)
    def ui_Dialog(self):
        self.setFixedSize(500,500)
        self.setWindowTitle("001")
        self.setBackground("mainBg.png")
        print(2)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec_()