
import pygame,sys
from pygame.locals import *
pygame.init()
fpsClock=pygame.time.Clock()
playSurface=pygame.display.set_mode((640,480))           #    设置界面
pygame.display.set_caption("贪吃蛇游戏")              # 设置标题
redColor=pygame.Color(255,0,0)                 # 红色 方块
blackColor=pygame.Color(0,0,0)                                    # 背景颜色
whiteColor=pygame.Color(255,255,255)              # 蛇本体颜色
snakePosition=[100,100]                           #   蛇头坐标
snakeSegments=[[100,100],[80,100],[60,100]]               #   蛇身体
foodPosition=[300,300]       

direction='right'                       


while True:
    for event in pygame.event.get():             
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    if direction=='right':                                      
        snakePosition[0]+=20            

    snakeSegments.insert(0,list(snakePosition))
    snakeSegments.pop()
    
    playSurface.fill(blackColor)         
    for position in snakeSegments:      
        pygame.draw.rect(playSurface,whiteColor,Rect(position[0],position[1],20,20))
    pygame.draw.rect(playSurface,redColor,Rect(foodPosition[0],foodPosition[1],20,20))      #  界面添加 食物
    pygame.display.update()    
    fpsClock.tick(10)       


