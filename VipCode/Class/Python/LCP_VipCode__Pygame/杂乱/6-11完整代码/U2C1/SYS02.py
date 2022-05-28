"""
1.各种属性的配置
2.界面创建
3.列表嵌套

== 最终效果：蛇和食物静态显示

"""
import pygame,sys
from pygame.locals import *

pygame.init()                                      # 初始化
playSurface = pygame.display.set_mode((640,480))   # 设置游戏界面
pygame.display.set_caption("贪吃蛇游戏")            # 设置窗口标题
redColor = pygame.Color(255,0,0)                   # 红颜色
whiteColor = pygame.Color(255,255,255)             # 白颜色
snakeSegments = [[100,100],[80,100],[60,100]]      # 蛇身体坐标--列表嵌套
foodPosition = [300,300]                           # 食物坐标

while True:
    for event in pygame.event.get():               # 退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    for position in snakeSegments:                 # for循环变量列表
        pygame.draw.rect(playSurface, whiteColor, Rect(position[0], position[1],20,20))
        """ 矩形对象设置位置(界面，颜色，Rect(x,y,w,h)) """
                                                   # 界面添加 食物
    pygame.draw.rect(playSurface, redColor, Rect(foodPosition[0], foodPosition[1],20,20))      

    pygame.display.update()                        # 刷新

