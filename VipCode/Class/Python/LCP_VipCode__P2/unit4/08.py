'''
1、添加计时器，计时器60秒关闭游戏窗口
2、添加代码12行
3、挑战建议为：接着上节课添加分数的挑战代码接着写。或者添加记录最高游戏记录的功能显示在游戏的顶端
'''
from VipCode import * 

class UI_Gold(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(600,400)
        self.setWindowTitle("黄金矿工")
        self.setBackground("bg1.png")
        
        self.listXY = [ [10,300],[453,350],[76,260],[513,346],[333,268],[153,159] ]
        random.shuffle(self.listXY)

        self.namelist = [] 
        for i in range(0,len(self.listXY),3):  
            self.addMineral(self.listXY[i][0],self.listXY[i][1],30,"gold.png",30)
            self.addMineral(self.listXY[i+1][0],self.listXY[i+1][1],20,"diamond.png",60)
            self.addMineral(self.listXY[i+2][0],self.listXY[i+2][1],50,"stone.png",5)

        self.elder = PyQt5_Qlabel(self,278,12,70,70)
        self.elder.setBackground("init.png")

        self.elderGif = PyQt5_QMovie("action.gif")
        self.elderGif.setScaledSize(self.elder.size())
        self.elder.setMovie(self.elderGif)

        self.hook = PyQt5_Qlabel(self,290,108,20,15)
        self.hook.setBackground("hook.png")

        self.finalX = 0     # 绳子初始化时最末端x坐标点
        self.finalY = 30  # 绳子初始时最末端的Y坐标点

        self.downButton = PyQt5_QPushButton(self, 0, 0, 600, 400)
        self.downButton.setBackgroundColor("transparent")        
        self.downButton.clicked.connect(self.downButtonClicked)

        self.isdo = 0   # 控制绳子勾东西的时机，用于点击按钮开始勾东西

        self.distanceX = 0 #绳子每次延长或缩短的X轴上的距离
        self.distanceY = 0  #绳子每次延长或缩短的Y轴上的距离

        #=====================================第八课添加代码============================================
        self.finalTime = 60
        self.finalTimeLabel = PyQt5_Qlabel(self,30,40,100,15)
        self.finalTimeLabel.setText("倒计时：%d"%self.finalTime)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout)
        #==============================================================================================
        self.beginLabel = PyQt5_Qlabel(self,0,0,600,400)
        self.beginLabel.setBackground("begin.png")
        self.beginButton = PyQt5_QPushButton(self, 120, 20, 180, 180)
        self.beginButton.setBackgroundColor("transparent")
        self.beginButton.clicked.connect(self.beginButtonClicked)

        self.isInit = 0 # 初始化控制绳子的摇摆标志位
        #=====================================第八课添加代码============================================
    def timeout(self):
        self.finalTime -= 1
        self.finalTimeLabel.setText("倒计时：%d"%self.finalTime)
        if self.finalTime <= 0:
            self.timer.stop()
            self.close()
        # ==============================================================================================

    def beginButtonClicked(self):
        self.beginLabel.setVisible(False)
        self.beginButton.setVisible(False)
        self.timer.start(1000)       #=====================================第八课添加代码==================
        self.isInit = 1
        
    def downButtonClicked(self):
        self.elder.setBackground("")    
        self.elderGif.start()           
        self.isdo = 1


    def paintEvent(self,QPaintEvent):
        qp = QPainter(self)
        qp.setPen(QPen(QColor(38,38,38),2))
        if self.isdo == 1:
            qp.drawLine(300, 60, 300+self.finalX+self.distanceX, 60+self.finalY+self.distanceY)
            judge(dialog,300+self.finalX+self.distanceX,60+self.finalY+self.distanceY,60,30,5,20,30,50)
            flag1,flag2 = YesOrNo(dialog)
            if flag1 == 1 and flag2== 0:
                self.hook.setVisible(False)
                change_img(dialog,30,60,5)
                self.namelist[self.index][0].move(300 - (getBorder()/2+3)+self.finalX+self.distanceX,60+self.finalY+self.distanceY)  #跟随绳子移动控件
            if flag1 == 1 and flag2 == 1:
                playAudio("success.mp3")
                self.elderGif.stop()    
                self.namelist[self.index][0].setVisible(False)
                del self.listXY[self.index]
                del self.namelist[self.index]
        elif self.isInit == 1:                                                          
            qp.drawLine(300, 60, 300+self.finalX, 60+self.finalY)      
            self.hook.setVisible(True)     
            self.hook.move(290+self.finalX, 58+self.finalY)             
            rock(dialog,30)                                             
        refresh(dialog,2)

    def addMineral(self,x,y,size,img,reward):
        self.name = PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(img)
        self.namelist.append([self.name,reward])                        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()