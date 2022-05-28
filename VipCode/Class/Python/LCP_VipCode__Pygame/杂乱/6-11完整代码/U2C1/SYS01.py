"""
1.各种属性的配置
2.界面创建

== 最终效果：食物静态显示

"""
import pygame,sys
from pygame.locals import *

pygame.init()

playSurface = pygame.display.set_mode((640,480))     # 设置界面
pygame.display.set_caption("贪吃蛇游戏")              # 设置标题
redColor = pygame.Color(255,0,0)                     # 颜色红
foodPosition = [300,300]                             # 食物坐标--食物是 20*20 小方块

while True:
    for event in pygame.event.get():                 # 退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                                                     # 界面添加 食物
    pygame.draw.rect(playSurface, redColor, Rect(foodPosition[0], foodPosition[1],20,20))      

    pygame.display.update()                          # 刷新

