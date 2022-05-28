import pygame, sys
from pygame.locals import *

class Snake():
    def __init__(self):
        """初始化方法"""
        pygame.init()
        self.playSurface = pygame.display.set_mode((640, 480))     #    设置界面
        pygame.display.set_caption("贪吃蛇游戏")                   # 设置标题
        self.redColor = pygame.Color(255, 0, 0)                  # 红色 方块
        self.blackColor = pygame.Color(0, 0, 0)                   # 背景颜色
        self.foodPosition = [300, 300]                        #    食物坐标   食物是 20*20 小方块

    def main(self):
        """主程序"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:       # 退出
                    pygame.quit()
                    sys.exit()

            self.playSurface.fill(self.blackColor)                  # 界面刷新

            #  矩形对象设置位置    界面，颜色，（x,y,w,h）
            pygame.draw.rect(self.playSurface, self.redColor, Rect(self.foodPosition[0], self.foodPosition[1], 20, 20))      #  界面添加 食物

            pygame.display.update()               #   刷新



game = Snake()
game.main()

