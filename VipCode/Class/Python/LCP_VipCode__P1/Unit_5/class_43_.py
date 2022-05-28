# @Author: 茄子 
# @Date: 2019-09-11 16:12:18   
# @Last Modified by:  茄子  
# @Last Modified time: 2019-09-11 16:12:18  
# @Description:  "第四十三课  点球大战(一)"

#导入工具
import random
#存放成绩
score = [0, 0]
#存放方向
direction = ['左', '中', '右']  

#半局比赛
def shoot(c):
    if c == 0:
        print('==== 轮到你来射门了！ ====')
    else:
        print('==== 轮到你来防守了！ ====')
    a = input('选择方向（左, 中, 右）:')
    b = random.choice(direction)
    if a != b:
        print('射门成功！')
        score[c] += 1
    else:
        print('防守成功！')
    print('得分: %d(玩家) - %d(电脑)' % (score[0], score[1]))

shoot(0)
shoot(1)

if score[0] > score[1]:
    print('你击败了电脑！')
else:
    print('我还会回来的！')



