# @Author: 茄子 
# @Date: 2019-09-11 12:57:21   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-11 12:57:21  
# @Description:  "第十四课  读心术"


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

choose = int(input('你选择的牌在第几列：'))
print('你选择的牌在第%d列。' % choose)









