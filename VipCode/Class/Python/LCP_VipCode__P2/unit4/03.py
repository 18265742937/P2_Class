'''
1、该节内容是根据上节课讲的摇摆之间X、Y和角度之间的关系，讲上节课的代码进行更改，和添加，让静态的线摆动起来
2、添加、变动的代码为8行
3、挑战可以让学生线段在窗口的平移（向上、向下的平移）
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
        for i in range(0,len(self.listXY),3):  
            self.addMineral(self.listXY[i][0],self.listXY[i][1],30,"gold.png",30)
            self.addMineral(self.listXY[i+1][0],self.listXY[i+1][1],20,"diamond.png",60)
            self.addMineral(self.listXY[i+2][0],self.listXY[i+2][1],50,"stone.png",5)

        
        self.elder = PyQt5_Qlabel(self,278,12,70,70)
        self.elder.setBackground("init.png")

        self.hook = PyQt5_Qlabel(self,290,88,20,15)
        self.hook.setBackground("hook.png")

        #=====================================第三课添加代码============================================
        self.finalX = 0     # 绳子初始化时最末端x坐标点
        self.finalY = 30  # 绳子初始时最末端的Y坐标点
        #==============================================================================================


    def paintEvent(self,QPaintEvent):
        qp = QPainter(self)
        qp.setPen(QPen(QColor(38,38,38),2))
        qp.drawLine(300, 60, 300+self.finalX, 60+self.finalY)  #==============================此处做更改
        self.hook.move(290+self.finalX, 58+self.finalY) #==============================第三课添加代码
        rock(dialog,30)     #==============================第三课添加代码
        refresh(dialog,2)    #==============================第三课添加代码
    
    def addMineral(self,x,y,size,img,reward):
        self.name = PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()



