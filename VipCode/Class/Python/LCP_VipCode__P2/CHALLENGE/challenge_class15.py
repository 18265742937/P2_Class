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
        self.label = PyQt5_Qlabel(self, 200, 50, 475, 45)
        # 给问题标签添加文字
        self.label.setText("以下哪位诗人被称为诗仙？")
        self.label.setFontSize(18)

        # 添加组控件，用来盛放四个选项 
        self.groupBox = PyQt5_QGroupBox(self, 220, 90, 300, 150)
        self.groupBox.setBorderWidth(0)
        # 设置选项A
        self.optionA = PyQt5_QRadioButton(self.groupBox, 0, 10, 460, 25)
        self.optionA.setFontSize(15)
        self.optionA.setText("苏轼")
        self.optionA.toggled.connect(lambda:self.checkOptions(0))   

        # 设置选项B
        self.optionB = PyQt5_QRadioButton(self.groupBox, 0, 35, 460, 25)
        self.optionB.setFontSize(15)
        self.optionB.setText("杜甫")
        self.optionB.toggled.connect(lambda:self.checkOptions(1))
        # 设置选项C
        self.optionC = PyQt5_QRadioButton(self.groupBox, 0, 60, 460, 25)
        self.optionC.setFontSize(15)
        self.optionC.setText("李白")
        self.optionC.toggled.connect(lambda:self.checkOptions(2))
        # 设置选项D
        self.optionD = PyQt5_QRadioButton(self.groupBox, 0, 85, 460, 25)
        self.optionD.setFontSize(15)
        self.optionD.setText("白居易")
        self.optionD.toggled.connect(lambda:self.checkOptions(3))
        
        # 创建数组存储
        self.optionsBtn = [self.optionA, self.optionB, self.optionC, self.optionD]
    
     # 单选按钮组绑定的事件
    def checkOptions(self, option):
        pass

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

