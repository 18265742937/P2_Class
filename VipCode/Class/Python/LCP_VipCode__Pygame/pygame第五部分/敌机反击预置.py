import pygame,sys
from pygame import locals
import random

class PlayerSprite(pygame.sprite.Sprite): #玩家战机
    #初始化方法，继承父类初始化属性，创建子类属性     
    def __init__(self,image, screen):
        super().__init__()

        self.image = pygame.image.load("images/hero/hero_b_03.png")
        self.rect = self.image.get_rect()
        self.rect.x = 500/2 - 61
        self.rect.y= 500

        self.speed = 3

        self.playMusic()

        self.bulletgroup = pygame.sprite.Group()

        self.screen = screen
        self.timer = 0

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
        if keys[locals.K_w] or keys[locals.K_UP]:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0
        if keys[locals.K_s] or keys[locals.K_DOWN]:
            self.rect.y += self.speed
            if self.rect.y > 602:
                self.rect.y = 602
    def update(self):
        self.fire()
        self.bulletgroup.update()
        self.bulletgroup.draw(self.screen)

        self.move()      

        #实现背景音效播放
    def playMusic(self):
        """ 播放音乐"""
        music = pygame.mixer.music  #  创建音乐播放器
        music.load("./BGM3.flac")   # 加载音乐
        music.play(-1)              # 无限播放音乐

    def fire(self):    
        self.timer += 1
        if self.timer == 50:
            self.timer = 0
            bullet = BulletSprite("images/bullet/bullet1.png",  [self.rect.x + 45, self.rect.y - 20], 6)
            self.bulletgroup.add(bullet)    

class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, image, yspeed, movetype, screen): 
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, 300)
        self.rect.y = -50
        self.yspeed = yspeed

        self.xspeed = random.randint(0, yspeed+1) * movetype
        self.screen = screen

    def move(self):
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

        if self.rect.x > 400 or self.rect.x < 0:
            self.xspeed *= -1
            self.rect.x += self.xspeed
        if self.rect.y > 800:
            self.kill()    

    def update(self):
        self.move()

    def bomb(self):
        bombimages = ["images/boom/boom01.png",
                      "images/boom/boom02.png",
                      "images/boom/boom03.png",
                      "images/boom/boom04.png",
                      "images/boom/boom05.png",
                      "images/boom/boom06.png",
                           ] 
        for i in bombimages :
            self.screen.blit(pygame.image.load(i),(self.rect.x,self.rect.y))

            pygame.time.delay(20)
            pygame.display.update() 
        self.kill()                         
#----U5C2代码书写区------

#----------------

def main():
    pygame.init()
    screen = pygame.display.set_mode((500,700))

    pygame.display.set_caption("雷霆战机")
    image_bg = pygame.image.load("images/bg/bg1.jpg")
    image_bg = pygame.transform.smoothscale(image_bg, (500,700))

   

    player = PlayerSprite("images/hero/hero_b_03.png", screen)
    group_player = pygame.sprite.Group()
    group_player.add(player)

    group_enemy = pygame.sprite.Group()

    # 创建两个事件常量
    CREATE_ENEMY = pygame.USEREVENT + 1
    CREATE_BOSS = pygame.USEREVENT + 2

    # 创建定时器
    pygame.time.set_timer(CREATE_ENEMY,random.randint(500,1000))
    pygame.time.set_timer(CREATE_BOSS, random.randint(3000, 5000))

    FPSclock = pygame.time.Clock()


    while True:
        FPSclock.tick(240)
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()
            # 根据不同的事件常量创建不同的敌机对象，并添加到精灵组中
            if event.type == CREATE_ENEMY:
                enemy = EnemySprite("images/enemy/enemy2.png",2,1, screen)
                group_enemy.add(enemy)

                
            if event.type == CREATE_BOSS:
                boss = EnemySprite("images/enemy/boss.png", 1, 0, screen)
                group_enemy.add(boss)    

        

        screen.blit(image_bg, (0,0))
        group_player.update()
        group_player.draw(screen)

        group_enemy.draw(screen)
        group_enemy.update()

        collide_player_enemy = pygame.sprite.groupcollide(group_player, group_enemy, False, True)

        if collide_player_enemy:
            a = list(collide_player_enemy.values())[0]
            a[0].bomb()

        pygame.display.update()        

if __name__ == "__main__":
    main()         