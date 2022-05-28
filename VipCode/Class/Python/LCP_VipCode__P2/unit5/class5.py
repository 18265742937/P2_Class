'''
点击地鼠，出现木槌，地鼠哭泣(添加11行代码)，留下bug(木槌不消失，下节课解决）
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
        self.listXY = [ [132,160], [319,160], [515,165], [100,250], [320,250], [520,250], [95,347], [320,352], [540,354] ]
        self.hamsters = []
        for x in range(9):
            self.addHamsters(x)
        self.timer=QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeOut)

# ------------------------------------------------------------------------------------class5
        self.hammer = PyQt5_Qlabel(self,132,160,122,122)
        self.hammer.setBackground("hammer.png")
        self.hammer.setVisible(False)

    def hitHamsters(self,x):
        self.hamsters[x][0].setBackground("hit.png")
        self.hamsters[x][0].setEnabled(False)
        self.hammer.move(self.listXY[x][0],self.listXY[x][1])
        self.hammer.setVisible(True)
# ---------------------------------------------------------------------------------------------

    def timeOut(self):
        while True:
            index = random.randint(0,8)
            #print(self.hamsters)
            if self.hamsters[index][0].isVisible() == False:          
                self.hamsters[index][0].setVisible(True)              
                break
        for i in self.hamsters:
            if i[0].isVisible():
                i[1] += 1
                if i[1] > 3:
                    i[0].setVisible(False)
                    i[1] = 0
                    i[0].setBackground("hamster.png")  # ----------------------class5
                    i[0].setEnabled(True)     # -----------------class5

    def addHamsters(self, x):
        self.name = PyQt5_Qlabel(self,self.listXY[x][0],self.listXY[x][1],122,122)
        self.name.setBackground("hamster.png") 
        self.hamsters.append([self.name,0])   
        self.name.setVisible(False)
        self.name.pressed.connect(lambda:self.hitHamsters(x))  # ---------------------class5

    def proExit(self):
        # 退出应用程序
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog =Anim_Dialog()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()