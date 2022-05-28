import pygame
from pygame import locals
import random, time, math, sys

class PlayerSprite(pygame.sprite.Sprite): 
    def __init__(self,screen, width, height,color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 500/2 - 61
        self.rect.y = 600
        self.speed = 1
        self.screen = screen

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[locals.K_d] or keys[locals.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > 378:
                self.rect.x = 378
        if keys[locals.K_a] or keys[locals.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0

    def update(self):
        self.move()      

class SqureSprite(pygame.sprite.Sprite): 
    def __init__(self,screen, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.screen = screen
        #================ start ==================


        #================ end ==================
def main():
    pygame.init()
    FPSclock = pygame.time.Clock()
    screen = pygame.display.set_mode((500,700))

    player = PlayerSprite(screen, 100, 10,(225,225,225))    
    group_player = pygame.sprite.Group()
    group_player.add(player)

    squre = SqureSprite(screen, 10, 10,(0,225,225))    
    group_squre = pygame.sprite.Group()
    group_squre.add(squre)

    while True:
        FPSclock.tick(200)
        screen.fill((0,0,0))

        group_player.update()
        group_player.draw(screen)

        group_squre.update()
        group_squre.draw(screen)
        
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()

        #================= 碰撞检测 ===============

        #==================== end ==================        

        pygame.display.update()

if __name__ == "__main__":        
    main()

