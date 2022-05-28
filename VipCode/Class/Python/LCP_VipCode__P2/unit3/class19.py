from VipCode import *  # 导入工具

class Dialog_First(PyQt5_QDialog):  # 创建一个类
    # 定义显示窗口的函数   self代表当前的函数
    def show_Dialog(self):
        self.show()  # 显示这个窗口

    # 定义美化窗口的函数
    def ui_Dialog(self):
        self.setFixedSize(555, 555)  # 设置窗口的尺寸,不可拖动更改尺寸 (长,高)
        self.setWindowTitle("我的第一个小窗口 !")  # 设置窗口的标题
        self.setBackground("mainBg.png")  # 设置窗口的背景图片

# 开始-------------------------------------------
        # 设置窗口托盘
        self.tray = PyQt5_QSystemTrayIcon(self)
        # 设置托盘图标样式
        self.tray._setIcon("icon.png")
        # 添加显示的菜单
        self.menuShow = self.tray.addMenu("显示")
        # 连接显示菜单的事件
        self.menuShow.triggered.connect(self.trayShow)
        # 添加退出的菜单
        self.menuExit = self.tray.addMenu("退出")
        # 连接退出菜单的事件
        self.menuExit.triggered.connect(self.trayExit)
        # 显示图标
        self.tray.show()
# 结束-------------------------------------------------


# 开始-------------------------------------------
    # 改变窗口退出的事件
    def closeEvent(self, event):
        # 隐藏当前界面
        self.hide()
        # 设置默认的退出窗口失效
        event.ignore()

    # 图标的显示事件
    def trayShow(self):
        # 显示窗口
        self.show()

    # 图标的退出事件
    def trayExit(self):
        # 程序的退出
        QApplication.quit()   #self.close()
# 结束------------------------------------------------


if __name__ == "__main__":  # 该程序的入口
    app = QApplication(sys.argv)  # 应用程序  =货架子
    dialog = Dialog_First()  # 创建窗口类对象
    dialog.ui_Dialog()  # 通过对象去调用
    dialog.show_Dialog()  # 通过对象去调用显示这个窗口的函数
    app.exec_()  # 让程序持续保持运行

