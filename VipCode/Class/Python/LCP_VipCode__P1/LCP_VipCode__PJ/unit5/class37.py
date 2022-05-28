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

shoot(0)
shoot(1)

if score[0] > score[1]:
    print('你击败了电脑！')
elif score[0] == score[1]:
    print('再来一次！')
else:
    print('我还会回来的！')
