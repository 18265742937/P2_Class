from random import choice as c

while True:

    cc = input("请您输入孩子的名字: ")
    cs = input("请输入单元: ")
    cf = input("请输入本单元学习的知识点: ")
    print("\n")
    print(r"您好家长, 我们{1}的学习已经完成, 本单元学习的主要知识点有: {2}, 在本单元的学习中{0}的表现非常的出色, 每次课前{0}都可以提前进入教室, 及时做好各项课前准备工作, 课上的状态也很棒, 尤其是笔记方面, {0}记录的笔记非常的详细,很认真可以看出孩子的态度非常的端正, 课上遇到问题孩子可以及时的向老师进行询问, 每次课后作业基本都能高质量的完成, 课后在完成课后作业的时候遇到不理解的地方也都可以及时通过微信向老师进行询问获取老师的帮助, 大部分的课后作业都能独立完成, 课后的业余时间{0}也可以及时的复习相应的课堂笔记, 总体这这一阶段的学习中{0}表现的非常优秀, 希望{0}在后面的学习中再接再厉,继续加油!".format(cc, cs, cf))
    print("\n")
    
