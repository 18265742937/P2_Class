"""
1.各种属性的配置
2.界面创建
3.随机三原色
4.帧速率

== 最终效果：矩形方块闪烁

"""

import pygame,sys
from random import randint
from pygame.locals import *
pygame.init()

playSurface = pygame.display.set_mode((640,480))           #    设置界面
FPSClock = pygame.time.Clock()

while True:
    for event in pygame.event.get():             # 退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    randomColor = pygame.Color(randint(0,255),randint(0,255),randint(0,255))    
    pygame.draw.rect(playSurface, randomColor, Rect(20,20,600,440),)
    FPSClock.tick(20)       # 控制帧数
    pygame.display.update()    #   刷新