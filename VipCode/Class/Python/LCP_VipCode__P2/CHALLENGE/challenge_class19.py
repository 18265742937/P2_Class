from VipCode import *
class UI_TiePi(PyQt5_QDialog):
    def showDialog(self):
        self.show()
    def setupUI(self):

        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(960, 600)
        # 设置窗口的标题
        self.setWindowTitle("Hello，Top！！")
        # 设置窗口的背景
        self.setBackground("mainBg.png")

        # 添加标签控件， 设置位置以及大小
        self.label = PyQt5_Qlabel(self, 370, 180, 350, 350)
        
        # ---------------------身体功能按钮-----------------------------------------------#
      
# --------------------------------------------------------------
     # 播放的gif
    def playGif(self, gif_name):
        # 确定要播放的gif
        self.gif = PyQt5_QMovie(gif_name)
        # 给gif设置大小
        self.gif.setScaledSize(self.label.size())
        # 确定label播放哪个gif 
        self.label.setMovie(self.gif)
        # 播放gif
        self.gif.start()
        # 获取gif的帧数
        self.frameCount = self.gif.frameCount()
        # gif帧数改变事件
        self.gif.frameChanged.connect(self.returnGif)

    # 播放音效
    def playAudio(self, auido_name):
        # 对音乐处理模块进行初始化
        self.music = PyQt5_QMediaPlayer()
        # 加载播放的声音文件
        self.music.prepare_audio(auido_name)
        # 播放
        self.music.play()
      
    def returnGif(self):
        # 让帧数自减一
        self.frameCount -= 1
        # 如果帧数为0
        if self.frameCount == 0:
            # 停止播放当前gif
            self.gif.stop()
            # 确定要播放的gif
            self.gif = PyQt5_QMovie('main_lion.gif')
            # 给gif设置大小
            self.gif.setScaledSize(self.label.size())
            # 确定label播放哪个gif 
            self.label.setMovie(self.gif)
            # 播放gif
            self.gif.start()

if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建窗口
    dialog = UI_TiePi()
    # 设置窗口的属性
    dialog.setupUI()
    # 播放特效
    dialog.playGif("main_lion.gif")
    # 播放音效
    dialog.playAudio("main_lion2.wav")
    # 显示窗口
    dialog.showDialog()
    # 保持应用运行
    app.exec_()