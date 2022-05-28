import pygame
from random import *


class ProductsImages():
    def __init__(self):
        # 阳光图片
        self.sun_images = []
        self.sun_images.extend([\
            pygame.image.load("photo/Plants/SunFlower/Sun_1.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_2.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_3.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_4.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_5.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_6.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_7.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_8.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_9.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_10.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_11.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_12.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_13.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_14.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_15.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_16.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/Sun_17.png").convert_alpha() \
            ])

        # 弹丸图片
        self.bullet_image = pygame.image.load("photo/Plants/Peashooter/Bullet.png").convert_alpha()
        self.firebullet_images = []
        self.firebullet_images.extend([\
            pygame.image.load("photo/Plants/Torchwood/fire_bullet1.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Torchwood/fire_bullet2.png").convert_alpha() \
            ])


class Sun(pygame.sprite.Sprite):
    def __init__(self,T,X,images):
        pygame.sprite.Sprite.__init__(self)

        self.images = images.sun_images
        self.top, self.x = T, X
        self.rect1 = self.images[0].get_rect()
        self.rect2 = self.images[0].get_rect()
        self.rect1.left,self.rect1.top = randint(125,470), 87 - self.rect1.height
        self.rect2.centerx, self.rect2.centery = self.x, self.top + 30
        self.index_image = 0
        self.num_image = 17
        self.speed1 = 2
        self.speed2 = 1
        self.speed3 = 10
        self.position = randint(335, 480)
        self.count_time = 0
        self.is_supply = True
        self.gather = False
        self.get_position = False

    def move1(self):
        if self.rect1.top < self.position:
            self.rect1.top += self.speed1
        else:
            self.rect1.top = self.position

    def move2(self):
        if self.rect2.centery > self.top - 10:
            self.rect2.centery -= self.speed2
        else:
            self.rect2.centery = self.top - 10

    def move3(self):
        if self.is_supply:
            if self.rect1.centerx > 79:
                self.rect1.centerx -= self.speed3
            else:
                self.rect1.centerx = 79
            if self.rect1.centery > 36:
                self.rect1.centery -= self.speed3
            else:
                self.rect1.centery = 36
            if self.rect1.centerx == 79 and self.rect1.centery == 36:
                self.get_position = True
        else:
            if self.rect2.centerx > 79:
                self.rect2.centerx -= self.speed3
            else:
                self.rect2.centerx = 79
            if self.rect2.centery > 36:
                self.rect2.centery -= self.speed3
            else:
                self.rect2.centery = 36
            if self.rect2.centerx == 79 and self.rect2.centery == 36:
                self.get_position = True


class Bullet(pygame.sprite.Sprite):
    def __init__(self,bg_size,positon,images):
        pygame.sprite.Sprite.__init__(self)

        self.bullet_image = images.bullet_image
        self.firebullet_images = images.firebullet_images
        self.rect = self.bullet_image.get_rect()
        self.index_image = 0
        self.num_image = 2
        self.left,self.top = positon[0] + 20,positon[1] - 28
        self.rect.left,self.rect.top = self.left,self.top
        self.width = bg_size[0]
        self.shoot = False
        self.speed = 5
        self.is_bullet = True
        self.bullet_mask = pygame.mask.from_surface(self.bullet_image)
        self.firebullet_mask = pygame.mask.from_surface(self.firebullet_images[0])
        self.mask = self.bullet_mask

    def move(self):
        self.rect.left += self.speed
        if self.rect.left >= self.width:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = self.left,self.top
        self.is_bullet = True
        self.shoot = False