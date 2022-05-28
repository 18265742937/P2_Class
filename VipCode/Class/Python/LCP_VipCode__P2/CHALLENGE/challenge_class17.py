from VipCode import *
import random

class UI_Blaming (PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(600, 450)
        # 设置窗口的背景
        self.setBackground("blamingBg.jpg")
        # 创建小猪的label
        self.pigLabel = PyQt5_Qlabel(self, 340, 135, 200, 200)
        self.pigLabel.setBackground("pig.png")
        # 创建玩家的label
        self.playerLabel = PyQt5_Qlabel(self, 120 , 120, 200, 200)
        self.playerLabel.setBackground("main_lion.png")
        # 添加攻击按钮
        self.button = PyQt5_QPushButton(self, 250, 350 , 90, 30)
        self.button.setBackground("attack.png")
        self.button.clicked.connect(self.playGif)
        # 添加血条，血条由n个label组成
        self.label1 = PyQt5_Qlabel(self, 300, 150, 20, 4)
        self.label1.setBackgroundColor('red')
        self.label2 = PyQt5_Qlabel(self, 320, 150, 20, 4)
        self.label2.setBackgroundColor('red')
        self.label3 = PyQt5_Qlabel(self, 340, 150, 20, 4)
        self.label3.setBackgroundColor('red')
        self.label4 = PyQt5_Qlabel(self, 360, 150, 20, 4)
        self.label4.setBackgroundColor('red')
        self.label5 = PyQt5_Qlabel(self, 380, 150, 20, 4)
        self.label5.setBackgroundColor('red')
        self.label6 = PyQt5_Qlabel(self, 400, 150, 20, 4)
        self.label6.setBackgroundColor('red')
        self.label7 = PyQt5_Qlabel(self, 420, 150, 20, 4)
        self.label7.setBackgroundColor('red')
        self.label8 = PyQt5_Qlabel(self, 440, 150, 20, 4)
        self.label8.setBackgroundColor('red')
        self.label9 = PyQt5_Qlabel(self, 460, 150, 20, 4)
        self.label9.setBackgroundColor('red')
        self.label10 = PyQt5_Qlabel(self, 480, 150, 20, 4)
        self.label10.setBackgroundColor('red')
        # 这些label存储到列表中方便使用
        self.labels = [self.label1,self.label2,self.label3,self.label4,self.label5,self.label6,self.label7,self.label8,self.label9,self.label10]
        for x in range(len(self.labels)):
                    self.labels[x].move(self.labels[x].x()+10,150)
                    # 将血量设置回10
                    self.HP=10 
        
        
        
        # 记录最后一个血条下标
        self.HP = 10
    def playGif(self):
        # 点击攻击后隐藏攻击按钮，等攻击结束之后再显示
        self.button.setVisible(False)
        # 确定要播放的gif
        self.gif = PyQt5_QMovie("boxing.gif")
        # 给gif设置大小
        self.gif.setScaledSize(self.playerLabel.size())
        # 确定label播放哪个gif 
        self.playerLabel.setMovie(self.gif)
        # 播放gif
        self.gif.start()
        # 设置空背景相当于清楚原有背景，否则播放gif时会出现重影
        self.playerLabel.setBackground("")
        # 获取gif的帧数
        self.frameCount = self.gif.frameCount()
        # gif帧数改变事件
        self.gif.frameChanged.connect(self.playPigGif)
    def playPigGif(self):
        # 如果动画未播放完一次
        if self.frameCount > 0 :
             # 剩余帧数-1
            self.frameCount -=1
        else :
            # 播放完一次时停止播放gif
            self.gif.stop()
            
        # 打到小猪时（差5帧播放完时打到了小猪）开始播放小猪晕倒的gif
        if self.frameCount == 5:
            self.pigGif = PyQt5_QMovie("pig.gif")
            # 给gif设置大小
            self.pigGif.setScaledSize(self.pigLabel.size())
            # 确定label播放哪个gif 
            self.pigLabel.setMovie(self.pigGif)
            # 播放gif
            self.pigGif.start()
            # 设置空背景相当于清楚原有背景，否则播放gif时会出现重影
            self.pigLabel.setBackground("")
            # 获取gif的帧数
            self.pigframeCount = self.pigGif.frameCount()
            # gif帧数改变事件
            self.pigGif.frameChanged.connect(self.pigGifChange)
    def pigGifChange(self):
        # 如果小猪gif没有播放完一次
        if self.pigframeCount > 0:
            # 剩余帧数-1
            self.pigframeCount -=1
        else :
            # 播放完gif设置攻击按钮可见
            self.button.setVisible(True)
            # 小猪gif停止播放
            self.pigGif.stop()
        # 小猪倒地时（差5帧播放完成）生命值减少
        if 5 == self.pigframeCount:
            pass
                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Blaming()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()
