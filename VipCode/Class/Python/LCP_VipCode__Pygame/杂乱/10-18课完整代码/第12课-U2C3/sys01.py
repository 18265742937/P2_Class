import pygame, sys, time, random
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
        self.changeDirection = self.direction                    # 记录改变的方向



    def keyPressEvent(self,event):
        """键盘事件"""
        if event.key == K_RIGHT or event.key == K_d:        # 小键盘 或者键盘上下左右键进行操作移动
            self.changeDirection = 'right'
        if event.key == K_LEFT or event.key == K_a:
            self.changeDirection = 'left'
        if event.key == K_UP or event.key == K_w:
            self.changeDirection = 'up'
        if event.key == K_DOWN or event.key == K_s:
            self.changeDirection = 'down'


    def move(self):
        """确定键盘 移动事件"""
        if self.changeDirection == 'right' and self.direction != 'left':      #   移动   防止 上下调转方向   左右调转方向
            self.direction = self.changeDirection
        if self.changeDirection == 'left' and self.direction != 'right':
            self.direction = self.changeDirection
        if self.changeDirection == 'up' and self.direction != 'down':
            self.direction = self.changeDirection
        if self.changeDirection == 'down' and self.direction != 'up':
            self.direction = self.changeDirection
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
                if event.type == KEYDOWN:
                    self.keyPressEvent(event)     #键盘事件
            self.move()    #确定方向 移动

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