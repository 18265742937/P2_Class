'''
1、本节课主要为：添加一个点击按钮，点击按钮控制台输出内容（以后拓展画线）（同时讲清楚响应事件应该是什么，为什么要追加金子、钻石和石头到列表中）
2、添加、变动的代码为12行
3、务必讲清楚绳子向下时的坐标关系，为下节课碰撞做铺垫（做课件时参考下节课的坐标关系提前渗透）
4、本节课讲解内容较多，逻辑较为复杂，可不添加挑战事件
'''
from VipCode import * 

class UI_Gold(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(600,400)
        self.setWindowTitle("黄金矿工")
        self.setBackground("bg1.png")

        self.namelist = []  #==========================================第四课缩进代码
        
        self.listXY = [[10, 300], [453, 350], [76, 260], [513, 346], [333, 268], [153, 159]]
        
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

    #=====================================第四课添加代码============================================
        #创建按钮
        self.downButton = PyQt5_QPushButton(self, 10, 10, 40, 40)
        #连接事件
        self.downButton.clicked.connect(self.downButtonClicked)

        self.distanceX = 0 #绳子每次延长或缩短的X轴上的距离
        self.distanceY = 0  #绳子每次延长或缩短的Y轴上的距离

        # 定义标记位
        self.isdo = 0   
        
    def downButtonClicked(self):
        # 更改标记位
        self.isdo = 1
    #=============================================================================================

    def paintEvent(self,QPaintEvent):
        qp = QPainter(self)
        qp.setPen(QPen(QColor(38, 38, 38), 2))
        
        if self.isdo == 1:            #===============================第四课添加代码
            print("延长线段，检测碰撞")  #===============================第四课添加代码
            self.isdo = 0            #===============================第四课添加代码
        else:                 #===============================第四课修改代码
            qp.drawLine(300, 60, 300+self.finalX, 60+self.finalY) #===============================第四课缩进代码
            self.hook.move(290+self.finalX, 58+self.finalY)  #===============================第四课缩进代码
            rock(dialog,30)    #===============================第四课缩进代码
        refresh(dialog,2)                                      
    
    def addMineral(self,x,y,size,img,reward):
        self.name = PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(img)
        self.namelist.append([self.name,reward])   #=======================================第四课添加代码

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()

#标记位:  以变量的形式描述数据的多种状态  0/1   True/False