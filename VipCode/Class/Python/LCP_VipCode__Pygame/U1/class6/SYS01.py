# 利用面向对象的编程实现：
# 创建一个窗口，窗口宽、高分别为850，480，
# 背景颜色为(135,206,235),窗口中有6个🏀，
# 篮球可以随机在随机位置(x在10-600之间，y在0-400之间)开始，
# 从左到右不间断地移动，点击关闭即可关闭窗口。
import pygame,sys,random
from pygame.locals import *
pygame.init()     # 初始化模块
class draw():
    def __init__(self,img_file):
        self.x=random.randint(10,600)
        self.y=random.randint(0,400)
        self.image=pygame.image.load(img_file)
    def move(self):
        self.x+=1
        if self.x > 800:
            self.x = 0
        screen.blit(self.image,[self.x,self.y])
screen = pygame.display.set_mode((850, 480))    # 窗口大小
w=[]
for i in range(6):
    a = draw(r"D:\Code\P2_CLASS\Python\LCP_VipCode__Pygame\image\篮球图.png")
    w.append(a)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.fill([135,206,235])
    for i in w:
        i.move()
    pygame.time.delay(10)
    pygame.display.flip()
