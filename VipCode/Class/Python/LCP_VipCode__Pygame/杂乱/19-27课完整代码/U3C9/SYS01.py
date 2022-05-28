
import pygame, sys, random
from pygame.locals import *

class Plan(pygame.sprite.Sprite):  #  飞机
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


class Missile(pygame.sprite.Sprite):  # 导弹
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("导弹.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
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
        self.group = pygame.sprite.Group()
        self.group.add(self.plane,self.missile)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            self.screen.fill([255, 255, 255])
            self.group.update()
            self.group.draw(self.screen)
            slist = pygame.sprite.spritecollide(self.plane,
                self.group, False,pygame.sprite.collide_mask)
            if len(slist)==2: 
                app = APP()
                app.main()
            pygame.display.update()
            self.fpsClock.tick(120)  

if __name__ == '__main__':
    app = APP()
    app.main()



