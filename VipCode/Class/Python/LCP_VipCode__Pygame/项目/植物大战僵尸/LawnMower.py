import pygame


class CarImage():
    def __init__(self):
        self.car_image = pygame.image.load("photo/others/LawnMower.gif").convert_alpha()


class Car(pygame.sprite.Sprite):
    def __init__(self,L,image):
        pygame.sprite.Sprite.__init__(self)

        self.image = image.car_image
        self.rect = self.image.get_rect()
        self.rect.left = - self.rect.width
        self.L = L
        self.active = False
        self.speed = 4
        self.mask = pygame.mask.from_surface(self.image)

    def move1(self):
        if self.rect.right < self.L:
            self.rect.left += self.speed
        else:
            self.rect.right = self.L + 4

    def move2(self):
        self.rect.left += self.speed