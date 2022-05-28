from VipCode import *  # *代表全部的意思


class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(650, 500)
        self.setWindowTitle("小窗口 !")
        self.setBackgroundColor("#7FFFD4")
        self.playAudio("一百万个可能.mp3")

    #播放音效函数
    def playAudio(self, audio_name):
        #添加媒体音效播放器
        self.media = PyQt5_QMediaPlayer()
        #确定要播放的音效文件
        self.media.prepare_audio(audio_name)
        #播放
        self.media.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec_()
