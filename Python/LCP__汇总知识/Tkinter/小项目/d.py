import tkinter as tk
from tkinter import*
from time import sleep
import tkinter.messagebox
import sys


class start():

    def __init__(self):
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

        self.answers = ["状态变化的方式", "b/s", "103", "光学的",
                        "存储", "-3", "28/31", "-1", "0.5", "惯性定律", " "]

    def work(self):
        window = tk.Tk()
        window.title("准备测试")
        window.configure(bg="orange")
        window.geometry("500x300")
        self.label = Label(window, text="考试准备", fg="blue", bg="orange", font="SansSerif 30 bold")
        self.label.pack()
        # print(type(self.label))
        self.la = Label(window, text="准考证号", fg="green", bg="orange", font="SansSerif 10 bold")
        self.la.pack()
        self.a = tk.Entry(window, show=None)
        self.a.pack()
        self.lab = Label(window, text="考生姓名", fg="green", bg="orange", font="SansSerif 10 bold")
        self.lab.pack()
        self.b = tk.Entry(window, show=None)
        self.b.pack()
        lab_empty = Label(window, text="                ", fg="green", bg="orange", font="SansSerif 10 bold")
        lab_empty.pack()
        bt = Button(window, text="确认考生信息", fg="green", bg="orange", font="SansSerif 10 bold", command=self.right_click)
        bt.pack()
        window.mainloop()

#------------------------------------------------------------------------------

    def right_click(self):
        # tk.messagebox.showinfo(title="考生注意",messange="本次考试共10道题,每题10分,共100分")
        tkinter.messagebox.showinfo(title='考生注意', message='本次考试共10道题,每题10分,共100分')
        self.start_answer()

#------------------------------------------------------------------------------

# class answer_page(start):
    def start_answer(self):
        """
        答题主界面
        """
        self.var = tk.StringVar()
        self.v = tk.StringVar()
        self.question_number = 0  # --------题号

        self.time = 0
        self.marks = 0  # 计分器
        self.page = tk.Tk()
        self.page.title("考试界面")
        self.page.configure(bg="orange")
        self.page.geometry("700x400")
        # self.Qe=tk.Label(self.page, textvariable=self.var,fg="blue",bg="green",font=('Arial', 12), width=30, height=2)
        self.Qe = tk.Label(self.page, text=self.questions[0], fg="blue", bg="green", font=('Arial', 12), width=30, height=2)
        self.Qe.pack()
        # print(self.questions[0])
        self.var.set(self.questions[self.question_number])

        Q = tk.Label(self.page, text="作答区域", fg="blue",
                     bg="orange", font="SansSerif 10 bold")
        Q.pack()
        self.c = tk.Entry(self.page, show=None)
        self.c.pack()
        self.btn = Button(self.page, text="下一题", fg="green", bg="orange", font="SansSerif 10 bold", command=self.next_click)
        self.btn.pack()
        self.page.mainloop()


    def next_click(self):
        """
        下一题按钮
        """
        if self.question_number <= 10:
            self.question_number += 1
            if self.question_number == 10:
                #     self.v.set("答题完毕")
                self.var.set(self.questions[self.question_number])
                tkinter.messagebox.showinfo(title=self.lab, message=self.marks)

            # else:
            # self.var.set(self.questions[self.question_number])
                # self.var.set("qiezi")
            # self.Qe = tk.Label(self.page, text=self.questions[self.question_number], fg="blue", bg="green", font=('Arial', 12), width=30, height=2)
            # self.Qe.pack()
            self.Qe["text"] = "啊哈哈哈"

            if self.c.get() == self.answers[self.question_number]:
                #判断答案是否正确
                self.addmarks()
            else:
                pass


    def addmarks(self):
        #加十分
        self.marks += 10

        # if self.question_number==20:
        #     pass

        # else:
        #     print(self.question_number)
        #     # Start=answer_page()
        #     # Start.start_answer()
        #     #这两行不对， 在这里需要改变标签中的内容
        #     #思路： 点击按钮， 触犯这个函数 ， 改变标签中的文字
        #     self.Qe=tk.Label(self.page,text=self.questions[self.question_number],fg="blue",bg="orange",font="SansSerif 15 bold")
        #     self.Qe.pack()
        #     self.Qe.delete(0, END)

    # def final_page(self):
    #     pass

# class final(answer_page):
#     def start_final(self):
#         f=tk.Tk()
#         f.title("考试结束")
#         f.configure(bg="orange")
#         f.geometry("700x400")
#         Finish=tk.Label(f,text="考试结束,你的得分为：",fg="blue",bg="orange",font="SansSerif 28 bold")
#         Finish.pack()
#         s=tk.Label(f,text=self.marks,fg="blue",bg="orange",font="SansSerif 28 bold")
#         s.pack()


if __name__ == "__main__":
    Start = start()
    Start.work()

