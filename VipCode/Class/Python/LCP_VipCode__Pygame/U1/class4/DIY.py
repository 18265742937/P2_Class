import pygame,sys,random
from pygame.locals import *
pygame.init()     # 初始化模块
class Money():
    def __init__(self,img_file):
        self.x=random.randint(-1200,-50)
        self.y=random.randint(0,450)
        self.image=pygame.image.load(img_file)
    def move(self):
        self.x+=1
        if self.x>640:
            self.x=-50
        screen.blit(self.image,[self.x,self.y])
screen = pygame.display.set_mode((640, 480))    # 窗口大小
img_list=["1.png","2.png","3.png","4.png"]
background = pygame.image.load(
    r'D:\Code\P2_CLASS\Python\LCP_VipCode__Pygame\image\background2.jpg')

moneys=[]
for x in range(20):
    img_file=random.choice(img_list)
    money1 = Money("D:/Code/P2_CLASS/Python/LCP_VipCode__Pygame/image/"+ img_file)
    moneys.append(money1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.blit(background,[0,0])
    for i in moneys:
        i.move()
    pygame.display.flip()
