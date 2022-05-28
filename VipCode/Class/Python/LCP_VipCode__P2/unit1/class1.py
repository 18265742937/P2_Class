
# @Author: 茄子
# @Date: 2019-07-30 11:47:08
# @Last Modified by:   茄子
# @Last Modified time: 2019-07-30 11:47:08
# @Description:  "第二课 第一个窗口"

#导入工具
from VipCode import *  # *代表全部的意思


#创建一个类
class Dialog_First(PyQt5_QDialog):
    #定义显示窗口的函数   self代表当前的窗口
    def show_Dialog(self):
        #显示这个窗口
        self.show()

#程序的入口(大门)
if __name__ == "__main__":
    #通过QApplication来创建程序
    app = QApplication(sys.argv)
    #创建一个窗口类对象
    dialog = Dialog_First()
    #通过对象去调用显示这个窗口的函数
    dialog.show_Dialog()
    #让程序持续保持运行
    app.exec_()


    # pip list查看已经安装的工具
    
    # pip  install - ihttps: // pypi.mirrors.ustc.edu.cn / simple / PyQt5
    
#工具栏
    #资源管理器/文件管理器
        #新建文件
        #新建文件夹
        #重命名
        #删除
    #应用商店   作用:安装插件(包)

#菜单栏
    #文件
        #打开文件夹
        #自动保存
    #帮助
        #欢迎使用
            #最近