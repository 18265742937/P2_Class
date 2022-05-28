# 4、碰到边缘，改变矩形的移动方向

import pygame,sys,random
from pygame.locals import*

pygame.init()

screen=pygame.display.set_mode([640,480])


img = pygame.image.load(
    r"D:\Code\P2_CLASS\Python\LCP_VipCode__Pygame\6-11完整代码\U1C8\mayun.png")
img_rect=img.get_rect()

x=random.randint(0,5)
y=random.randint(0,5)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    pygame.time.delay(50)
    screen.fill([255,255,255])
    img_rect.move_ip(x,y)
    if img_rect.right >screen.get_width() or img_rect.left<0:
        x=-x
    if img_rect.bottom>screen.get_height() or img_rect.top<0:
        y=-y
    screen.blit(img,img_rect)
    pygame.display.update()

