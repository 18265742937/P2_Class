from VipCode import *
import random
class Anim_Dialog(PyQt5_QDialog):
    def showDialog(self):
        self.show()
    def setupUI(self):
        
        self.i = 0
        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(600, 600)
        # 设置窗口的背景
        self.setBackgroundColor("rgb(3,3,3)")
        self.label = PyQt5_Qlabel(self,0,0,600,600)
        self.label2 = PyQt5_Qlabel(self.label,0,0,0,0)
        self.label.moved.connect(self.drawCircle)
        self.label1 = {}
        self.anim = {}

#开始--------------------------------------------------------------------------------------
    def drawCircle(self,event):
    
        self.posX = event.x()
        self.posY = event.y()
        #获取一个随机整数
        self.qNumber = random.randint(1, 8)
        imageName = "circle" + str(self.qNumber)
        self.label1[self.i] = PyQt5_Qlabel(self.label, self.posX, self.posY, 0, 0)
        self.label1[self.i].setBackground(imageName)

        # 动态添加label需要添加show()方法
        self.label1[self.i].show()
        # 创建动画
        self.anim[self.i] = PyQt5_Animation(self.label1[self.i])
        self.anim[self.i].setDuration(400)
        self.anim[self.i].setEndValues(self.posX-20,self.posY-20,40,40)
        self.anim[self.i].start()
        # 动画结束时清除label[i]
        self.anim[self.i].animFinished.connect(self.label1[self.i].deleteLater)
        # 变量+1
        self.i+=1
#结束------------------------------------------------------------------------------------
      

if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建窗口
    dialog =Anim_Dialog()
    # 设置窗口的属性
    dialog.setupUI()
    # 显示窗口
    dialog.showDialog()
    # 保持应用运行
    app.exec_()