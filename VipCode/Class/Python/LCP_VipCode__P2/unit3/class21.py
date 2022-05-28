from VipCode import *

class Dialog_First(PyQt5_QDialog):
    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(700, 500)
        self.setBackground("mainBg2.png")
        self.label = PyQt5_Qlabel(self, 200, 140, 300, 300)
        self.playGif("initial.gif")

        #创建系统托盘
        self.tray = PyQt5_QSystemTrayIcon(self)
        #设置托盘图标样式
        self.tray._setIcon("icon_dragon.png")
        #显示系统托盘
        self.tray.show()
        #添加奔跑菜单选项
        self.runMenu = self.tray.addMenu("奔跑")
        #添加散步菜单选项
        self.walkMenu = self.tray.addMenu("散步")
        #添加飞行菜单选项
        self.flyMenu = self.tray.addMenu("飞行")
        #添加撕咬菜单选项
        self.biteMenu = self.tray.addMenu("撕咬")

        self.runMenu.triggered.connect(self.runMenuClicked)
        self.walkMenu.triggered.connect(self.walkMenuClicked)
        self.flyMenu.triggered.connect(self.flyMenuClicked)
        self.biteMenu.triggered.connect(self.biteMenuClicked)

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
        #获取GIF的帧数
        self.frameCount = self.gif.frameCount()
        #gif帧数改变事件
        self.gif.frameChanged.connect(self.returnGif)

    def returnGif(self):
        #让帧数自减1
        self.frameCount -= 1
        #如果帧数为0
        if self.frameCount == 0:
            #停止播放当前GIF
            self.gif.stop()
            #确定要播放的GIF
            self.gif = PyQt5_QMovie("initial.gif")
            #给gif设置大小
            self.gif.setScaledSize(self.label.size())
            #确定label播放哪一个gif
            self.label.setMovie(self.gif)
            #播放GIF
            self.gif.start()
    #奔跑的方法
    def runMenuClicked(self):
        self.playGif("run.gif")
    #散步的方法
    def walkMenuClicked(self):
        self.playGif("walk.gif")
    #飞行的方法
    def flyMenuClicked(self):
        self.playGif("fly.gif")
    #撕咬的方法
    def biteMenuClicked(self):
        self.playGif("bite.gif")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec_()

