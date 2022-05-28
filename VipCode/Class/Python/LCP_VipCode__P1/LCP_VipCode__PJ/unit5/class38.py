import random

score = [0, 0]
part = ['玩家', '电脑', '玩家']


def shoot(x):
    if x == 0:
        print('==== 轮到你来射门了！ ====')
    else:
        print('==== 轮到你来防守了！ ====')
    p_direction = input('选择方向（左, 中, 右）:')
    direction = ['左', '中', '右']
    c_direction = random.choice(direction)
    if p_direction != c_direction:
        print(part[x] + '射门成功！')
        score[x] += 1
    else:
        print(part[x + 1] + '防守成功！')
    print('得分: %d(玩家) - %d(电脑)' % (score[0], score[1]))

#开始-----------------------------------------------------------------------------------
count = 1
while True:
    print("====第%d回合====" % count)
    shoot(0)
    shoot(1)
    if score[0] + (5 - count) < score[1] or score[1] + (5 - count) < score[0]:
        break
    count += 1

i = 6
while score[0] == score[1]:
    print("====第%d回合====" % i)
    shoot(0)
    shoot(1)
    i += 1
    if i == 7:
        break


if score[0] == score[1]:
    print("平局")
else:
    if score[0] > score[1]:
        print('你击败了电脑！')
    else:
        print('我还会回来的！')
#结束----------------------------------------------------------------------------
