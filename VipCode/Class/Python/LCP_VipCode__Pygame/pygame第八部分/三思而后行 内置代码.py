import pygame
from pygame.locals import *
import math  
import random

class Rabbit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/rabbit.png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.hp = 100
        self.rect.x = 100
        self.rect.y = 100

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

    def update(self, position):
        #======= 角色生命值显示 ===========
        screen.fill((255,255,0), (self.rect.x+10,self.rect.y+70,self.hp/2, 4)) 

        angle = math.atan2(position[1]-self.rect.y + 60, position[0]- self.rect.x)
        playerrot = pygame.transform.rotate(self.image, 360-angle*57.29)
        screen.blit(playerrot, (self.rect.x, self.rect.y))
        self.move()

#============== 敌人类 ========================
class EnemyRabbit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/rabbit.png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.hp = 100
        self.rect.x = random.randint(0,600)
        self.rect.y = random.randint(0,450)

    def update(self):
        screen.fill((0,255,0), (self.rect.x+10,self.rect.y+70,self.hp/2, 4))
        screen.blit(self.image, (self.rect.x, self.rect.y))  

class Arrow(pygame.sprite.Sprite):
    def __init__(self, player, position):
        super().__init__()
        self.image = pygame.image.load('resources/images/bullet.png')
        angle = math.atan2(position[1]-player.rect.y, position[0] - player.rect.x)        
        self.playerrot = pygame.transform.rotate(self.image, 360-angle*57.29)
        self.rect = self.playerrot.get_rect()  
        self.rect.x, self.rect.y = player.rect.x, player.rect.y
        self.speed = 10
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed

    def update(self):
        self.rect.x += self.dx 
        self.rect.y += self.dy
        screen.blit(self.playerrot, (self.rect.x, self.rect.y))
        if self.rect.x < 0 or self.rect.x > 600 or self.rect.y < 0 or self.rect.y > 480:
            self.kill() 

def updateBackground():
    screen.fill((0, 0, 0))
    for x in range(SCREEN_SIZE[0]//grass_img.get_width()+1):
        for y in range(SCREEN_SIZE[1]//grass_img.get_height()+1):
            screen.blit(grass_img, (x*100, y*100))

def getEvent(player, position):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            arrow = Arrow(player, position) 
            group_arrow.add(arrow)

#========= 检测碰撞 =============
def checkCollision():
    collide_player_enemy = pygame.sprite.groupcollide(group_arrow, group_enemy, True, True)

if __name__ == "__main__":
    pygame.init()
    SCREEN_SIZE = 640, 480
    screen = pygame.display.set_mode(SCREEN_SIZE)
    FPSclock = pygame.time.Clock()
    grass_img = pygame.image.load("resources/images/grass.png")

    group_rabbit = pygame.sprite.Group()
    group_arrow = pygame.sprite.Group()
    
    rabbit = Rabbit()
    group_rabbit.add(rabbit)

    # ========== 敌人实例化 ==============
    group_enemy = pygame.sprite.Group()
    enemyRabbit = EnemyRabbit()
    group_enemy.add(enemyRabbit)

    while True:
        FPSclock.tick(240)
        updateBackground()
        # ========== 调用检测碰撞 =============
        checkCollision() 

        position = pygame.mouse.get_pos()
        getEvent(rabbit, position)
        group_rabbit.update(position)  
        group_arrow.update()

        # ====== 敌人精灵组刷新 =====
        group_enemy.update()

        pygame.display.update()        