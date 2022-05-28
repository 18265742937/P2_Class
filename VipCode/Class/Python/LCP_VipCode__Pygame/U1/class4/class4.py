import pygame,sys,random
from pygame.locals import *
pygame.init()     # 初始化模块
class Money():
    def __init__(self,img_file):
        self.x=random.randint(0,554)
        self.y=random.randint(-500,0)
        self.image=pygame.image.load(img_file)
    def move(self):
        self.y+=1
        if self.y>480:
            self.y =- 50
        screen.blit(self.image,[self.x,self.y])
screen = pygame.display.set_mode((854, 480))    # 窗口大小
img_list=["money1.png","money2.png","money3.png","money4.png","money5.png"]
surprise=["mayun.png","treasure.png"]
background = pygame.image.load(
    r"D:\Code\P2_CLASS\Python\LCP_VipCode__Pygame\image\background.jpg")
moneys=[]
for x in range(50):
    if random.random()>=0.99:
        img_file=random.choice(surprise)
    else:
        img_file=random.choice(img_list)
    money1 = Money("D:/Code/P2_CLASS/Python/LCP_VipCode__Pygame/image/"+img_file)
    moneys.append(money1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.blit(background,[0,0])
    for i in moneys:
        i.move()
    pygame.display.flip()
