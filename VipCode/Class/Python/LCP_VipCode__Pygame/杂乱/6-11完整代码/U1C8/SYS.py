# 4、碰到边缘，改变矩形的移动方向

import pygame,sys,random
from pygame.locals import*

pygame.init()
screen=pygame.display.set_mode([640,480])
class draw():
    def __init__(self,img_file):
        self.x=random.randint(0,5)
        self.y=random.randint(0,5)
        self.img=pygame.image.load(img_file)
        self.img_rect=self.img.get_rect()

    def move(self):
        self.img_rect.move_ip(self.x,self.y)
        if self.img_rect.right >screen.get_width() or self.img_rect.left<0:
            self.x=-self.x
        if self.img_rect.bottom>screen.get_height() or self.img_rect.top<0:
            self.y=-self.y
        screen.blit(self.img,self.img_rect)

img_list=["money1.png","money2.png","money3.png","money4.png","money5.png","money6.png","money7.png","mayun.png"]
img=[]
for x in range(10):
    img_file=random.choice(img_list)
    pic=draw(img_file)
    img.append(pic)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    pygame.time.delay(50)
    screen.fill([255,255,255])
    for i in img:
        i.move()
    pygame.display.update()

