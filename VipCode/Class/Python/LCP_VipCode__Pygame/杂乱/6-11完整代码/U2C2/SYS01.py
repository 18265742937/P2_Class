"""
1.各种属性的配置
2.界面创建
3.列表嵌套
4.帧速率
5.面向对象的思想编程
6.程序启动入口
"""

import pygame, sys
from pygame.locals import *

class Snack():                                                     # 定义类
    def __init__(self):                                            # 构造函数
        pygame.init()                                              # 初始化
        self.playSurface = pygame.display.set_mode((640, 480))     # 设置游戏界面
        pygame.display.set_caption("贪吃蛇游戏")                    # 设置窗口标题
        self.redColor = pygame.Color(255, 0, 0)                    # 红颜色
        self.blackColor = pygame.Color(0, 0, 0)                    # 黑颜色
        self.whiteColor = pygame.Color(255, 255, 255)              # 白颜色
        self.snakeSegments = [[100, 100], [80, 100], [60, 100]]    # 蛇身体坐标--列表嵌套
        self.foodPosition = [300, 300]                             # 食物坐标
        self.fpsClock = pygame.time.Clock()                        # 创建时钟对象

    def main(self):
        """主程序"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:      
                    pygame.quit()
                    sys.exit()                                     # 退出

            for position in self.snakeSegments:                    # 循环遍历列表
                pygame.draw.rect(self.playSurface, self.whiteColor, 
                Rect(position[0], position[1], 20, 20))
                                                                   
            pygame.draw.rect(self.playSurface, self.redColor,      # 界面添加食物
            Rect(self.foodPosition[0], self.foodPosition[1], 20, 20))
            self.fpsClock.tick(40)                                 # 控制帧数
            pygame.display.update()                                # 刷新    
            
if __name__ == '__main__':                                         # 程序启动入口
    game = Snack()                                                 # 类的实例化--创建类对象game
    game.main()                                                    # 类对象调用类方法

