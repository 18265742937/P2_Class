from VipCode import *  # *代表全部的意思


class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(650, 500)
        self.setWindowTitle("小窗口 !")
        self.setBackgroundColor("#7FFFD4")
        self.addLabel(0, 0, 200, 200)
        self.playGif("main_lion.gif")

    #添加标签(label)
    def addLabel(self, x, y, width, till):
        # 设置标签组件的(位置)和(尺寸)
        self.lable = PyQt5_Qlabel(self, x, y, width, till)

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

    #通过GIF帧数改变事件(控制次数)
    def returnGif(self):
        self.frameCount -= 1  # 递减
        if self.frameCount == 0:  # 加条件判断
            #停止GIF播放
            self.gif.stop()
            #设置GIF
            self.playGif("main_lion.gif")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec_()
