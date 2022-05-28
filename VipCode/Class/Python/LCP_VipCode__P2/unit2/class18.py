from VipCode import *

class Dialog_First(PyQt5_QDialog):

    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(640, 360)
        # 设置窗口的背景
        self.setBackground("battleBg.png")
        self.heros = ["不知火舞","东皇太一","兰陵王","关羽","后羿","周瑜","大乔","妲己","安琪拉","宫本武藏",
        "扁鹊","曹操","狄仁杰","白起","花木兰","蔡文姬","貂蝉","达摩","阿轲","黄忠"]

        # 添加第一个显示英雄的标签组件
        self.first_hero = PyQt5_Qlabel(self, 90, 90, 100, 170)
        # 添加第二个显示英雄的标签组件
        self.second_hero = PyQt5_Qlabel(self, 210, 90, 100, 170)
        # 添加第三个显示英雄的标签组件
        self.third_hero = PyQt5_Qlabel(self, 330, 90, 100, 170)
        # 添加第四个显示英雄的标签组件
        self.fourth_hero = PyQt5_Qlabel(self, 450, 90, 100, 170)

        self.clicked()
        
        # 添加音效播放器 
        self.media = PyQt5_QMediaPlayer()
        # 加载将要播放的音乐
        self.media.prepare_audio('battleBg.mp3')
        # 播放音效，0为无限循环
        # self.media.play(0)

        # 添加重置按钮
        self.resetBtn = PyQt5_QPushButton(self, 272, 305, 96, 40)
        # 设置按钮的背景图片
        self.resetBtn.setBackground("reset_normal.png")
        # 设置按钮被按压时的 图片
        self.resetBtn.setPressedBackground("reset_pressed.png")
        # 绑定重置按钮的点击事件
        self.resetBtn.clicked.connect(self.clicked)
      
    # 重置按钮的点击事件
    def clicked(self):
        # 随机4个英雄进行存储
        self.list = random.sample(self.heros, 4)
        # 显示第一个英雄
        self.first_hero.setBackground(self.list[0]+".jpg")
        # 显示第二个英雄
        self.second_hero.setBackground(self.list[1]+".jpg")
        # 显示第三个英雄
        self.third_hero.setBackground(self.list[2]+".jpg")
        # 显示第四个英雄
        self.fourth_hero.setBackground(self.list[3]+".jpg")

if __name__ == "__main__":   #该程序的入口
    app = QApplication(sys.argv)    #应用程序  =货架子
    dialog = Dialog_First()   #创建窗口类对象
    dialog.ui_Dialog()  #通过对象去调用
    dialog.show_Dialog()   #通过对象去调用显示这个窗口的函数
    app.exec_()   #让程序持续保持运行