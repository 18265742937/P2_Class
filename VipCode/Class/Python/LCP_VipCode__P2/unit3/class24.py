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

        #添加身体按钮
        # self.addBodyButton(self.lable)
        #设置窗口托盘
        self.tray = PyQt5_QSystemTrayIcon(self)
        #设置托盘图标样式
        self.tray._setIcon("icon.png")
        #添加显示的菜单
        self.menuShow = self.tray.addMenu("显示")
        #连接显示菜单的事件
        self.menuShow.triggered.connect(self.trayShow)
        #添加退出的菜单
        self.menuExit = self.tray.addMenu("退出")
        #连接退出菜单的事件
        self.menuExit.triggered.connect(self.trayExit)
        #显示图标
        self.tray.show()

        #添加透明窗口组件
        self.framelessBox = PyQt5_FramelessBox()
        #设置组件置顶
        self.framelessBox.setWindowsTop(True)
        #设置组件透明(只显示界面上的组件, 虚化窗口)
        self.framelessBox.setWindowsTransparent(True)
        #添加一个label组件到framelessBox上
        self.frameLabel = PyQt5_Qlabel(self.framelessBox, 0, 0, 340, 340)
        # #测试透明属性, 添加背景
        # self.frameLabel.setBackground("icon.png")
        #播放GIF
        self.playGif2("frame_fly.gif")

        #为framelessBox创建一个动画
        self.anim = PyQt5_Animation(self.framelessBox)
        #设置动画时长
        self.anim.setDuration(4000)
        #获取窗口的宽度
        self.width = getDesktopWidth()
        #获取窗口的高度
        self.height = getDesktopHeight()
        #设置动画的终点
        self.anim.setEndValues(self.width-640, self.height-340, 240, 240)
        #设置动画模式
        self.anim.setMode(Mode.InOut)
        #添加动画可移动监听
        self.anim.valueChanged.connect(self.animChange)

        #添加Animation结束的事件
        self.anim.animFinished.connect(self.animFinish)

#开始---------------------------------------------------------------------------------
        #创建一个关闭动画
        self.closeAnim = PyQt5_Animation(self.framelessBox)
        #设置动画时长
        self.closeAnim.setDuration(4000)
        #设置动画终点
        self.closeAnim.setEndValues(self.width/2-17, self.height/2-170, 340, 340)
        #设置动画模式
        self.closeAnim.setMode(Mode.InOut)
        #连接animChange方法
        self.closeAnim.valueChanged.connect(self.animChange)

        #动画结束监听
        self.closeAnim.animFinished.connect(self.closeAnimFinish)
#结束-----------------------------------------------------------




    #改变窗口退出的事件
    def closeEvent(self, event):
        #隐藏当前界面
        self.hide()
        #显示framelessBox界面
        self.framelessBox.show()
        #透明窗口显示时开始运行动画
        self.anim.start()
        #设置默认的退出窗口失效
        event.ignore()

#开始修改代码---------------------------------------------------------------------------
    def trayShow(self):
        #关闭透明窗口
        #self.framelessBox.close()
        #显示窗口
        #self.show()
        #切换GIF为fly
        self.playframeGif("frame_fly.gif")
        #设置结束为False
        #关闭动画开始播放
        self.closeAnim.start()
#结束修改代码-------------------------------------------------------------


    #图标的退出事件
    def trayExit(self):
        #程序的退出
        QApplication.quit()

    #anim播放的时候不断地适应组件的大小

    def animChange(self):
        #更改frameLabel的大小为窗口的大小
        self.frameLabel.setSize(self.framelessBox.size())
        #给GIF设置大小
        self.frameGif.setScaledSize(self.frameLabel.size())

    #创建animFinished方法, 并且切换GIF

    def animFinish(self):
        #动画结束后切换GIF
        self.playframeGif("frame_down.gif")

        #获取GIF的帧数
        self.flyCount = self.frameGif.frameCount()
        #绑定帧改变事件
        self.frameGif.frameChanged.connect(self.changeGif)

    def changeGif(self):
        #帧减少1
        self.flyCount -= 1
        #如果播放完一次(mac系统由于透窗口的的刷新机制, 需要提前一帧进行切换)
        if self.flyCount == 1:
            #停止之前的GIF
            self.frameGif.stop()
            #播放休眠的GIF
            self.playframeGif("frame_sleep.gif")
#开始-----------------------------------------------------
    #创建显示主界面的方法
    def closeAnimFinish(self):
        #关闭framelessBox界面
        self.framelessBox.close()
        #显示主界面
        self.show()
#结束-----------------------------------------------------




     #播放GIF的函数
    def playGif2(self, gif_name):
        #确定要播放的Gif
        self.frameGif = PyQt5_QMovie(gif_name)
        #给GIF设置大小尺寸 (与label的尺寸大小保持一致!)
        self.frameGif.setScaledSize(self.frameLabel.size())
        #确定label播放哪一个GIF
        self.frameLabel.setMovie(self.frameGif)
        #播放GIF
        self.frameGif.start()


    #播放GIF的函数
    def playframeGif(self, gif_name):
        #确定要播放的Gif
        self.frameGif = PyQt5_QMovie(gif_name)
        #给GIF设置大小尺寸 (与label的尺寸大小保持一致!)
        self.frameGif.setScaledSize(self.frameLabel.size())
        #确定label播放哪一个GIF
        self.frameLabel.setMovie(self.frameGif)
        #播放GIF
        self.frameGif.start()

        #mac本透明窗口需要手动添加刷新
        self.frameGif.frameChanged.connect(self.frameLabel.refresh)


if __name__ == "__main__":  # 该程序的入口
    app = QApplication(sys.argv)  # 应用程序  =货架子
    dialog = Dialog_First()  # 创建窗口类对象
    dialog.show_Dialog()  # 通过对象去调用显示这个窗口的函数
    dialog.ui_Dialog()  # 通过对象去调用
    app.exec_()  # 让程序持续保持运行
    

