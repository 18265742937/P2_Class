from VipCode import *

class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(555, 555)
        self.setWindowTitle("茄子云音乐")
        # self.setBackground("mainBg.png")
        self.setBackgroundColor("#9AFF9A")

        #播放音乐按钮
        self.addButton(200, 388, 35, 35, "开始播放1.png", "animal_2.png")
        #按钮连接事件
        self.button.clicked.connect(self.playmusic)

        #暂停音乐按钮
        self.addButton(360, 388, 35, 35, "暂停1.png", "animal_2.png")
        #按钮连接事件
        self.button.clicked.connect(self.stopmusic)


    #播放音乐事件
    def playmusic(self):
        self.playAudio("一百万个可能.mp3")

    #暂停音乐事件
    def stopmusic(self):
        self.media.stop()

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
        self.button = PyQt5_QPushButton(
            self, x, y, width, till)  # 设置按钮的位置和大小 (self,x,y,宽,高)
        self.button.setBackground(forward_picture)  # 添加按钮的背景图片
        self.button.setPressedBackground(backward_picture)  # 设置按钮被按压后的背景


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec()
