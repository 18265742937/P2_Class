import pygame,sys,random
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,480))

class draw():
    def __init__(self):
        self.x=30
        self.y=30
        pygame.draw.rect(screen,[76,145,255],(self.x,self.y,100,100))
        pygame.draw.circle(screen,[255,0,0],[self.x,self.y],30)
        pygame.draw.circle(screen,[255,0,0],[self.x+100,self.y],30)
        pygame.draw.ellipse(screen,[150,0,0],[self.x,self.y,200,300],3)

        self.speed_x=1
        self.speed_y=1

    def move(self):
        self.x+=self.speed_x
        self.y+=self.speed_y
        if self.x<30 or self.x>510:
            self.speed_x=-self.speed_x
        if self.y<30 or self.y>380:
            self.speed_y=-self.speed_y
        pygame.draw.rect(screen,[76,145,255],(self.x,self.y,100,100))
        pygame.draw.circle(screen,[255,0,0],[self.x,self.y],30)
        pygame.draw.circle(screen,[255,0,0],[self.x+100,self.y],30)
        pygame.draw.ellipse(screen,[255,255,255],[self.x+25,self.y+50,50,20])


rectangle=draw()
while True:
    for even in pygame.event.get():
        if even.type==QUIT:
            sys.exit()
    screen.fill((255,255,255))
    rectangle.move()
    pygame.display.update()
    pygame.time.delay(10)