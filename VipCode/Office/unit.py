# @Author: 茄子
# @Date: 2019-12-07 11:15:17
# @Last Modified by:  茄子
# @Last Modified time: 2019-12-07 11:15:17
# @Description:  "读取文件"

#coding = utf-8
from random import choice as c

while True:

    name = input("请您输入孩子的名字: ")
    td = input("孩子本单元的学习态度/优点/缺点: (加名字):")
    print("\n")
    print("向您反馈一下在本单元的学习中{0}课上的表现以及学习状况和学习态度, 基本每节课课上的时候都会先查看{0}的课后作业的完成情况, 然后让{0}回忆了上节课所学习到的知识点, 并进行简单的提问检测孩子对上节课知识点的掌握情况, 在本节课的学习中{1} 总体{0}的表现非常的优秀, 希望{0}在后期的编程学习中再接再厉, 继续加油!".format(name, td))
    print("\n")
