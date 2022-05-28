"""
闪烁的 "田" 字
"""

import pygame,sys
from random import randint
from pygame.locals import *
pygame.init()

playSurface = pygame.display.set_mode((400,400))           # 设置界面
positionS = [[100,100],[200,100],[100,200],[200,200]]      # 坐标--列表嵌套
FPSClock = pygame.time.Clock()                             # 创建时钟对象 (可以控制游戏循环频率)

while True:
    for event in pygame.event.get():                       # 退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                                                           # 随机颜色--三原色(RGB)
    randomColor = pygame.Color(randint(0,255),randint(0,255),randint(0,255))

    for position in positionS:                             # 循环遍历列表
        pygame.draw.rect(playSurface, randomColor, Rect(position[0],position[1],100,100),20)

    a = FPSClock.tick(20)                                  # 控制帧数
    pygame.display.update()                                # 刷新