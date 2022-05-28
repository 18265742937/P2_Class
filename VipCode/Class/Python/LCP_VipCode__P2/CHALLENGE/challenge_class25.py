from VipCode import *
class Anim_Dialog(PyQt5_QDialog):
    def showDialog(self):
        self.show()
    def setupUI(self):

        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(600, 600)
        # 设置窗口的背景
        self.setBackgroundColor("rgb(3,3,3)")
        # 添加魔法球组件
        self.label = PyQt5_Qlabel(self,200,200,200,200)
        self.label.setBackground("magicBall.png")
        # 创建label的动画
        self.anim = PyQt5_Animation(self.label)
     

      
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