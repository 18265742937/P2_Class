from VipCode import *

class UI_Challenge(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(600, 400)
        # 设置窗口的标题
        self.setWindowTitle("挑战")
        # 设置窗口的背景
        self.setBackground("challengeBg_14.png")
        # 添加问题标签控件， 设置位置以及大小
        self.label = PyQt5_Qlabel(self, 100, 50, 400, 200)
        # 给问题标签添加文字
        self.label.setText(r"又一阵晚风吹过，是海潮在低吟，还是松涛在呼唤？原来那是千万株大叶杨，看见了萤火虫在它们身边翩翩起舞，舞姿分外轻柔动人，于是也发出了欢乐的笑声：“哗--哗--” 再仔细地一听，青蛙在水稻田里纵情地歌唱，小虫儿在玉米地呼唤伙伴，蚯蚓钻在地底下说悄悄话。还有那草丛中的蛐蛐，像是在唱歌，又像是在弹琴。歌声啊阵阵，琴声啊悠悠，莫不是妈妈在把它呼唤……哦，美丽的夏夜！如果不是清凉、湿润的夜露提醒了我，我将会陪伴你到黎明。")
        \n


if __name__ == '__main__':
    #创建一个应用
    app = QApplication(sys.argv)
    # 创建类对象
    dialog = UI_Challenge()
    # 调用美化窗口方法
    dialog.setupUI()
    # 显示窗口
    dialog.showDialog()
    #让应用一直保持运行状态
    app.exec_()

