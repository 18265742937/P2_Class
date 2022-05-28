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
        #创建选项C单选按钮
        self.optionC = PyQt5_QRadioButton(self.groupBox, 30, 90, 460, 25)
        #设置选项C的文字
        self.optionC.setText(self.question["c"])
        #设置选项C的文字大小
        self.optionC.setFontSize(15)
        #创建选项D单选按钮
        self.optionD = PyQt5_QRadioButton(self.groupBox, 30, 130, 460, 25)
        #设置选项D的文字
        self.optionD.setText(self.question["d"])
        #设置选项D的文字大小
        self.optionD.setFontSize(15)

        #当单选按钮被选中会调用toggleg, 带参需要添加lambda
        self.optionA.toggled.connect(lambda:self.checkOptions(0))
        self.optionB.toggled.connect(lambda:self.checkOptions(1))
        self.optionC.toggled.connect(lambda:self.checkOptions(2))
        self.optionD.toggled.connect(lambda:self.checkOptions(3))
        #创建列表存储
        self.optionsBtn = [self.optionA, self.optionB, self.optionC, self.optionD]

#开始--------------------------------------------------------------------
        #添加解释label组件
        self.analysis = PyQt5_Qlabel(self, 50, 280, 500, 220)
        #设置背景图片
        self.analysis.setBackground("answer_analysis.png")
        #设置文字大小
        self.analysis.setFontSize(15)
        #设置居左和顶部对齐
        self.analysis.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        #设置解析文字左边距为30 上边距为40, 右边距为30, 没有下边距
        self.analysis.setContentsMargins(30, 40, 30, 0)
        #设置允许换行
        self.analysis.setWordWrap(True)
        #是指解析文字
        self.analysis.setText(self.question["jiexi"])
        #将解释设置为不可见
        self.analysis.setVisible(False)
#结束-------------------------------------------------------------------

#将解析中显示的文字增大两个字号, 并设置为紫色

    """
    封装事件
    """
    #单选按钮组被选定的事件
    def checkOptions(self,option):
        #判断选择的是哪一个
        if self.optionsBtn[option].isChecked() == True:
            #正确选项为蓝色, 其余选项为灰色
            for x in range(len(self.optionsBtn)):
                #设置字体颜色为灰色
                self.optionsBtn[x].setTextColor("grey")
            index = int(self.question["daan"])
            #判断是否正确
            if index == option:
                self.optionsBtn[option].setTextColor("blue")
            else:
                #设置文字颜色为红色
                self.optionsBtn[option].setTextColor("red")
                self.optionsBtn[index].setTextColor("blue")
            #设置圆按钮不可再次被点击
            self.groupBox.setEnabled(False) 
            #将解释设置为可见
            self.analysis.setVisible(True) #添加代码--------------------------------------  




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