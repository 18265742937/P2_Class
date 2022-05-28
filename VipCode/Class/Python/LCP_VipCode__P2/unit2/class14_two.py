#导入工具
from VipCode import *  # *代表全部的意思


#创建一个类
class Dialog_Second(PyQt5_QDialog):  
    #定义显示窗口的函数   self代表当前的窗口
    def show_Dialog(self):
        #显示这个窗口
        self.show()


    #窗口UI的函数
    def ui_Dialog(self):
        #设置窗口大小
        self.setFixedSize(620,600)
        #设置窗口的标题
        self.setWindowTitle("答题界面")
        #设置窗口的背景
        self.setBackground("answerBg.png")

        #创建label
        self.label = PyQt5_Qlabel(self,65,30,475,45)
        #设置label字体
        self.label.setFontSize(17)
        #设置label自动换行
        self.label.setWordWrap(True)
            #True : 允许自动换行
            #False : 不允许自动换行

        #随机题号
        num = [5,49,4,43,7,49,39,26,32,11,15]
        self.number = random.choice(num)
        #获取对应为的问题详情
        # self.question = getQuestion(self.number)
        self.question = getQuestion(self.number)
        #输出问题详情
        print(self.question)
        #输出问题
        print(self.question["wenti"])
        #使用label加载问题内容
        self.label.setText(self.question["wenti"])

 #开始-----------------------------------------------------------------
        #单选按钮组
        self.groupBox = PyQt5_QGroupBox(self, 50, 80, 500, 200)
        #设置group的边框宽度
        self.groupBox.setBorderWidth(0)
        #创建选项A单选按钮  (添加radiobutton组件)---小圆
        self.optionA = PyQt5_QRadioButton(self.groupBox, 30, 10, 460, 25)
        #设置选项A的文字
        self.optionA.setText(self.question["a"])
        #设置选项A的文字大小
        self.optionA.setFontSize(15)
        #创建选项B单选按钮
        self.optionB = PyQt5_QRadioButton(self.groupBox, 30, 50, 460, 25)
        #设置选项B的文字
        self.optionB.setText(self.question["b"])
        #设置选项B的文字大小
        self.optionB.setFontSize(15)

        #当单选按钮被选中会调用toggleg, 带参需要添加lambda
        self.optionA.toggled.connect(lambda:self.checkOptions(0))
        self.optionB.toggled.connect(lambda:self.checkOptions(1))
        #创建列表存储
        self.optionsBtn = [self.optionA, self.optionB]
#结束-------------------------------------------------------------------

#开始-------------------------------------------------------------------
    #单选按钮组被选定的事件
    def checkOptions(self,option):
        #判断选择的是哪一个
        if self.optionsBtn[option].isChecked() == True:
            print(option)
#结束-------------------------------------------------------------------





#程序的入口(大门)
if __name__ == "__main__":
    #通过QApplication来创建程序
    app = QApplication(sys.argv)
    #创建一个窗口类对象
    dialog = Dialog_Second()  
    #调用美化窗口函数
    dialog.ui_Dialog()
    #通过对象去调用显示这个窗口的函数
    dialog.show_Dialog()
    #让程序持续保持运行
    app.exec_()

