from VipCode import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QLineEdit


class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(555, 555)
        self.setWindowTitle("茄子最棒 !")
        self.setBackground("mainBg.png")

        #创建文本框
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 40)  # 移动
        self.textbox.resize(280, 40)

        #创建按钮
        self.button = QPushButton('show text', self)
        self.button.move(20, 80)

        #事件
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, "Message", '内容: ' + textboxValue,
                             QMessageBox.Ok, QMessageBox.Ok)
        """打印完毕之后清空文本框"""
        self.textbox.setText('')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec()
