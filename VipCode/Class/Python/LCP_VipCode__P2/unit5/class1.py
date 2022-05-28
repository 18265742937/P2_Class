'''
将窗口隐藏，在窗口添加Label设置背景图片，添加退出游戏的按钮(8行代码)
'''
from VipCode import *

class Anim_Dialog(PyQt5_FramelessBox):
    def showDialog(self):
        self.show()
    def setupUI(self):
        self.setFixedSize(750, 550)
#======================================================class1
        # self.setWindowsTransparent(True)
        self.setWindowsTransparent(True)
        self.label = PyQt5_Qlabel(self, 0, 0, 750, 550)
        self.label.setBackground("bg_canvas.png")
        self.exit = PyQt5_QPushButton(self, 215, 0, 305, 140)
        self.exit.setBackgroundColor("transparent")
        self.exit.clicked.connect(self.proExit)

    def proExit(self):
        QApplication.quit() # self.close()
#============================================================

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog =Anim_Dialog()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()


#==============================================
"""
(1)窗口尺寸 (750, 550)
(2)标签位置以及尺寸: 0, 0, 750, 550
(3)标签背景 bg_canvas.png
(4)按钮位置以及尺寸: 215, 0, 305, 140
(5)设置按钮为透明色背景 transparent
(6)创建按钮的连接事件函数, 该函数可直接退出窗口, 点击按钮立即退出窗口

GUI
    pyqt5  
    tkinter  



"""
