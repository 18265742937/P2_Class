import pygame,sys,random
from pygame.locals import *

pygame.init()

class draw():
    
    pass

screen=pygame.display.set_mode((640,480))


while True:
    for even in pygame.event.get():
        if even.type==QUIT:
            sys.exit()

    screen.fill([255,255,255])
    
    pygame.display.update()
    