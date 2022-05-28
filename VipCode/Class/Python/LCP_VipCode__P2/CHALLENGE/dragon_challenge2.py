from VipCode import *

class Anim_Dialog(PyQt5_QDialog):
    def showDialog(self):
        self.show()
    def setupUI(self):
        self.setFixedSize(1000,600)
        # 设置窗口的背景
        self.setBackground("background.png")
        #添加小恐龙 
        self.top = PyQt5_Qlabel(self,420,390,70,100)
        # 播放gif
        self.playGif(self.top,"frame_fly.gif")

        self.move = QTimer()  
        self.move.timeout.connect(self.horizontalMove)
        self.moveSpeed = 0
        self.move.start(15)

            
 
 # 播放的gif
    def playGif(self, label,gif_name):
        # 确定要播放的gif
        self.gif = PyQt5_QMovie(gif_name)
        # 给gif设置大小
        self.gif.setScaledSize(label.size())
        # 确定label播放哪个gif 
        label.setMovie(self.gif)
        # 播放gif
        self.gif.start()
if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建窗口
    dialog =Anim_Dialog()
    # 设置窗口的属性
    dialog.setupUI()
    # 显示窗口
    dialog.showDialog()
    # 保持应用运行
    app.exec_()