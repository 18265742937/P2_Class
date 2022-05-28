import pygame
from random import *


class PlantsImages():
    def __init__(self):
        # 向日葵图片
        self.sunflower_card_image = pygame.image.load("photo/Plants/SunFlower/SunFlower_Card.gif").convert_alpha()
        self.sunflower_images = []
        self.sunflower_images.extend([ \
            pygame.image.load("photo/Plants/SunFlower/SunFlower1.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower2.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower3.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower4.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower5.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower6.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower7.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower8.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower9.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower10.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower11.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower12.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower13.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower14.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower15.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower16.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower17.png").convert_alpha(), \
            pygame.image.load("photo/Plants/SunFlower/SunFlower18.png").convert_alpha() \
            ])

        # 豌豆射手图片
        self.peashooter_card_image = pygame.image.load("photo/Plants/Peashooter/Peashooter_Card.gif").convert_alpha()
        self.peashooter_images = []
        self.peashooter_images.extend([ \
            pygame.image.load("photo/Plants/Peashooter/Peashooter1.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter2.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter3.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter4.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter5.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter6.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter7.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter8.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter9.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter10.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter11.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter12.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Peashooter/Peashooter13.png").convert_alpha() \
            ])

        # 坚果图片
        self.wallnut_card_image = pygame.image.load("photo/Plants/WallNut/WallNut_Card.gif").convert_alpha()
        self.wallnut_ok_images = []
        self.wallnut_ok_images.extend([ \
            pygame.image.load("photo/Plants/WallNut/WallNut1.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut2.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut3.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut4.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut5.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut6.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut7.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut8.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut9.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut10.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut11.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut12.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut13.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut14.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut15.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut16.png").convert_alpha() \
            ])
        self.wallnut_c1_images = []
        self.wallnut_c1_images.extend([ \
            pygame.image.load("photo/Plants/WallNut/Wallnut_cracked1_1.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_2.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_3.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_4.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_5.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_6.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_7.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_8.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_9.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_10.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked1_11.png").convert_alpha() \
            ])
        self.wallnut_c2_images = []
        self.wallnut_c2_images.extend([ \
            pygame.image.load("photo/Plants/WallNut/Wallnut_cracked2_1.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_2.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_3.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_4.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_5.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_6.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_7.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_8.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_9.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_10.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_11.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_12.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_13.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_14.png").convert_alpha(), \
            pygame.image.load("photo/Plants/WallNut/WallNut_cracked2_15.png").convert_alpha() \
            ])

        # 火炬图片
        self.torchwood_card_image = pygame.image.load("photo/Plants/Torchwood/Torchwood_Card.gif").convert_alpha()
        self.torchwood_images = []
        self.torchwood_images.extend([ \
            pygame.image.load("photo/Plants/Torchwood/Torchwood1.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Torchwood/Torchwood2.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Torchwood/Torchwood3.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Torchwood/Torchwood4.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Torchwood/Torchwood5.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Torchwood/Torchwood6.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Torchwood/Torchwood7.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Torchwood/Torchwood8.png").convert_alpha(), \
            pygame.image.load("photo/Plants/Torchwood/Torchwood9.png").convert_alpha() \
            ])

        # 铲子图片
        self.shovel_card_image = pygame.image.load("photo/Plants/Shovel/Shovel_Card.png").convert_alpha()
        self.shovel_images = []
        self.shovel_images.extend([pygame.image.load("photo/Plants/Shovel/Shovel.png").convert_alpha()])


class SunFlower(pygame.sprite.Sprite):
    def __init__(self,images):
        pygame.sprite.Sprite.__init__(self)

        self.card_image = images.sunflower_card_image
        self.card_rect = self.card_image.get_rect()
        self.card_rect.left,self.card_rect.top = 125,8
        self.images = images.sunflower_images
        self.rect = self.images[0].get_rect()
        self.shadow_rectx,self.shadow_recty = -10,50
        self.index = 1
        self.index_image = 0
        self.num_image = 18
        self.price = 50
        self.count_time = 0
        self.create_time = randint(12,22)
        self.blood = 3
        self.attacked = False
        self.num_az = 0
        self.mask = pygame.mask.from_surface(self.images[9])


class Peashooter(pygame.sprite.Sprite):
    def __init__(self,images):
        pygame.sprite.Sprite.__init__(self)

        self.card_image = images.peashooter_card_image
        self.card_rect = self.card_image.get_rect()
        self.card_rect.left,self.card_rect.top = 180,8
        self.images = images.peashooter_images
        self.rect = self.images[0].get_rect()
        self.shadow_rectx, self.shadow_recty = -11, 45
        self.index = 2
        self.index_image = 0
        self.num_image = 13
        self.price = 100
        self.blood = 3
        self.attacked = False
        self.num_az = 0
        self.mask = pygame.mask.from_surface(self.images[6])


class WallNut(pygame.sprite.Sprite):
    def __init__(self,images):
        pygame.sprite.Sprite.__init__(self)

        self.card_image = images.wallnut_card_image
        self.card_rect = self.card_image.get_rect()
        self.card_rect.left,self.card_rect.top = 235,8

        self.ok_images = images.wallnut_ok_images
        self.index_ok_image = 0
        self.num_ok_image = 16
        self.ok_mask = pygame.mask.from_surface(self.ok_images[8])

        self.c1_images = images.wallnut_c1_images
        self.index_c1_image = 0
        self.num_c1_image = 11
        self.c1_mask = pygame.mask.from_surface(self.c1_images[5])

        self.c2_images = images.wallnut_c2_images
        self.index_c2_image = 0
        self.num_c2_image = 15
        self.c2_mask = pygame.mask.from_surface(self.c2_images[7])

        self.rect = self.ok_images[0].get_rect()
        self.shadow_rectx,self.shadow_recty = -10,50
        self.index = 3
        self.images = self.ok_images
        self.index_image = self.index_ok_image
        self.num_image = self.num_ok_image
        self.mask = self.ok_mask
        self.price = 50
        self.blood = 40
        self.attack = False
        self.num_az = 0


class Torchwood(pygame.sprite.Sprite):
    def __init__(self,images):
        pygame.sprite.Sprite.__init__(self)

        self.card_image = images.torchwood_card_image
        self.card_rect = self.card_image.get_rect()
        self.card_rect.left,self.card_rect.top = 290,8
        self.images = images.torchwood_images
        self.rect = self.images[0].get_rect()
        self.shadow_rectx, self.shadow_recty = -8, 60
        self.index = 4
        self.index_image = 0
        self.num_image = 9
        self.price = 175
        self.blood = 3
        self.attacked = False
        self.num_az = 0
        self.mask = pygame.mask.from_surface(self.images[4])


class Shovel(pygame.sprite.Sprite):
    def __init__(self,images):
        pygame.sprite.Sprite.__init__(self)

        self.card_image = images.shovel_card_image
        self.card_rect = self.card_image.get_rect()
        self.card_rect.left, self.card_rect.top = 483,1
        self.images = images.shovel_images
        self.index = 5
        self.price = 0
        self.rect = self.images[0].get_rect()