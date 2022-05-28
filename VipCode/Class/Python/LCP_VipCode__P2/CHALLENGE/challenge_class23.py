from VipCode import *
class Anim_Dialog(PyQt5_QDialog):
    def showDialog(self):
        self.show()
    def setupUI(self):

        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(960, 600)
        # 设置窗口的背景
        self.setBackgroundColor("rgb(20,20,20)")
        # 第一根线
        self.label1 = PyQt5_Qlabel(self,0,50,320,80)
        self.label1.setBackground("line1.png")
        # 后两跟线
        # self.label2 = PyQt5_Qlabel(self,0,130,320,80)
        # self.label2.setBackground("line2.png")
        # self.label3 = PyQt5_Qlabel(self,0,210,320,80)
        # self.label3.setBackground("line3.png")
        

        
       

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