# @Author: 茄子
# @Date: 2019-08-01 22:14:50
# @Last Modified by: 茄子
# @Last Modified time: 2019-08-01 22:14:50
# @Description:  "第八课 吃饱的日常(一)"


from VipCode import *  # 导入工具

class Dialog_First(PyQt5_QDialog):  # 创建一个类
    #定义显示窗口的函数   self代表当前的函数
    def show_Dialog(self):
        self.show()  # 显示这个窗口

    #定义美化窗口的函数
    def ui_Dialog(self):
        self.setFixedSize(555, 555)  # 设置窗口的尺寸,不可拖动更改尺寸 (长,高)
        self.setWindowTitle("我的第一个小窗口 !")  # 设置窗口的标题
        self.setBackground("mainBg.png")  # 设置窗口的背景图片

        #让小狮子出现(创建标签)
        self.addLabel(180, 180, 350, 350, "main_lion.gif")
        #让小狮子动起来(放入GIF)
        self.playGif("main_lion.gif")
        #添加音乐
        self.playAudio("main_lion2.wav")
        #添加吃汉堡的按钮
        self.addButton(60, 388, 57, 57, "animal_2.png", "animal_1.png")
        #连接吃汉堡按钮的点击事件
        self.hamburger.clicked.connect(self.hamburgerClicked)
        #添加喝果汁的按钮
        self.addButton(60,430,57,57,"animal_2.png","animal_1.png")
        #连接喝果汁按钮的点击事件
        self.hamburger.clicked.connect(self.juiceClicked)
#开始---------------------------------------------------------
        #添加组控件
        self.addBox(490,15,60,367,"action_group.png")
#结束---------------------------------------------------------


    #Top吃汉堡按钮事件
    def hamburgerClicked(self):
        #播放吃汉堡GIF
        self.playGif("hamburger.gif")
        #播放吃汉堡音效
        self.playAudio("hamburger.wav")
    
    #Top喝果汁的事件
    def juiceClicked(self):
        #播放喝果汁动画
        self.playGif("juice.gif")
        #播放喝果汁的音效
        self.playAudio("juice.wav")
        
#开始------------------------------------------------
    #Top眩晕事件            
    def haloClicked(self):
        #播放GIF动画
        self.playGif("halo.gif")
        #播放音效
        self.playAudio("halo.wav")
 
    #Top生气事件
    def angerClicked(self):
        #播放GIF动画
        self.playGif("anger.gif")
        #播放音效
        self.playAudio("anger.wav") 
#结束----------------------------------------------- 


    #添加标签(label)
    def addLabel(self, x, y, width, till, back_picture):
        self.lable = PyQt5_Qlabel(self, x, y, width, till)  # 设置标签组件的(位置)和(大小)
        self.lable.setBackground(back_picture)  # 给标签添加背景 (静态的)

    #播放GIF的函数并可以控制GIF帧数
    def playGif(self, gif_name):
        #确定要播放的Gif
        self.gif = PyQt5_QMovie(gif_name)
        #给GIF设置大小
        self.gif.setScaledSize(self.lable.size())
        #确定label播放哪一个GIF
        self.lable.setMovie(self.gif)
        #播放gif
        self.gif.start()
        #获取GIF的帧数
        self.frameCount = self.gif.frameCount()
        #GIF帧数改变事件(连接事件函数)
        self.gif.frameChanged.connect(self.returnGif)

    #播放音效函数
    def playAudio(self, audio_name):
        #添加媒体音效播放器
        self.media = PyQt5_QMediaPlayer()
        #确定要播放的音效文件
        self.media.prepare_audio(audio_name)
        #播放
        self.media.play()
        

    #添加按钮函数
    def addButton(self, x, y, width, till, forward_picture, backward_picture):
        self.hamburger = PyQt5_QPushButton(self, x, y, width, till)  # 设置按钮的位置和大小 (self,x,y,宽,高)
        self.hamburger.setBackground(forward_picture)  # 添加按钮的背景图片
        self.hamburger.setPressedBackground(backward_picture)  # 设置按钮被按压后的背景
    
    #通过GIF帧数改变事件(控制次数)
    def returnGif(self):
        self.frameCount -= 1   #递减
        if self.frameCount == 0:   #加条件判断
            #停止GIF播放
            self.gif.stop()   

            #设置GIF
            self.playGif("main_lion.gif")
#开始------------------------------------------------------
    #添加组控件按钮(box_button)
    def addBoxButton(self,x,y,width,till,forward_picture,backward_picture):
        self.hamburger = PyQt5_QPushButton(self.allGroup,x,y,width,till)    #添加按钮组件, 并调整按钮的位置和大小 (self,,,宽,高)
        self.hamburger.setBackground(forward_picture)   #添加按钮的背景图片
        self.hamburger.setPressedBackground(backward_picture)   #设置按钮被按压后的背景    

    #添加组控件(box)
    def addBox(self,x,y,width,till,picture_name):
        self.allGroup = PyQt5_QGroupBox(self,x,y,width,till)
        self.allGroup.setBackground(picture_name)
        #设置组控件中的按钮
        #第一个按钮以及连接事件
        self.addBoxButton(9,5,42,42,"main_halo_normal.png","main_halo_pressed.png")
        self.hamburger.clicked.connect(self.haloClicked)
        #第二个按钮以及连接事件
        self.addBoxButton(9,56,42,42,"main_anger_normal.png","main_anger_pressed.png")
        self.hamburger.clicked.connect(self.angerClicked)
        
 #结束--------------------------------------------------------



if __name__ == "__main__":  # 该程序的入口
    app = QApplication(sys.argv)  # 应用程序  =货架子
    dialog = Dialog_First()  # 创建窗口类对象
    dialog.ui_Dialog()  # 通过对象去调用
    dialog.show_Dialog()  # 通过对象去调用显示这个窗口的函数
    app.exec_()  # 让程序持续保持运行
