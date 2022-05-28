import pygame, sys, random
from pygame.locals import *

class Plan(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("飞机.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = -200,random.randint(0, 200)

    def update(self):
        self.rect.move_ip(1, 0)
        if self.rect.x >= 1400:
            self.rect.x, self.rect.y = -300, random.randint(0, 200)


#      ---继承精灵
class Missile():
    def __init__(self):
        # ---重写后调用父类方法 

        #                              加载图片---实现透明转换

        #                  将image对象转化为mask对象

        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = random.randint(0,1000),600

    def update(self):
        self.rect.move_ip(3, -3)
        if self.rect.bottom <= 0 or self.rect.x >= 1200:
            self.rect.x, self.rect.y = random.randint(0, 1000), 600

class APP():
    def __init__(self):
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 600))
        self.plane = Plan()
        self.missile = Missile()
        #    创建精灵组

        #    添加飞机和导弹对象到精灵组中



    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            self.screen.fill([255, 255, 255])
            #   调用精灵组中所有精灵的update方法


            #   将精灵组中所有精灵绘制到屏幕上


            #                  检测精灵碰撞

            # 碰撞检测


            pygame.display.update()
            self.fpsClock.tick(120)  # 控制帧数    速度


if __name__ == '__main__':
    app = APP()
    app.main()
