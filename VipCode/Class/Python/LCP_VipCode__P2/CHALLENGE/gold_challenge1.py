from VipCode import * 

class UI(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(600,400)
        self.setWindowTitle("黄金矿工")
        self.setBackground("bg1.png")


        
    def addMineral(self,i,x,y,size,img,reward):
        name = "mineral"+str(i)
        self.name = PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()