# @Author: 茄子
# @Date: 2019-09-29 11:16:38
# @Last Modified by:  茄子
# @Last Modified time: 2019-09-29 11:16:38
# @Description:  "第四课  Top的食物箱"

from VipCode import *

class Dialog_First(PyQt5_QDialog):
    # def __init__(self,listmusic):
    #     self.listmusic = listmusic
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(555, 555)
        self.setWindowTitle("茄子云音乐")
        # self.setBackground("mainBg.png")
        self.setBackgroundColor("#9AFF9A")

        #播放音乐按钮
        self.addButton(60, 388, 35, 35, "开始播放1.png", "animal_2.png")
        #按钮连接事件
        self.button.clicked.connect(self.playmusic)

        #暂停音乐按钮
        self.addButton(160, 388, 35, 35, "暂停1.png", "animal_2.png")
        #按钮连接事件
        self.button.clicked.connect(self.stopmusic)

  
    def playmusic(self):
        self.playAudio("一百万个可能.mp3")

    def stopmusic(self):
        self.media.stop()

    def ssmusic():


    #添加标签(label)
    def addLabel(self, x, y, width, till):
        self.label = PyQt5_Qlabel(self, x, y, width, till)  # 设置标签组件的(位置)和(大小)

    #播放GIF的函数
    def playGif(self, gif_name):
        #确定要播放的Gif
        self.gif = PyQt5_QMovie(gif_name)
        #给GIF设置大小
        self.gif.setScaledSize(self.label.size())
        #确定label播放哪一个GIF
        self.label.setMovie(self.gif)
        #播放gif
        self.gif.start()

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
