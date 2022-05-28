import pygame,sys,random
from pygame.locals import *

pygame.init()     # 初始化模块
class Font_Write():
    def __init__(self,font_text):
        self.x=random.randint(0,854)
        self.y=random.randint(-480,0)
        self.font=font.render(font_text,True,[239,255,0])
    def move(self):
        self.y+=1
        if self.y>480:
            self.y=-50
        screen.blit(self.font,[self.x,self.y])


screen = pygame.display.set_mode((854, 480))    # 窗口大小
text=["##","$$","@@"]
background = pygame.image.load(
    r"D:\Code\P2_CLASS\Python\LCP_VipCode__Pygame\image\background.jpg")
font=pygame.font.SysFont("华文宋体",30)

w=[]
for i in range(50):
    font_text=random.choice(text)
    a=Font_Write(font_text)
    w.append(a)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.blit(background,[0,0])
    for i in w:
        i.move()
    pygame.display.flip()
