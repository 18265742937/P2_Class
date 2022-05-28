from VipCode import *

class UI_TiePi(PyQt5_QDialog):

    # 创建窗口的方法
    def showDialog(self):
        self.show()
        
    # 美化窗口的方法
    def setupUI(self):
        self.setWindowTitle("动植物分类")
        self.setFixedSize(960, 600)
        self.setBackground("challengeBg_8.png")

        self.plantGroup = PyQt5_QGroupBox(self, 200, 160, 250, 400)
        self.plantGroup.setBackground("group_8")


        self.animal1 = PyQt5_Qlabel(self, 170, 10, 50, 50)
        self.animal1.setBackground("animal_1.png")
        self.animal2 = PyQt5_Qlabel(self, 330, 10, 50, 50)
        self.animal2.setBackground("animal_2.png")
        self.animal3 = PyQt5_Qlabel(self, 490, 10, 50, 50)
        self.animal3.setBackground("animal_3.png")
        self.animal4 = PyQt5_Qlabel(self, 650, 10, 50, 50)
        self.animal4.setBackground("animal_4.png")
        self.animal5 = PyQt5_Qlabel(self, 810, 10, 50, 50)
        self.animal5.setBackground("animal_5.png")

        self.plant1 = PyQt5_Qlabel(self.plantGroup, 90, 10, 50, 50)
        self.plant1.setBackground("plant_1.png")
        self.plant2 = PyQt5_Qlabel(self, 250, 10, 50, 50)
        self.plant2.setBackground("plant_2.png")
        self.plant3 = PyQt5_Qlabel(self, 410, 10, 50, 50)
        self.plant3.setBackground("plant_3.png")
        self.plant4 = PyQt5_Qlabel(self, 570, 10, 50, 50)
        self.plant4.setBackground("plant_4.png")
        self.plant5 = PyQt5_Qlabel(self, 730, 10, 50, 50)
        self.plant5.setBackground("plant_5.png")
        
        
        #----------------------------------代码书写位置----------------------------------#
        # self.plantGroup = PyQt5_QGroupBox(self, 200, 160, 250, 400)
        # self.plantGroup.setBackground("group_8")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口类对象
    dialog = UI_TiePi()
    # 美化窗口的方法
    dialog.setupUI()
    # 显示窗口
    dialog.showDialog()
    # 让应用一直保持运行状态
    app.exec_()
