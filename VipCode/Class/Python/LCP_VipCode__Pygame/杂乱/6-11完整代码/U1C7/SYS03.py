import pygame,sys,random
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,480))

class draw():
    def __init__(self):
        self.x=0
        self.y=0
        pygame.draw.rect(screen,[76,145,255],(self.x,self.y,100,100))
        self.speed_x=1
        self.speed_y=1

    def move(self):
        self.x+=self.speed_x
        self.y+=self.speed_y
        if self.x<0 or self.x>540:
            self.speed_x=-self.speed_x
        if self.y<0 or self.y>380:
            self.speed_y=-self.speed_y
        pygame.draw.rect(screen,[76,145,255],(self.x,self.y,100,100))


triangle=draw()
while True:
    for even in pygame.event.get():
        if even.type==QUIT:
            sys.exit()
    screen.fill((255,255,255))
    triangle.move()
    pygame.display.update()
    pygame.time.delay(5)