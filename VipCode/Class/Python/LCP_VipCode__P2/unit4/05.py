'''
1、本节课主要内容为将绳子碰到的东西吊起来，吊成功的话播放成功音乐，并将吊成功的控件从列表中删除，
   将坐标也同时删除。坐标为上节课讲的内容
2、代码数量为：12行代码
3、此时有一个小bug（钓完金子后，绳子上的钩子消失了，下节课开头讲）
4、本节课内容较多，逻辑偏复杂。所以挑战可以设计简单的或者不设计。
  （建议设计的内容为：让学生自己尝试些播放音乐的方法，而不是调用已经有的方法，该内容为前18课已经讲解的内容）
'''
from VipCode import * 

class UI_Gold(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):

        self.setFixedSize(600,400)
        self.setWindowTitle("黄金矿工")
        self.setBackground("bg1.png")

        self.namelist = [] 
        self.listXY = [ [10,300],[453,350],[76,260],[129,320],[520,160],[190,190],[209,322],[259,180],[356,159],[456,222],[513,346],[333,268],[153,159],[268,357],[550,263] ]
        random.shuffle(self.listXY)

        for i in range(0,len(self.listXY),3):  
            self.addMineral(self.listXY[i][0],self.listXY[i][1],30,"gold.png",30)
            self.addMineral(self.listXY[i+1][0],self.listXY[i+1][1],20,"diamond.png",60)
            self.addMineral(self.listXY[i+2][0],self.listXY[i+2][1],50,"stone.png",5)

        
        self.elder = PyQt5_Qlabel(self,278,12,70,70)
        self.elder.setBackground("init.png")

        self.hook = PyQt5_Qlabel(self,290,108,20,15)
        self.hook.setBackground("hook.png")

        self.finalX = 0     # 绳子初始化时最末端x坐标点
        self.finalY = 30  # 绳子初始时最末端的Y坐标点

        self.downButton = PyQt5_QPushButton(self, 10, 10, 60, 60)
        self.downButton.clicked.connect(self.downButtonClicked)

        self.isdo = 0   # ff控制绳子勾东西的时机，用于点击按钮开始勾东西

        self.distanceX = 0 #绳子每次延长或缩短的X轴上的距离
        self.distanceY = 0  #绳子每次延长或缩短的Y轴上的距离

    def downButtonClicked(self):
        self.isdo = 1


    def paintEvent(self,QPaintEvent):
        qp = QPainter(self)
        qp.setPen(QPen(QColor(38,38,38),2))
        if self.isdo == 1:
#=====================================第五课添加代码============================================
            qp.drawLine(300, 60, 300+self.finalX+self.distanceX, 60+self.finalY+self.distanceY)
            judge(dialog,300+self.finalX+self.distanceX,60+self.finalY+self.distanceY,60,30,5,20,30,50)
            flag1,flag2 = YesOrNo(dialog)
            if flag1 == 1 and flag2== 0:
                # print("捞取东西，还没上岸")
                self.hook.setVisible(False)
                change_img(dialog,30,60,5)
                self.namelist[self.index][0].move(300 - (getBorder() / 2 + 3) + self.finalX + self.distanceX, \
                    60+self.finalY+self.distanceY)  #跟随绳子移动控件
            if flag1 == 1 and flag2 == 1:
                # print("捞取东西，已经上岸")
                playAudio("success.mp3")
                self.namelist[self.index][0].setVisible(False)
                del self.listXY[self.index]
                del self.namelist[self.index]
#============================================================================================
        else:                                                           
            qp.drawLine(300, 60, 300+self.finalX, 60+self.finalY)      
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



