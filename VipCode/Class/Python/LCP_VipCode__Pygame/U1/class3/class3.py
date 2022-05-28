import pygame,sys
from pygame.locals import *
pygame.init()     # 初始化模块
path = "VipCode\Class\Python\LCP_VipCode__Pygame"
class Money():
    def __init__(self):
        self.x=10
        self.y=10
        self.image=img
    def move(self):
        # 下方两个参数同时使用就是斜向移动
        self.y+=1  # 纵向移动
        # self.x+=1  # 横向移动
        screen.blit(self.image,[self.x,self.y])

# pygame.init()
screen=pygame.display.set_mode([650,365])
pygame.display.set_caption("游戏小窗口")
background = pygame.image.load(path+r'\image\background.jpg')
img = pygame.image.load(path+r'\image\mayun.png')
money1=Money()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.blit(background,[0,0])
    money1.move()
    pygame.time.delay(100)
    pygame.display.flip()
