import pygame
import sys
from pygame.locals import*
 
pygame.init()
 
GRAY = (150,150,150)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE =(0,0,255)
 
size = width,height = 640,480
screen = pygame.display.set_mode(size)
 
position = size[0]//2,size[1]//2
moving = False
 
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        
        if event.type == QUIT:
            exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
                s = 0
 
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                moving = False
 
    #得到鼠标位置，圆形移动
    if moving:
        # ======== 获取鼠标位置 ========
 
    screen.fill(GRAY)
 
    # 绘制圆形 
    # pygame.draw.circle(screen, 颜色, 圆心位置, 画笔宽度)
    
    
    #更新图片
    pygame.display.flip()
    #设置帧率
    clock.tick(120)