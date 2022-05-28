import pygame, sys
from pygame.locals import *

class Bird():
    def __init__(self):
        self.images = []
        for i in range(3):
            img = pygame.image.load("./img/bird0_%s.png" % i)
            self.rect = img.get_rect()
            self.images.append(img)
        self.rect.x = 50
        self.rect.y = 10

class APP():
    def __init__(self):
        # 初始化
        pygame.init()
        self.width, self.height = 700, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('飞翔的小鸟')
        self.bg = pygame.image.load("img/bg_day.png")
        self.bg = pygame.transform.smoothscale(self.bg, (self.width, self.height))

    def main(self):
        while True:
            self.screen.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(bird.images[0], bird.rect)
            pygame.display.update()

if __name__ == '__main__':
    app = APP()
    bird = Bird()
    app.main()


