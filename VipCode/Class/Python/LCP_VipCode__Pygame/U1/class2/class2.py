from os import path
import pygame,sys
from pygame.locals import*
from random import randint
pygame.init()
screen=pygame.display.set_mode([650,365])
path = "VipCode\Class\Python\LCP_VipCode__Pygame"

pygame.display.set_caption("游戏小窗口")
bg = pygame.image.load(path+r"\image\background.jpg")
img1 = pygame.image.load(path+r'\image\mayun.png')
# VipCode\Class\Python\LCP_VipCode__Pygame\image\1.png
while True:  
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    screen.blit(bg,[0,0])
    screen.blit(img1,[randint(0,500),randint(0,200)])
    pygame.display.flip()
    pygame.time.delay(100)
    
