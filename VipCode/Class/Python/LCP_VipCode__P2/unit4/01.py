'''
1、本节课主要随机在窗口生成两个金块、两个钻石、两个石头（一共十行代码） 
2、课件制作要引导式教学，用最笨的方式，然后慢慢开始封装函数，添加多个参数
3、挑战可以设置为添加多个金块，砖石，和石头（数量可以是不相同的）
'''


from VipCode import *

class UI_Gold(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(600,400)
        self.setWindowTitle("黄金矿工")
        self.setBackground("bg1.png")

#=====================================第一节课添加代码==========================================
        self.listXY = [ [10,300],[453,350],[76,260],[513,346],[333,268],[153,159] ]
        random.shuffle(self.listXY)

        for i in range(0,len(self.listXY),3):  
            self.addMineral(self.listXY[i][0],  self.listXY[i][1],30,"gold.png", 30)
            self.addMineral(self.listXY[i+1][0],self.listXY[i+1][1],20,"diamond.png", 60)
            self.addMineral(self.listXY[i+2][0],self.listXY[i+2][1],50,"stone.png", 5)
        
    def addMineral( self, x, y, size, img, reward ):
        self.name = PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(img)
#==============================================================================================

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()
