from VipCode import *

class Dialog_Second(PyQt5_QDialog):   #创建一个类
    #定义显示窗口的函数   self代表当前的函数
    def show_Dialog(self):   
        self.show()   #显示这个窗口

#开始---------------------------------------------------------------------
     #定义美化窗口的函数
    def ui_Dialog(self):   
        self.setFixedSize(640,360)  #设置窗口的尺寸,不可拖动更改尺寸 (长,高)

        #添加标签控件, 这是位置以及大小
        self.addLabel(0,0,640,360)
        #播放动画
        self.playGif("wzry.gif")
#结束----------------------------------------------------------------------

    def playGif(self,gif_name):
        #确定要播放的Gif
        self.gif = PyQt5_QMovie(gif_name)
        #给GIF设置大小尺寸 (与label的尺寸大小保持一致!)
        self.gif.setScaledSize(self.lable.size()) 
        #确定label播放哪一个GIF
        self.lable.setMovie(self.gif)
        #播放GIF
        self.gif.start()

#开始---------------------------------------------------------
    #添加标签(label)
    def addLabel(self,x,y,width,till):
        self.lable = PyQt5_Qlabel(self,x,y,width,till)   #添加标签组件 (创建标签的对象) 并 改变标签组件的(位置)和(大小)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = Dialog_Second()
    first.ui_Dialog()
    first.show_Dialog()
    app.exec_()
#结束---------------------------------------------------------------


