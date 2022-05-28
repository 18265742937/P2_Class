import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(
            QPixmap('F:\Python\PyQt5\Widgets\images\mute.png'))
        self.label.setGeometry(160, 30, 80, 50)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('滑块控件')
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(
                QPixmap('F:\Python\PyQt5\Widgets\images\mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(
                QPixmap('F:\Python\PyQt5\Widgets\images\min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(
                QPixmap('F:\Python\PyQt5\Widgets\images\med.png'))
        else:
            self.label.setPixmap(
                QPixmap('F:\Python\PyQt5\Widgets\images\max.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
