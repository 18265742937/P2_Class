from VipCode import *  # *代表全部的意思
import wmi
import os


class Dialog_First(PyQt5_QDialog):
    def __init__(self):
        super().__init__()
        self.s = 0
        self.w = wmi.WMI()
        # global list
        self.list = []

    def show_Dialog(self):
        self.show()

    def ui_Dialog(self):
        self.setFixedSize(650, 500)
        self.setWindowTitle("电脑信息")
        self.setBackgroundColor("#C1FFC1")
        self.label = PyQt5_Qlabel(self, 60, 0, 650, 500)
        self.label.setTextColor("#7B68EE")
        self.label.setFontSize(22)
        self.label.setText(self.main())

    def info(self):
        # self.list.append("电脑信息")
        for BIOSs in self.w.Win32_ComputerSystem():
            self.list.append("电脑名称: %s" % BIOSs.Caption)
            self.list.append("使 用 者: %s" % BIOSs.UserName)
        for address in self.w.Win32_NetworkAdapterConfiguration(ServiceName="e1dexpress"):
            self.list.append("IP地址: %s" % address.IPAddress[0])
            self.list.append("MAC地址: %s" % address.MACAddress)
        for BIOS in self.w.Win32_BIOS():
            self.list.append("使用日期: %s" % BIOS.Description)
            self.list.append("主板型号: %s" % BIOS.SerialNumber)
        for processor in self.w.Win32_Processor():
            self.list.append("CPU型号: %s" % processor.Name.strip())
        for memModule in self.w.Win32_PhysicalMemory():
            totalMemSize = int(memModule.Capacity)
            self.list.append("内存厂商: %s" % memModule.Manufacturer)
            self.list.append("内存型号: %s" % memModule.PartNumber)
            self.list.append("内存大小: %.2fGB" % (totalMemSize/1024**3))
        for disk in self.w.Win32_DiskDrive(InterfaceType="IDE"):
            diskSize = int(disk.size)
            self.list.append("磁盘名称: %s" % disk.Caption)
            self.list.append("磁盘大小: %.2fGB" % (diskSize/1024**3))
        for xk in self.w.Win32_VideoController():
            self.list.append("显卡名称: %s" % xk.name)

    def main(self):
        s = """"""
        global path
        path = "c:/systeminfo"
        for BIOSs in self.w.Win32_ComputerSystem():
            UserNames = BIOSs.Caption
        fileName = path+os.path.sep+UserNames+".txt"
        self.info()

        #判断文件夹（路径）是否存在
        if not os.path.exists(path):
            print("不存在")
            #创建文件夹（文件路径）
            os.makedirs(path)
            #写入文件信息
            with open(fileName, 'w+') as f:
                for li in self.list:
                    print(li)
                    l = li+"\n"
                    f.write(l)
        else:
            print("存在")
            with open(fileName, 'w+') as f:
                for li in self.list:
                    # print(li)
                    s += (li+"\n")
                    l = li+"\n"
                    f.write(l)
        return s


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog_First()
    dialog.ui_Dialog()
    dialog.show_Dialog()
    app.exec_()
