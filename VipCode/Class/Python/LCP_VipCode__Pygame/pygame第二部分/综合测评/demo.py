import pygame, sys
from pygame.locals import *
class App():
    def __init__(self):
        """初始化方法"""
        pygame.init()
        self.playSurface = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Vipcode")

    def main(self):
        """主程序"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

if __name__ == '__main__':
    game = App()
    game.main()









