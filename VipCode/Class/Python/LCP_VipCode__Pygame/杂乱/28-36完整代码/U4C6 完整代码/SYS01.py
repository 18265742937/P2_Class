import pygame
from pygame import locals
import random, sys

'''
玩家战机类
1.初始化玩家飞机，继承父类初始化属性
2.实现的功能有玩家飞机移动的过程（键盘事件）
3.重写父类方法
'''
class PlayerSprite(pygame.sprite.Sprite):
    # 初始化方法，继承父类初始化属性，创建子类属性                       #玩家战机
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = 500 / 2 - 61
        self.rect.y = 600
        self.speed = 3
        self.playMusic()

    # 实现背景音效播放
    def playMusic(self):
        """ 播放音乐"""
        music = pygame.mixer.music  # 创建音乐播放器
        music.load("./music/BGM3.flac")  # 加载音乐
        music.play(-1)  # 无限播放音乐

    # 实现玩家飞机的移动
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

    # 重写父类方法，实现位置更新
    def update(self):
        self.move()


'''
敌方战机类
1.初始化敌方战机，继承父类初始化属性
2.设置rect对象的随机位置
3.实现的功能有敌机对象的移动
4.重写父类方法
'''
class EnemySprite(pygame.sprite.Sprite):
    # 初始化方法，继承父类初始化属性，创建子类属性
    def __init__(self, image, yspeed, movetype,):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 330)
        self.rect.y = -50
        self.yspeed = yspeed
        self.xspeed = random.randint(0, yspeed + 1) * movetype

    # 创建敌机移动的方法，超出下边界就杀死精灵
    def move(self):
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed
        if self.rect.x > 400 or self.rect.x < 0:
            self.xspeed *= -1
            self.rect.x += self.xspeed

        if self.rect.y > 800:
            self.kill()

    # 重写父类方法，调用move方法，实现位置更新
    def update(self):
        self.move()


'''
主要游戏逻辑
1.基本窗口的实现
2.页面的加载
3.创建玩家战机精灵组，并将玩家战机对象添加进玩家战机精灵组，进行精灵组的更新，绘制
4.创建敌方战机精灵组，并将敌方战机对象添加进敌方战机精灵组，进行精灵组的更新，绘制
5.页面的刷新
6.设置定时器和事件常量，根据事件常量判断创建敌机的类型，以及敌机可以不断出现的效果
7.实现精灵组与精灵组之间的检测碰撞
'''
def main():
    pygame.init()
    pygame.display.set_caption("雷霆战机")
    screen = pygame.display.set_mode((500, 700))
    image_bg = pygame.image.load("images/bg/bg1.jpg")
    image_bg = pygame.transform.smoothscale(image_bg, (500, 700))
    FPSclock = pygame.time.Clock()
    player = PlayerSprite("images/hero/hero_b_03.png")
    group_player = pygame.sprite.Group()
    group_player.add(player)
    # 创建敌方战机精灵组
    group_enemy = pygame.sprite.Group()
    # 创建两个事件常量
    CREATE_ENEMY = pygame.USEREVENT + 1
    CREATE_BOSS = pygame.USEREVENT + 2
    # 创建定时器
    pygame.time.set_timer(CREATE_ENEMY, random.randint(500, 1000))
    pygame.time.set_timer(CREATE_BOSS, random.randint(3000, 5000))

    while True:
        FPSclock.tick(240)
        screen.blit(image_bg, (0, 0))
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()

            # 根据不同的事件常量创建不同的敌机对象，并添加道精灵组中
            if event.type == CREATE_ENEMY:
                enemy = EnemySprite("images/enemy/enemy2.png", 2, 1)
                group_enemy.add(enemy)
            if event.type == CREATE_BOSS:
                boss = EnemySprite("images/enemy/boss.png", 1, 0)
                group_enemy.add(boss)

        group_player.update()
        group_player.draw(screen)
        group_enemy.update()
        group_enemy.draw(screen)

        # 精灵组与精灵组之间检测碰撞：pygame.sprite.groupcollide(玩家精灵组，地方精灵组，不消除玩家，清除敌方)
        collide_player_enemy = pygame.sprite.groupcollide(group_player, group_enemy, False, True)      # -------
        # 输出碰撞结果：
        print(collide_player_enemy)       # ------ 查看返回值
        # 屏幕显示刷新
        pygame.display.update()


if __name__ == "__main__":
    main()