import pygame,sys
from pygame.locals import*

pygame.init()

# 设置窗口尺寸
screen = pygame.display.set_mode([600, 400])

# 设置背景颜色
screen.fill([255, 206, 205])

# 设置窗口标题
pygame.display.set_caption("游戏小窗口")
pygame.display.flip()

while True: 
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    