import pygame,sys
from pygame.locals import*
from random import randint
import os
path = "VipCode\Class\Python\LCP_VipCode__Pygame"

pygame.init()
screen=pygame.display.set_mode([650,365])
pygame.display.set_caption("游戏小窗口")

# 设置窗口的背景图片
bg = pygame.image.load(path+r"\image\background.jpg")
screen.blit(bg,[0,0])
img1 = pygame.image.load(path+r"\image\mayun.png")
# 在随机位置添加图片
screen.blit(img1,[randint(0,500),randint(0,200)])
pygame.display.flip()
while True:  
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    
