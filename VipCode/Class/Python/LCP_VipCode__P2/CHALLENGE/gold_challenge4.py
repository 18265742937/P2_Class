from VipCode import * 

class UI(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(400,400)

        self.finalX = 0
        self.finalY = 100

    def paintEvent(self,QPaintEvent):
            qp = QPainter(self)
            qp.setPen(QPen(QColor("red"),5))
            qp.drawLine(200, 100, 200+self.finalX, 200+self.finalY)  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()