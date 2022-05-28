from VipCode import *

class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(555,555)
        self.setWindowTitle("茄子最棒！")
        self.setBackground("mainBg.png")

        self.addLabel(180,180,350,350)
        self.playGif("main_lion.gif")
        self.playAudio("main_lion2.wav")

        self.addButton(60,388,57,57,"animal_1.png","animal_2.png")
        self.button.clicked.connect(self.hamburgerClicked2)

        self.addButton(60,430,57,57,"animal_2.png","animal_1.png")
        self.button.clicked.connect(self.juiceClicked)

        self.addBox(490,15,60,367,"action_group.png")

        self.addButton(500,330,42,42,"main_all_normal.png","main_all_pressed.png")
        self.button.clicked.connect(self.allClicked)

    def hamburgerClicked(self):
        QMessageBox.information(self,"提示信息","按钮被点击了！")


    #添加标签（label）
    def addLabel(self,x,y,width,till):
        self.lable = PyQt5_Qlabel(self,x,y,width,till)

    #播放GIF的函数
    def playGif(self,gif_name):
        #确定要播放的gif
        self.gif = PyQt5_QMovie(gif_name)
        #给GIF设置大小
        self.gif.setScaledSize(self.lable.size())
        #确定label播放哪一个GIF
        self.lable.setMovie(self.gif)
        #播放GIF
        self.gif.start()

        #获取GIF的帧数
        self.frameCount = self.gif.frameCount()
        #GIF帧数改变事件（链接事件函数）
        self.gif.frameChanged.connect(self.returnGIF)

    #播放音效函数
    def playAudio(self,audio_name):
        #添加媒体音效播放器
        self.media = PyQt5_QMediaPlayer()
        #确定要播放的音效文件
        self.media.prepare_audio(audio_name)
        #播放
        self.media.play()

#开始-----------------------------------------
    #添加按钮函数
    def addButton(self,x,y,width,till,forword_picture,back_picture):
        self.button = PyQt5_QPushButton(self,x,y,width,till)#设置按钮的位置和大小（self，x，y，宽，高）
        self.button.setBackground(forword_picture)#添加按钮的背景图片
        self.button.setPressedBackground(back_picture)
        
#开始修改代码----------------------------------
    #Top吃汉堡按钮事件
    def hamburgerClicked2(self):
        #播放吃汉堡GIF
        self.playGif("hamburger.gif")
        #播放吃汉堡音效
        self.playAudio("hamburger.wav")

    def juiceClicked(self):
        #播放喝果汁动画
        self.playGif("juice.gif")
        #播放喝果汁的音效
        self.playAudio("juice.wav")


    #通过GIF帧数改变事件（控制次数）
    def returnGIF(self):
        self.frameCount -= 1  #递减
        if self.frameCount == 0:   #加条件判断  
            #停止播放GIF
            self.gif.stop()

            #设置GIF
            self.playGif("main_lion.gif")


    def addBoxButton(self,x,y,width,till,forward_picture,backward_picture):
        self.hamburger = PyQt5_QPushButton(self.allGroup,x,y,width,till)
        self.hamburger.setBackground(forward_picture)
        self.hamburger.setPressedBackground(backward_picture)


    def addBox(self,x,y,width,till,picture_name):
        self.allGroup = PyQt5_QGroupBox(self,x,y,width,till)
        self.allGroup.setBackground(picture_name)

        self.addBoxButton(9,5,42,42,"main_halo_normal.png","main_halo_pressed.png")
        self.hamburger.clicked.connect(self.haloClicked)

        self.addBoxButton(9,56,42,42,"main_anger_normal.png","main_anger_pressed.png")
        self.hamburger.clicked.connect(self.angerClicked)

        self.addBoxButton(9,107,42,42,"main_cry_normal.png","main_cry_pressed.png")
        self.hamburger.clicked.connect(self.cryClicked)

        self.addBoxButton(9,158,42,42,"main_glasses_normal.png","main_glasses_pressed.png")
        self.hamburger.clicked.connect(self.glassesClicked)

        self.addBoxButton(9,209,42,42,"main_boxing_normal.png","main_boxing_pressed.png")
        self.hamburger.clicked.connect(self.boxingClicked)

        self.addBoxButton(9,260,42,42,"main_disappear_normal.png","main_disappear_pressed.png")
        self.hamburger.clicked.connect(self.disappearClicked)

        


    def haloClicked(self):
        self.playGif("halo.gif")
        self.playAudio("halo.wav")

    def angerClicked(self):
        self.playGif("anger.gif")
        self.playAudio("anger.wav")


    def cryClicked(self):
        self.playGif("cry.gif")
        self.playAudio("cry.wav")

    def glassesClicked(self):
        self.playGif("glasses.gif")
        self.playAudio("glasses.wav")


    def boxingClicked(self):
        self.playGif("boxing.gif")
        self.playAudio("boxing.wav")


    def disappearClicked(self):
        self.playGif("disappear.gif")
        self.playAudio("disappear.wav")


    def allClicked(self):
        if self.allGroup.isVisible():
            self.allGroup.setVisible(False)
        else:
            self.allGroup.setVisible(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec()     

    




