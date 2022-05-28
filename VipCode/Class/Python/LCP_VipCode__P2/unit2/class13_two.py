#导入工具
from VipCode import *  # *代表全部的意思

#创建一个类
class Dialog_Second(PyQt5_QDialog):  
    #定义显示窗口的函数   self代表当前的窗口
    def show_Dialog(self):
        #显示这个窗口
        self.show()

#开始-------------------------------------------------------------------------
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
        self.question = getQuestion(self.number)
        #输出问题详情
        print(self.question)
        #输出问题
        print(self.question["wenti"])
        #使用label加载问题内容
        self.label.setText(self.question["wenti"])
        
#结束---------------------------------------------------------------------------

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



"""
{'id': 26, 
'wenti': '下列哪个不是北京的别称？', 
'daan': '2', 
'jiexi': 'A:大都，元代以金的离宫今北海公园为中心重建新城
，元世祖至元九年（1272年）改称大都，俗称元大都。\nB:中都，泛指中国历史上的古都。亦指中国历史上不同朝代的国都，首都， 
中京。主指九(最多)朝古都洛阳，三朝古都北京。\nC:上都，即夏都，遗址在今内蒙古正蓝旗东20千米的闪电河北岸。\nD:南京，辽 
太宗会同元年（938年），将原来的幽州升为幽都府，建号南京，又称燕京，作为辽的陪都。当时辽的首都在上京。', 
'd': '南京', 
'a': '大都', 
'b': '中都', 
'c': '上都'}


窗口内部不能直接添加图片/动画/文字, 需要先在窗口中添加标签, 然后在标签中添加以上内容

"""
