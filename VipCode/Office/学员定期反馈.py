#coding = utf-8
from random import choice as c
while True:
    print("")
    names = input("请您输入孩子的名字: ")
    biaoxian = input("孩子近期课上的表现: ")
    f = f"您好{names}家长, 向您反馈一下孩子近期的学习状态以及课上表现: {biaoxian}" \
        f". 总体而言, {names}的表现非常的优秀, 希望{names}再接再厉, 继续加油! 茄子会定期向您反馈孩子课上的表现以及学习状态, "\
        f"您或者孩子遇到什么问题以及需要请假或者加课等都可以在群里联系茄子或者班主任老师的, 咱们紧密联系, 帮助孩子更好的学习编程!"\
        f"最后祝您以及您的家人, 阖家欢乐, 万事如意!"
    print("")
    print(f)
    print("")
    print("#"*150)