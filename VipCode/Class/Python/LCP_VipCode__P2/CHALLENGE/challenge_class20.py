from VipCode import *
import random

class UI_Hamster (PyQt5_QDialog):
    def setupUI(self):
         # 创建一个特殊的组件类似于窗口，不同的是没有边框，并且可以只显示控件（透明）
        self.framelessBox = PyQt5_FramelessBox()



        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Hamster()
    dialog.setupUI()
    # dialog.show()
    dialog.framelessBox.show()
    app.exec_()