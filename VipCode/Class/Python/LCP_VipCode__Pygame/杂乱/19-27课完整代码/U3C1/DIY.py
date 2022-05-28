import pygame, sys
from pygame.locals import *

class Bird():
    def __init__(self):
        self.images = []
        for i in range(3):
            img = pygame.image.load("./img/bird0_%s.png" % i).convert_alpha()
            rect = img.get_rect()
            rect.x = 50
            self.images.append([rect,img])


class APP():
    def __init__(self):
        # 初始化
        pygame.init()
        self.width, self.height = 700, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('飞翔的小鸟')
        self.bg = pygame.image.load("img/bg_day.png").convert()  # 背景图片导入并缩放为窗口大小
        self.bg = pygame.transform.smoothscale(self.bg, (self.width, self.height))

    def main(self):
        while True:
            self.screen.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            bird.images[0][0].y = 50
            self.screen.blit(bird.images[0][1],bird.images[0][0])
            bird.images[1][0].y = 100
            self.screen.blit(bird.images[1][1],bird.images[1][0])
            bird.images[2][0].y = 150
            self.screen.blit(bird.images[2][1],bird.images[2][0])

            pygame.display.update()

if __name__ == '__main__':
    app = APP()
    bird = Bird()
    app.main()


