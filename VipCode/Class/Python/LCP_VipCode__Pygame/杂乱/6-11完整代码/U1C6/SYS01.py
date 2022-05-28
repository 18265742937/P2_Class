import pygame,sys
from pygame.locals import*

pygame.init()

screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.rect(screen,[242,169,3],[100,100,300,200],3)
my_polygon=[(100,50),(50,90),(70,150),(130,150),(150,90)]
pygame.draw.polygon(screen,[248,252,9],my_polygon,3)
# pygame.draw.line(screen,[248,52,100],[50,200],[500,400],3)
# my_line=([50,200],[500,400],[300,200],[400,100])
# pygame.draw.lines(screen,[48,152,200],True,my_line,3)
# pygame.draw.circle(screen,[130,20,153],[200,100],100,5)
# pygame.draw.ellipse(screen,[150,0,0],[100,100,200,300],3)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
