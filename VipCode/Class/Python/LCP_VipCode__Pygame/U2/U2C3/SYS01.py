
import pygame,sys,random
from pygame.locals import*

pygame.init()

screen=pygame.display.set_mode([640,480])

screen.fill([255,255,255])



while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    pygame.display.update()
