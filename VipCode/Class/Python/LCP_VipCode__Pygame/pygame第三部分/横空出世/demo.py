import pygame, sys
from pygame.locals import *

class APP():
    def __init__(self):
        # 初始化
        pygame.init()
        self.width, self.height = 700, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('飞翔的小鸟')
        self.bg = pygame.image.load("img/bg_day.png")

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.bg, (0, 0))
            pygame.display.update()

if __name__ == '__main__':
    app = APP()
    app.main()


