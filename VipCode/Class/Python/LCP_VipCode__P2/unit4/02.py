'''
1、添加老头、静态的线和钩子（8行代码）
2、该节内容主要讲静态的划线，然后在PPT讲解线摇摆时的原理，及此时X,Y,和角度之间的关系。方便下节课上来就更改代码为摇摆的效果
3、挑战可以让学生做关于划线的内容，例如用画线的知识点做一个十字，或者土字形状
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

        #=====================================第二课添加代码============================================
        #添加矿工的图片
        self.elder = PyQt5_Qlabel(self,278,12,70,70)
        self.elder.setBackground("init.png")
        #添加钩子的图片
        self.hook = PyQt5_Qlabel(self,290,88,20,15)
        self.hook.setBackground("hook.png")

    #设置并调整绳子的函数
    def paintEvent(self,QPaintEvent):
        qp = QPainter(self)  #拿到画笔
        qp.setPen(QPen(QColor(38,38,38),2))    #设置画笔
        qp.drawLine(300, 60, 300, 60+30)    #绘制绳子

        #==============================================================================================
    
    def addMineral(self,x,y,size,img,reward):
        self.name = PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(img)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()