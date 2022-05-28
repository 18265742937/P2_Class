import tkinter as tk
from tkinter import* 
from time import sleep
import tkinter.messagebox
import sys

class start():
    def __init__(self):
        """
        初始化函数
        """
        self.questions = [
            "1. 从认识论层次来看，信息是指：“事物运动的状态及___",
            "2. 数据通信中比特的传输率单位是___",
            "3.十进制数 67 的转换成八进制数是___",
            "4.信息处理系统按技术手段分类，可分为机械的、电子的和___",
            "5.现代信息处理系统中，为了消除人们使用信息的时间障碍，而使用___技术",
            "6.一次函数y=-x-3与x轴交点的横坐标为___",
            "7.磷酸氢二铵中磷元素和氮元素的质量比为___(用分数线'/')",
            "8.二次函数y=2(x+1)(x-3)的对称轴为直线x=___",
            "9.30度角的正切值为___(用小数)",
            "10.牛顿第一定律又被称为什么？___",
            "答题完毕！ 请看得分："
        ]  # --------题库


    def work(self):
        """
        主界面
        """
        window=tk.Tk()
        window.title("准备测试")
        window.configure(bg="orange")
        window.geometry("500x300")
        label=Label(window,text="考试准备",fg="blue",bg="orange",font="SansSerif 30 bold")
        label.pack()
        print(type(label))
        la=Label(window,text="准考证号",fg="green",bg="orange",font="SansSerif 10 bold")
        la.pack()
        a=tk.Entry(window,show=None)
        a.pack()
        lab=Label(window,text="考生姓名",fg="green",bg="orange",font="SansSerif 10 bold")
        lab.pack()
        b=tk.Entry(window,show=None)
        b.pack()
        lab_empty=Label(window,text="                ",fg="green",bg="orange",font="SansSerif 10 bold")
        lab_empty.pack()
        bt=Button(window,text="确认考生信息",fg="green",bg="orange",font="SansSerif 10 bold",command=self.right_click)
        bt.pack()
        window.mainloop()

    # def right_click(self):
    #     """
    #     确认信息按钮---> 默认题
    #     """
    #     print("茄子")

    def right_click(self):
        self.page = tk.Tk()
        self.page.title("考试界面")
        self.page.configure(bg="orange")
        self.page.geometry("700x400")
        self.Qe = tk.Label(self.page, textvariable=self.var, fg="blue", bg="orange", font="SansSerif 15 bold")
        self.var.set(self.questions[0])
        self.Qe.pack()
        Q = tk.Label(self.page, text="作答区域", fg="blue",bg="orange", font="SansSerif 10 bold")
        Q.pack()
        self.c = tk.Entry(self.page, show=None)
        self.c.pack()
        self.btn = Button(self.page, textvariable=self.v, fg="green", bg="orange", font="SansSerif 10 bold", command=self.next_click)
        self.v.set("下一题")
        self.btn.pack()
        self.page.mainloop()



if __name__ == "__main__":
    Start=start()
    Start.work()
