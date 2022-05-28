# --------------------------
# 管道类的定义
# 调用显示管道
#  管道移动
import pygame, sys
from pygame.locals import *

class Bird():
    def __init__(self):
        self.images = []
        for i in range(3):
            img = pygame.image.load("./img/bird0_%s.png" % i).convert_alpha()
            self.rect = img.get_rect()
            self.images.append(img)
        self.frame = 0  # 初始帧数
        self.rect.x = 50
        self.rect.y = 10
        self.distance = 0

    def update(self):
        self.distance += 0.5
        self.rect.y += self.distance

        self.frame += 1
        if self.frame > 2:
            self.frame = 0
        self.image = self.images[self.frame]


class Pipe():  # =======
    def __init__(self, image, top):       # ------------------------
        self.image = image                 # ----------------------
        self.rect = self.image.get_rect()         # ---------------------
        self.rect.x = app.width/2             # ----------------
        self.rect.y = top              # ---------------------


class APP():
    def __init__(self):
        # 初始化
        pygame.init()
        self.width, self.height = 700, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('飞翔的小鸟')
        self.bg = pygame.image.load("img/bg_day.png").convert()  # 背景图片导入并缩放为窗口大小
        self.bg = pygame.transform.smoothscale(self.bg, (self.width, self.height))
        self.FPSclock = pygame.time.Clock()
        self.pipe_down_image = pygame.image.load("img/pipe_down.png").convert_alpha()  #------------- 口冲下的管道
        self.pipe_up_image = pygame.image.load("img/pipe_up.png").convert_alpha()  # -------------口冲上的管道


    def main(self):

        while True:
            self.screen.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN and event.key == K_SPACE:
                    bird.distance = -8

            bird.update()
            self.screen.blit(bird.image, bird.rect)
            pygame.display.update()
            self.FPSclock.tick(60)


if __name__ == '__main__':
    app = APP()
    bird = Bird()
    app.main()


