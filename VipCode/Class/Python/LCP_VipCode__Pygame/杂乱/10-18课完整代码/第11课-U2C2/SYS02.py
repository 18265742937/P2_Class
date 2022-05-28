import pygame, sys
from pygame.locals import *

class Snake():
    def __init__(self):
        """初始化方法"""
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.playSurface = pygame.display.set_mode((640, 480))     #    设置界面
        pygame.display.set_caption("贪吃蛇游戏")                   # 设置标题
        self.redColor = pygame.Color(255, 0, 0)                  # 红色 方块
        self.blackColor = pygame.Color(0, 0, 0)                   # 背景颜色
        self.whiteColor = pygame.Color(255, 255, 255)               # 蛇本体颜色
        self.snakePosition = [100, 100]                               #   蛇头坐标
        self.snakeSegments = [[100, 100], [80, 100], [60, 100]]                  #   蛇身体
        self.foodPosition = [300, 300]                        #    食物坐标   食物是 20*20 小方块
        self.direction = 'right'                           # 默认方向

    def move(self):
        """移动 """
        if self.direction == 'right':                          #        控制蛇头移动
            self.snakePosition[0] += 20                    #  每次20
        if self.direction == 'left':
            self.snakePosition[0] -= 20
        if self.direction == 'up':
            self.snakePosition[1] -= 20
        if self.direction == 'down':
            self.snakePosition[1] += 20

    def main(self):
        """主程序"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:       # 退出
                    pygame.quit()
                    sys.exit()

            self.move()    #移动

            self.snakeSegments.insert(0, list(self.snakePosition))    #   蛇身体  在前边插入坐标  蛇头坐标为了前进
            self.snakeSegments.pop()      # 蛇身体删除最后1个          没吃到往前走

            self.playSurface.fill(self.blackColor)                  # 界面刷新

            for position in self.snakeSegments:            #  从身体列表里找出身体的小坐标
                #  矩形对象设置位置    界面，颜色，（x,y,w,h）
                pygame.draw.rect(self.playSurface, self.whiteColor, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(self.playSurface, self.redColor, Rect(self.foodPosition[0], self.foodPosition[1], 20, 20))      #  界面添加 食物
            pygame.display.update()               #   刷新
            self.fpsClock.tick(10)             # 控制帧数    速度


if __name__ == '__main__':
    game = Snake()
    game.main()

