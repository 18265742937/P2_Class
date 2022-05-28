from VipCode import *

class UI_Safe(PyQt5_QDialog):
    def setupUI(self):
         # 创建一个特殊的组件类似于窗口，不同的是没有边框，并且可以只显示控件（透明）
        self.framelessBox = PyQt5_FramelessBox()
        # 设置组件置顶
        self.framelessBox.setWindowsTop(True)
        # 设置组件透明（只显示界面上的组件，虚化窗口）
        self.framelessBox.setWindowsTransparent(True)

        self.framelessX = getDesktopWidth()
        self.framelessY = getDesktopHeight()
        # 设置窗口大小
        self.framelessBox.setResize(200, 1000)
        self.framelessBox.move(self.framelessX-300, self.framelessY-1150)
        # 添加一个label组件到framelessBox上
        self.label = PyQt5_Qlabel(self.framelessBox, 100, 900, 100, 100)
        self.label1 = PyQt5_Qlabel(self.framelessBox, 50, 700, 200, 200)
        self.label1.setBackground("rocket.png")
        self.label1.setVisible(False)
        # 创建窗口托盘
        self.acion = PyQt5_QSystemTrayIcon(self)
        # 设置托盘图标样式
        self.acion._setIcon("icon.png")
        # 添加菜单选项
        self.menu = self.acion.addMenu("退出")
        # 连接菜单的事件
        self.menu.triggered.connect(self.menuClicked)
        # 显示图标
        self.acion.show()

        self.playGif("speedBall.gif")
        self.gif.stop()

    # --------------------------------------------------------class27需要书写代码----------------------------------------------------------
        #添加鼠标按下的事件
        self.label.pressed.connect(self.mousePress)
        # 添加鼠标移动的事件
        self.label.moved.connect(self.mouseMove)
        # 添加鼠标的双击事件
        self.label.doubleclicked.connect(self.mouseDoubleClicked)
        self.anim = PyQt5_Animation(self.label1)
        # 设置动画时长
        self.anim.setDuration(2000)
        # 获取窗口的宽度
        self.width = getDesktopWidth()
        #  获取窗口的高度
        self.height = getDesktopHeight()
        # 更改动画的起点固定在加速球上方
        self.anim.setStartValues(50, 700, 200, 200)
        # #设置动画终点和模式
        self.anim.setEndValues(50, 0, 200, 200)
        self.anim.setMode(Mode.OutIn)
        # anim结束后设置小火箭隐藏
        self.anim.animFinished.connect(lambda: self.label1.setVisible(False))
        
    # 加速球的双击事件
    def mouseDoubleClicked(self):
        # 播放gif
        self.playGif("speedBall.gif")
        # 设置小火箭可见
        self.label1.setVisible(True)
        # 开始播放anim
        self.anim.start()
   # self.label1.move(50,700)

    #加速球的单击事件
    def mousePress(self, event):
        # 按下的时候获取控件在窗口中的坐标
        self.posX = event.x()
        self.posY = event.y()

    #加速球位置的移动事件
    def mouseMove(self, event):
        self.label1.setVisible(False)
        self.anim.stop()
        # 获取鼠标在整个界面的坐标
        self.globalX = event.globalX()
        self.globalY = event.globalY()
        # 调用窗口的移动
        self.framelessBox.move(self.globalX-self.posX-100, self.globalY-self.posY-900)

    # ---------------------------------------------------------------------------------------------------------------------------------------------

     # anim进行时不断的适应组件大小

    def animChange(self):
        # 更改frameLabel的大小为窗口的大小
        self.label.resize(self.framelessBox.size())
        # 给gif设置大小
        self.gif.setScaledSize(self.label.size())

    def menuClicked(self):
        QApplication.quit()
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
        self.gif.frameChanged.connect(self.label.refresh)
        # 获取gif的帧数
        self.frameCount = self.gif.frameCount()
        # gif帧数改变事件
        self.gif.frameChanged.connect(self.returnGif)

    def returnGif(self):
        # 让帧数自减一
        self.frameCount -= 1
        # 如果帧数为0
        if self.frameCount == 0:
            # 停止播放当前gif
            self.gif.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Safe()
    dialog.setupUI()
    # dialog.show()
    dialog.framelessBox.show()
    app.exec_()
