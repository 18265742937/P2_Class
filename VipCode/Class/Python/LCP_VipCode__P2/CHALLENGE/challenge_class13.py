from VipCode import *
import random

class UI_Dice(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(960, 600)
        self.setWindowTitle("摇骰子")
        self.setBackground("mainBg.png")

        # 添加摇骰子的比赛结果label
        self.label_result = PyQt5_Qlabel(self, 360, 50, 250, 50)
        self.label_result.setFont(QFont('手札体-简',26,QFont.Bold))

        # 添加摇骰子按钮和点击事件
        self.shaizi = PyQt5_QPushButton(self, 100, 380, 57, 57)
        self.shaizi.setBackground("dice_normal.png")
        self.shaizi.setPressedBackground("dice_pressed.png")
        self.shaizi.clicked.connect(self.shaiziClicked)

        # 添加边框label
        self.label_1 = PyQt5_Qlabel(self, 200, 170, 250, 400)
        self.label_1.setBackground('group_8.png')
        self.label_2 = PyQt5_Qlabel(self, 500, 170, 250, 400)
        self.label_2.setBackground('group_8.png')

        # 添加玩家和电脑字样label
        self.label_11 = PyQt5_Qlabel(self, 290, 250, 250, 400)
        self.label_11.setText('玩家')
        self.label_11.setFont(QFont('手札体-简',26,QFont.Bold))
        self.label_22 = PyQt5_Qlabel(self, 600, 250, 250, 400)
        self.label_22.setText('电脑')
        self.label_22.setFont(QFont('手札体-简',26,QFont.Bold))

        # 添加玩家和电脑骰子的label
        self.label = PyQt5_Qlabel(self, 270, 300, 100, 100)
        self.label_comp = PyQt5_Qlabel(self, 580, 300, 100, 100)
    
    # 摇骰子的响应结果    
    def shaiziClicked(self):
        pass
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Dice()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()
        
       


        

        
        
        

    

