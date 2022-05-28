'''
添加兔子，让兔子和地鼠随机显示，击打兔子减分，击打地鼠加分(添加12行代码，删除1行代码)
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
        self.hammer = PyQt5_Qlabel(self,132,160,122,122)
        self.hammer.setBackground("hammer.png")
        self.hammer.setVisible(False)
        self.score = 0                  
        self.finalTime = 15    
        self.timeLabel = PyQt5_Qlabel(self,260,160,120,20)        
        self.timeLabel.setFont(QFont("楷体",16))       
        self.timeLabel.setTextColor("white")
        self.timeLabel.setText("时间：%d"%self.finalTime)               
        self.scoreLabel = PyQt5_Qlabel(self,390,160,120,20)      
        self.scoreLabel.setFont(QFont("楷体",16))
        self.scoreLabel.setTextColor("white")
        self.scoreLabel.setText("得分：%d"%self.score)  

        self.animalType = {}      #====================================添加代码
    def hitHamsters(self,x):
        #=================================================class8
        if self.animalType[self.hamsters[x][0]] == "rabbit":
            self.hamsters[x][0].setBackground("hitRabbit.png")
            self.score -= 2                 
        else:
            self.hamsters[x][0].setBackground("hit.png")
            self.score += 1    
        #=======================================================           
        self.hamsters[x][0].setEnabled(False)
        self.hammer.move(self.listXY[x][0],self.listXY[x][1])
        self.hammer.setVisible(True)
        # self.score += 1     #==================删除代码
        self.scoreLabel.setText("得分：%d"%self.score)                        

    def timeOut(self):
        while True:
            if self.hammer.isVisible():             
                self.hammer.setVisible(False)
            index = random.randint(0,8)
            #=================================================class8
            if random.randint(0,2) == 0:
                self.hamsters[index][0].setBackground("rabbit.png")
                self.animalType[ self.hamsters[index][0] ] = "rabbit"
            else:
                # self.hamsters[index][0].setBackground("hamster.png")
                self.animalType[ self.hamsters[index][0] ] = "hamster"
            #=======================================================
            if self.hamsters[index][0].isVisible() == False:          
                self.hamsters[index][0].setVisible(True)              
                break
        for i in self.hamsters:
            if i[0].isVisible():
                i[1] += 1
                if i[1] > 3:
                    i[0].setVisible(False)
                    i[0].setBackground("hamster.png")  
                    i[0].setEnabled(True)                    
                    i[1] = 0
                    

        self.finalTime -= 1
        self.timeLabel.setText("时间：%d"%self.finalTime)  
        if self.finalTime <= 0:
            self.timer.stop()
            QMessageBox.information(self,"得分","本次得分为:"+str(self.score))
            self.close()
            dialog1 =Anim_Dialog()
            dialog1.setupUI()
            dialog1.showDialog()

    def addHamsters(self, x):
        self.name = PyQt5_Qlabel(self,self.listXY[x][0],self.listXY[x][1],122,122)
        self.name.setBackground("hamster.png") 
        self.hamsters.append([self.name,0])   
        self.name.setVisible(False)
        self.name.pressed.connect(lambda:self.hitHamsters(x))   

    def proExit(self):
        # 退出应用程序
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog =Anim_Dialog()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()


