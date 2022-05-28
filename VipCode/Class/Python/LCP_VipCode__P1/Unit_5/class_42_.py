# @Author: 茄子 
# @Date: 2019-09-11 15:59:34   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-11 15:59:34  
# @Description:  "第四十二课  读心术(三)"



import random

h = '黑桃 红桃 方片 梅花'.split()
s = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
p = []
for i in h:
    for j in s:
        temp = i + ' ' + j
        p.append(temp)

list = random.sample(p, 21)

list1 = []
list2 = []
list3 = []

for i in range(7):
    list1.append(list[3 * i])
    list2.append(list[3 * i + 1])
    list3.append(list[3 * i + 2])

print(list1)
print(list2)
print(list3)

for i in range(3):
    a = list2 + list1 + list3
    b = list3 + list1 + list2
    choose1 = [a, b]
    c = list1 + list2 + list3
    d = list3 + list2 + list1
    choose2 = [c, d]
    e = list1 + list3 + list2
    f = list2 + list3 + list1
    choose3 = [e, f]

#开始------------------------------------------------------------------
    while True:
        choose = int(input('你选择的牌在第几列：'))
        if choose == 1:
            list = random.choice(choose1)
            break
        elif choose == 2:
            list = random.choice(choose2)
            break
        elif choose == 3:
            list = random.choice(choose3)
            break
        else:
            print("输入错误, 请重新输入!")
#结束---------------------------------------------------------------------

    list1 = []
    list2 = []
    list3 = []

    for i in range(7):
        list1.append(list[3 * i])
        list2.append(list[3 * i + 1])
        list3.append(list[3 * i + 2])

    print(list1)
    print(list2)
    print(list3)

print('我猜出来了，你选择的牌是%s!' % list2[3])























