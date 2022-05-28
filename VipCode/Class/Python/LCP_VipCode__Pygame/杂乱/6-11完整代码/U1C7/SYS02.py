import pygame,sys,random
from pygame.locals import *

pygame.init()

class draw():
    def __init__(self):
        self.x=random.randint(50,590)
        self.y=random.randint(50,430)
        pygame.draw.circle(screen,[255,0,0],[self.x,self.y],50)
        self.speed_x=1
        self.speed_y=1

    def move(self):
        self.x+=self.speed_x
        self.y+=self.speed_y
        if self.x<50 or self.x>590:
            self.speed_x=-self.speed_x
        if self.y<50 or self.y>430:
            self.speed_y=-self.speed_y
        pygame.draw.circle(screen,[255,0,0],[self.x,self.y],50)


screen=pygame.display.set_mode((640,480))

circle=draw()
while True:
    for even in pygame.event.get():
        if even.type==QUIT:
            sys.exit()
    screen.fill([255,255,255])
    circle.move()
    pygame.display.update()