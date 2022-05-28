from VipCode import *
from class12_two_wzry import *  

class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()
    def ui_Dialog(self):
#开始---------------------------------------------------------
        #设置窗口的尺寸,不可拖动更改尺寸 (长,高)
        self.setFixedSize(640,360)  
        #设置窗口的背景图片
        self.setBackground("wzry.png")   
        #播放音效
        self.playAudio("wzry.wav") 
        #添加开始游戏按钮, 冰规定其位置, 大小,背景
        self.addButton(220,270,200,55,"ksyx.png","ksyx.png")
        #连接按钮的点击事件
        self.hamburger.clicked.connect(self.Click)

#结束--------------------------------------------------------------------------
    #播放音效函数
    def playAudio(self,audio_name):
        #添加媒体音效播放器
        self.media = PyQt5_QMediaPlayer()
        #确定要播放的音效文件
        self.media.prepare_audio(audio_name)
        #播放
        # self.media.play()
#开始---------------------------------------------------------------
    #添加按钮函数
    def addButton(self,x,y,width,till,forward_picture,backward_picture):
        self.hamburger = PyQt5_QPushButton(self,x,y,width,till)    #添加按钮组件, 并调整按钮的位置和大小 (self,,,宽,高)
        self.hamburger.setBackground(forward_picture)   #添加按钮的背景图片
        self.hamburger.setPressedBackground(backward_picture)  #设置按钮被按压后的背景
        
     #显示开始游戏的第二个窗口界面的事件
    def Click(self):
        #创建第二个窗口界面的对象
        dialog = Dialog_Second()
        #调用设置窗口内容的函数
        dialog.ui_Dialog()
        #调用显示窗口的函数
        dialog.show_Dialog()
        #保持窗口持续运行
        dialog.exec_()  # ---------------------这一行一定要注意
#结束---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = Dialog_First()
    first.ui_Dialog()
    first.show_Dialog()
    app.exec_()





















