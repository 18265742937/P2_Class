import pygame, sys, time, random
from pygame.locals import *

class Snake():
    def __init__(self):
        """初始化方法"""
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.playSurface = pygame.display.set_mode((400, 300))     #    设置界面
        pygame.display.set_caption("贪吃蛇游戏")                   # 设置标题


    def addButton(self):
        self.mouse = pygame.mouse.get_pos()
        print(self.mouse)

    def main(self):
        """主程序"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:       # 退出
                    pygame.quit()
                    sys.exit()

            self.addButton()
            pygame.display.update()               #   刷新
            self.fpsClock.tick(10)             # 控制帧数    速度

if __name__ == '__main__':
    game = Snake()
    game.main()