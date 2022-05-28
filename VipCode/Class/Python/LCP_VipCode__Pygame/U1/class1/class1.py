# 导入工具
import pygame,sys
from pygame.locals import *

# 初始化所有导入的pg模块
pygame.init()
# 
screen = pygame.display.set_mode([640, 480])
# 游戏循环
while True:
    for event in pygame.event.get():
        #print("运行了")
        if event.type == QUIT:
            # 窗口持续运行
            sys.exit()
