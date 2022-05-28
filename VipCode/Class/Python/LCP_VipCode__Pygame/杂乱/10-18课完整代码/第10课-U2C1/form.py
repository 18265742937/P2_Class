import pygame,sys,random
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()
playSurface = pygame.display.set_mode((640,480))                        # 设置界面
pygame.display.set_caption("贪吃蛇游戏")                                 # 设置标题
redColor = pygame.Color(255,0,0)                                        # 红颜色
blackColor = pygame.Color(0,0,0)                                        # 黑颜色
whiteColor = pygame.Color(255,255,255)                                  # 白颜色
snakeSegments = [[100,100],[80,100],[60,100]]                           # 蛇身体坐标--列表嵌套
foodPosition = [300,300]                                                # 食物坐标--食物是 20*20 小方块 

for x in range(0,640,20):                                               # 双重for循环完成方格坐标 
    for y in range(0,480,20):
        pygame.draw.rect(playSurface, whiteColor, (x,y,20,20), 1)

old_x = 0                                                               # 定义变量
old_y = 0

while True:
    for event in pygame.event.get():                                    # 退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for position in snakeSegments:                                      # for循环变量字符串
        #  矩形对象设置位置    界面，颜色，（x,y,w,h）
        pygame.draw.rect(playSurface, whiteColor, 
                        Rect(position[0], position[1],20,20))

    x = random.randint(0,32-1)*20                                       # 随机红色方块的坐标
    y = random.randint(0,24-1)*20
    pygame.draw.rect(playSurface, redColor, (x,y,20,20))                # 画新的红色方块 
    pygame.draw.rect(playSurface, blackColor, (old_x, old_y,20,20))     # 将上次的红色方块变成黑色
    pygame.draw.rect(playSurface, whiteColor, (old_x, old_y,20,20),1)   # 还原小方格的白色边框

    old_x = x                                                           # 记录这次小方格的坐标，以便下次使用
    old_y = y

    pygame.display.update()                                             # 刷新
    fpsClock.tick(1)                                                    # 控制帧数
