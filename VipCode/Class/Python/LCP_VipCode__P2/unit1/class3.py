# @Author: 茄子
# @Date: 2019-09-29 11:16:38
# @Last Modified by:  茄子
# @Last Modified time: 2019-09-29 11:16:38
# @Description:  "第三课  Top的诞生"

from VipCode import *

class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(555, 555)
        self.setWindowTitle("茄子最棒 !")
        self.setBackground("mainBg.png")
        

#开始------------------------------------------------------------------------------
        #插入标签
        self.addLabel(180, 180, 350, 350)
        #在标签放入动态图片
        self.playGif("main_lion.gif")
        #播放音乐
        self.playAudio("main_lion2.wav")
#结束-------------------------------------------------------------------------------

#开始-------------------------------------------------------------------------------
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
#结束-------------------------------------------------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec()