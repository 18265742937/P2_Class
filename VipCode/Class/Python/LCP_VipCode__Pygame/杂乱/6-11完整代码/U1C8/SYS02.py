
import pygame,sys,random
from pygame.locals import*

pygame.init()

screen=pygame.display.set_mode([640,480])

screen.fill([255,255,255])
img=pygame.image.load("mayun.png")
img_rect=img.get_rect()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    pygame.time.delay(100)
    screen.fill([255,255,255])
    img_rect=img_rect.move(1,1)
    # img_rect.move_ip(1,1)
    screen.blit(img,img_rect)
    pygame.display.update()

