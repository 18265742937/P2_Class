import pygame,sys,random
from pygame import locals
'''
玩家战机类
1.初始化玩家飞机，继承父类初始化属性
2.实现的功能有玩家飞机移动的过程（键盘事件）
3.重写父类方法
'''
class PlayerSprite(pygame.sprite.Sprite):  
    #初始化方法，继承父类初始化属性，创建子类属性                                                      #玩家战机
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = 500/2 - 61
        self.rect.y = 500
        self.speed = 1
        self.playMusic()

    #实现背景音效播放
    def playMusic(self):
        """ 播放音乐"""
        music = pygame.mixer.music  #  创建音乐播放器
        music.load("./music/BGM3.flac")   # 加载音乐
        music.play(-1)              # 无限播放音乐

    #实现玩家飞机的移动
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
            if self.rect.y > 595:
                self.rect.y = 595

    #重写父类方法，实现位置更新
    def update(self):
        self.move()

'''
敌方战机类
1.初始化敌方战机，继承父类初始化属性
2.设置rect对象的随机位置
3.实现的功能有敌机对象的移动  # ---
'''
class EnemySprite(pygame.sprite.Sprite):   #----
    #初始化方法，继承父类初始化属性，创建子类属性                     
    def __init__(self,image):        #----
        super().__init__()           #----
        self.image = pygame.image.load(image)   #----
        self.rect = self.image.get_rect()       #----
'''
主要游戏逻辑
1.基本窗口的实现
2.页面的加载
3.创建玩家战机精灵组，并将玩家战机对象添加进玩家战机精灵组，进行精灵组的更新，绘制
4.创建敌方战机精灵组，并将敌方战机对象添加进敌方战机精灵组，进行精灵组的更新，绘制
5.页面的刷新
'''
def main():
    pygame.init()
    pygame.display.set_caption("雷霆战机")
    screen = pygame.display.set_mode((500,700))
    image_bg = pygame.image.load("images/bg/bg1.jpg")
    image_bg = pygame.transform.smoothscale(image_bg, (500, 700))

    player = PlayerSprite("images/hero/hero_b_03.png")
    group_player = pygame.sprite.Group()
    group_player.add(player)

    # 创建敌方战机精灵组和敌机对象，将敌机对象添加到敌机精灵组中
    group_enemy = pygame.sprite.Group()    #----
    boss = EnemySprite("images/enemy/boss.png")   #----
    group_enemy.add(boss)    #----

    while True:
        screen.blit(image_bg, (0,0))
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()

        group_player.update()
        group_player.draw(screen)
        # 对精灵组进行绘制
        group_enemy.draw(screen)    #----
        pygame.display.update()


if __name__ == "__main__":        
    main()



