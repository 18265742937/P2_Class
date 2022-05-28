# 导入pygame库，这一步能让你使用库里提供的功能
import pygame
from pygame.locals import *
import math   # 因为需要计算旋转的角度

class Rabbit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/dude.png')
        self.rect = self.image.get_rect()
        self.x = 100
        self.y = 100
        self.speed = 1

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_d] or keys[K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > 600:
                self.rect.x = 600
        if keys[K_a] or keys[K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[K_w] or keys[K_UP]:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0
        if keys[K_s] or keys[K_DOWN]:
            self.rect.y += self.speed
            if self.rect.y > 450:
                self.rect.y = 450

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.move()

def updateBackground():
    screen.fill((0, 0, 0))
    for x in range(SCREEN_SIZE[0]//grass_img.get_width()+1):
        for y in range(SCREEN_SIZE[1]//grass_img.get_height()+1):
            screen.blit(grass_img, (x*100, y*100))

def getEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

if __name__ == "__main__":
    pygame.init()
    SCREEN_SIZE = 640, 480
    screen = pygame.display.set_mode(SCREEN_SIZE)
    FPSclock = pygame.time.Clock()
    grass_img = pygame.image.load("resources/images/grass.png")
    group_rabbit = pygame.sprite.Group()
    rabbit = Rabbit()
    group_rabbit.add(rabbit)

    while True:
        FPSclock.tick(240)
        updateBackground()   
        position = pygame.mouse.get_pos()
        getEvent()
        group_rabbit.update()
        pygame.display.update()        