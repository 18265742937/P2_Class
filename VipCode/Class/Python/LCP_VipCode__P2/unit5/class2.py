'''
添加9只地鼠，并默认隐藏(10行代码)
'''

from VipCode import *

class Anim_Dialog(PyQt5_FramelessBox):
    def showDialog(self):
        self.show()
    def setupUI(self):
        self.setFixedSize(750, 550)
        self.setWindowsTransparent(True)
        self.label = PyQt5_Qlabel(self, 0, 0, 750, 550)
        self.label.setBackground("bg_canvas.png")
        # 在打地鼠文字处添加一个按钮
        self.exit = PyQt5_QPushButton(self, 215, 0, 305, 140)
        # 设置此按钮为透明
        self.exit.setBackgroundColor("transparent")
        self.exit.clicked.connect(self.proExit)

# -------------------------------------------------------------------class2
        self.listXY = [ [132,160], [319,160], [515,165], [100,250], [320,250], [520,250], [95,347], [320,352], [540,354] ]
        self.hamsters = []
        for x in range(9):
            self.addHamsters(x)
    def addHamsters(self, x):
        self.name = PyQt5_Qlabel(self,self.listXY[x][0],self.listXY[x][1],122,122)
        self.name.setBackground("hamster.png") 
        self.hamsters.append(self.name)
        # self.name.setVisible(False)
        self.name.setVisible(True)
        #Shift+Alt+ 上/下
# ----------------------------------------------------------------------------

    def proExit(self):
        # 退出应用程序
        QApplication.quit()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog =Anim_Dialog()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()