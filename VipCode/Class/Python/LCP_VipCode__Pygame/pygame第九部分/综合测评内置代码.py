import pygame
import sys
from pygame.locals import *
import time 

pygame.init()
size = width, height = 600,400
speed = [1,2]
bg = (255,255,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("弹弹弹，小游戏！")
gamemaster = pygame.image.load("dude2.png")
position = gamemaster.get_rect()

# 反转：第一个布尔值：左右翻转 第二个布尔值：上下翻转
l_head = pygame.transform.flip(gamemaster,True,False)
r_head = pygame.transform.flip(gamemaster,True,False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
        if event.type == KEYDOWN:
            
            """
            设置 上下左右 按键的效果
            上：偏移量为[1,-2]
            下：偏移量为[-1,2]
            左：反转，偏移量为[-2,1]
            右：反转，偏移量为[2,-1]
            """
            #=============start ================


            #=============start ================

    position = position.move(speed)
 
    """
    设置碰到边界后，
    设置gamemaster,左右翻转 上下不翻转
    """
    # ============ start ============
  

    # ============= end ============= 

    screen.fill(bg)

    screen.blit(gamemaster,position)
    pygame.display.flip()
    pygame.time.delay(10)