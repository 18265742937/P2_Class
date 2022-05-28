
import pygame,sys,random
from pygame.locals import*

pygame.init()

screen=pygame.display.set_mode([640,480])

screen.fill([255,255,255])

img=pygame.image.load("mayun.png")
img_rect=img.get_rect()
screen.blit(img,img_rect)

print(img_rect.top)
print(img_rect.left)
print(img_rect.bottom)
print(img_rect.right)
print(img_rect.width)
print(img_rect.height)
print(img_rect.center)
print(img_rect.size)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    pygame.display.update()
