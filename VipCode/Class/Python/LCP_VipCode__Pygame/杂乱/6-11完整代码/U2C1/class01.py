import pygame,sys
from pygame.locals import *

pygame.init()                                      # 初始化
playSurface = pygame.display.set_mode((640,480))   # 设置游戏界面
pygame.display.set_caption("贪吃蛇游戏")            # 设置窗口标题
redColor = pygame.Color(255,0,0)                   # 红颜色
blackColor = pygame.Color(0,0,0)                   # 黑颜色
whiteColor = pygame.Color(255,255,255)             # 白颜色
snakeSegments = [[100,100],[80,100],[60,100]]      # 蛇身体坐标--列表嵌套
foodPosition = [300,300]                           # 食物坐标
fpsClock = pygame.time.Clock()                     # 创建时钟对象     

while True:
    for event in pygame.event.get():               
        if event.type == QUIT:
            pygame.quit()
            sys.exit()                             # 退出

    for position in snakeSegments:                 # 循环遍历列表
        pygame.draw.rect(playSurface, whiteColor, 
        Rect(position[0], position[1],20,20))
                                                   
    pygame.draw.rect(playSurface, redColor,        # 界面添加食物
    Rect(foodPosition[0], foodPosition[1],20,20))    

    fpsClock.tick(10)                              # 控制帧数
    pygame.display.update()                        # 刷新
    
