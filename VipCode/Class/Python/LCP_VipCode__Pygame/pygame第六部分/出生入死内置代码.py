import pygame
from pygame import locals
import random, time, math, sys

#添加子弹，实现射击及击中功能
#1.定义子弹类
#2.定义子弹对象，添加至精灵组
#3.重写update函数，实现发射子弹功能
#4.调整子弹发射速度

'''
玩家战机类
1.初始化玩家飞机，继承父类初始化属性
2.实现的功能有玩家飞机移动的过程（键盘事件）
3.重写父类方法
4.定义子弹对象，将子弹添加至精灵组
'''
class PlayerSprite(pygame.sprite.Sprite): #玩家战机
    #初始化方法，继承父类初始化属性，创建子类属性     
    def __init__(self,image, screen, hp, score):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = 500/2 - 61
        self.rect.y = 600
        self.speed = 3
        self.playMusic()
        self.screen = screen
        self.bulletgroup = pygame.sprite.Group()
        self.timer = 0

        self.bullettype = 0     
        self.bulletnum = 10

        self.hp = hp         # <<< ====================
        self.score = score

    #实现背景音效播放
    def playMusic(self):
        """ 播放音乐"""
        music = pygame.mixer.music  #  创建音乐播放器
        music.load("./BGM3.flac")   # 加载音乐
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
            if self.rect.y > 602:
                self.rect.y = 602
    
    #重写父类方法，实现位置更新
    def update(self):
        self.move()       
        self.fire()
        self.bulletgroup.update()
        self.bulletgroup.draw(self.screen)

    def fire(self):               

        self.timer += 1
        if self.timer > 50:
            self.timer = 0
            if self.bullettype == 0:
                bullet = BulletSprite("images/bullet/bullet1.png",  [self.rect.x + 45, self.rect.y - 20], 6,0)
                self.bulletgroup.add(bullet)

            elif self.bullettype == 1:
                bullet = BulletSprite("images/bullet/bullet1.png", [self.rect.x + 30, self.rect.y - 20], 6,0)
                bullet2 = BulletSprite("images/bullet/bullet1.png", [self.rect.x + 60, self.rect.y - 20], 6,0)
                self.bulletgroup.add(bullet,bullet2)

            elif self.bullettype == 2:
                bullet = BulletSprite("images/bullet/bullet1.png", [self.rect.x + 30, self.rect.y - 20], 6, 0)
                bullet2 = BulletSprite("images/bullet/bullet1.png", [self.rect.x + 60, self.rect.y - 20], 6, 0)
                bullet3 = BulletSprite("images/bullet/bullet3r.png", [self.rect.x + 65, self.rect.y - 20], 6, 1)
                bullet4 = BulletSprite("images/bullet/bullet3l.png", [self.rect.x + 25, self.rect.y - 20], 6, -1)
                bullet5 = BulletSprite("images/bullet/bullet3r.png", [self.rect.x + 70, self.rect.y - 20], 6, 2)
                bullet6 = BulletSprite("images/bullet/bullet3l.png", [self.rect.x + 25, self.rect.y - 20], 6, -2)
                self.bulletgroup.add( bullet, bullet2, bullet3, bullet4, bullet5, bullet6, )

                self.bulletnum -= 1
                if self.bulletnum <= 0:
                    self.bullettype = 1
                    self.bulletnum = 10

"""
子弹类
1.初始化子弹，继承父类初始化属性
2.重写update方法
"""


class BulletSprite(pygame.sprite.Sprite): #传入父类，精灵                           #玩家子弹精灵租
    def __init__(self,imagepath,pos,yspeed, Offset):    
        super().__init__()
        self.image = pygame.image.load(imagepath)#加载绘制图片
        # self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.yspeed = yspeed

        self.Offset = Offset  
      
    def update(self):

        if self.Offset == 0:          
            self.rect.y -= self.yspeed

        elif abs(self.Offset)==1:
            self.rect.y -= 5
            self.rect.x += self.Offset

        elif abs(self.Offset)==2:
            self.rect.y -= 4
            self.rect.x += self.Offset

        if self.rect.y < -50:
            self.kill()

'''
敌方战机类
1.初始化敌方战机，继承父类初始化属性
2.设置rect对象的随机位置
3.实现的功能有敌机对象的移动
4.重写父类方法
5.添加子弹精灵组，并更新精灵组
'''

class EnemySprite(pygame.sprite.Sprite):                          #敌方战机
    def __init__(self,image,yspeed,movetype,screen, bullettype, hp):   # <<< ====================
        super().__init__()
        self.image = pygame.image.load(image)
        # self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 380)
        self.rect.y = -50
        self.yspeed = yspeed
        self.xspeed = random.randint(0,yspeed+1) * movetype
        self.screen = screen
        #创建敌机子弹精灵组
        self.bulletgroup = pygame.sprite.Group()
        #添加计时器
        self.timer = 0

        self.bullettype = bullettype     
        self.timer2 = 3

        self.hp = hp          # <<< =====================
    #重写父类方法，实现位置更新，超出下边界就杀死精灵
    def move(self):
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

        if self.rect.x > 400 or self.rect.x<0:
            self.xspeed *= -1
            self.rect.x += self.xspeed

        if self.rect.y > 800:
            self.kill()
    def update(self):
        self.fire()        
        self.move()
        self.bulletgroup.update()
        self.bulletgroup.draw(self.screen)


    # 添加爆炸的GIF效果，并且实现播放完GIF消除自己(敌机)的过程
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
            pygame.time.delay(5)
            pygame.display.update()
        # 杀死敌机自己：
        self.kill()

    #创建发射子弹的方法，添加精灵
    def fire(self):
        if self.bullettype == 0:         
            #间隔刷新100次，进行一次刷新
            self.timer += 1
            if self.timer == 100:
                self.timer = 0
                bullet = EnemyBulletSprite("images/bullet/enemy_bullet1.png", [self.rect.x + 40, self.rect.y + 39.5],5, 0)
                #添加左右偏移的敌机子弹
                bullet1 = EnemyBulletSprite("images/bullet/enemy_bullet1.png", [self.rect.x + 40, self.rect.y + 39.5],5, -1)
                bullet2 = EnemyBulletSprite("images/bullet/enemy_bullet1.png", [self.rect.x + 40, self.rect.y + 39.5],5, 1)
                self.bulletgroup.add(bullet,bullet1,bullet2)
                self.timer = 0
        else:     
            self.timer += 1
            self.timer2 += 1

            if self.timer > 100:
                bullet = EnemyBulletSprite("images/bullet/boss_bullet2.png", [self.rect.x + 120, self.rect.y + 39.5],2, -1)
                bullet2 = EnemyBulletSprite("images/bullet/boss_bullet2.png", [self.rect.x + 60, self.rect.y + 39.5],2, 1)
                self.bulletgroup.add(bullet, bullet2)
                self.timer = 0

            if self.timer2 > 200:     #BOSS发射导弹
                bullet = EnemyBulletSprite("images/bullet/boss_bullet.png", [self.rect.x + 80, self.rect.y + 39.5],2, 0)
                self.bulletgroup.add(bullet)
                self.timer2 = 0
'''
敌机子弹类
1.初始化敌机子弹属性，继承精灵属性
2.子弹的移动，超出边界，做出处理
3.重写update方法
'''
class EnemyBulletSprite(pygame.sprite.Sprite):  
    #敌机子弹初始化
    def __init__(self,imagepath,pos,speed,direction):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        # self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
        self.direction = direction
    #子弹的移动，超出边界，做出处理
    def move(self):
        self.rect.y += self.speed 
        #根据不同的参数，进行不同方向的移动
        if self.direction == -1:
            self.rect.x += self.speed/2
        elif self.direction == 1:
            self.rect.x -= self.speed/2        
        if self.rect.y > 700:
            self.kill()
    #重写update方法
    def update(self):       #子弹发射方向
        self.move()


    
class BulletHelp(pygame.sprite.Sprite):                               #补给品
    def __init__(self,imagepath,rect,pos,yspeed,screen,movetype):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.yspeed = yspeed
        self.xspeed = random.randint(0, yspeed) * movetype
        self.screen = screen
    def update(self):
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed
        if self.rect.x > 400:
            self.xspeed *= -1
            self.rect.x += self.xspeed
        if self.rect.x < 0:
            self.xspeed *= -1
            self.rect.x += self.xspeed
        if self.rect.y > 800:
            self.kill()
# ============================== 补给品 end ===================================== 


'''
主要游戏逻辑
1.基本窗口的实现
2.页面的加载
3.创建玩家战机精灵组，并将玩家战机对象添加进玩家战机精灵组，进行精灵组的更新，绘制
4.创建敌方战机精灵组，并将敌方战机对象添加进敌方战机精灵组，进行精灵组的更新，绘制
5.页面的刷新
6.设置定时器和事件常量，根据事件常量判断创建敌机的类型，以及敌机可以不断出现的效果
'''

def main():
    pygame.init()
    pygame.display.set_caption("雷霆战机")
    screen = pygame.display.set_mode((500,700))
    image_bg = pygame.image.load("images/bg/bg1.jpg")
    image_bg = pygame.transform.smoothscale(image_bg, (500, 700))
    font = pygame.font.Font(None,32)
    FPSclock = pygame.time.Clock()

    font = pygame.font.Font(None,32)        # <<< ===================== 

    player = PlayerSprite("images/hero/hero_b_03.png", screen, 100, 0)    # <<< ===================== 
    group_player = pygame.sprite.Group()
    group_player.add(player)


    # 创建敌方战机精灵组
    group_enemy = pygame.sprite.Group()
    group_boss = pygame.sprite.Group()      # <<< ========================
    group_bullethelp = pygame.sprite.Group()
     
    font = pygame.font.Font("STXINGKA.TTF",32)

    # 创建两个事件常量
    CREATE_ENEMY = pygame.USEREVENT + 1
    CREATE_BOSS = pygame.USEREVENT + 2
     
    CREATE_BULLET_HELP = locals.USEREVENT + 3
      

    # 创建定时器
    pygame.time.set_timer(CREATE_ENEMY,random.randint(500,1000))
    pygame.time.set_timer(CREATE_BOSS, random.randint(3000, 5000))
    
    pygame.time.set_timer(CREATE_BULLET_HELP,random.randint(3000,5000))
    
    
    while True:
        FPSclock.tick(240)
        screen.blit(image_bg, (0,0))

        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()

            # 根据不同的事件常量创建不同的敌机对象，并添加道精灵组中
            if event.type == CREATE_ENEMY:
                enemy = EnemySprite("images/enemy/enemy2.png",2,random.randrange(-1,1,2), screen,0, 2)
                group_enemy.add(enemy)

            if event.type == CREATE_BOSS:
                boss = EnemySprite("images/enemy/boss.png", 1, 0, screen, 1, 10)   # <<< ==================
                group_boss.add(boss)
             
            if event.type == CREATE_BULLET_HELP:
                bullethelp = BulletHelp("images/hero/supply.png",[0,0,40,41],[random.randint(0,410),-50],2,screen,-1)
                group_bullethelp.add(bullethelp)
             
        group_player.update()
        group_player.draw(screen)

        # 对精灵组进行更新
        group_enemy.update()
        # 对精灵组进行绘制
        group_enemy.draw(screen)

        group_boss.update()              # <<< =========================
        group_boss.draw(screen)

         
        group_bullethelp.update()
        group_bullethelp.draw(screen)
        
        """检测碰撞之_玩家飞机_敌人小飞机"""
        # 精灵组与精灵组之间检测碰撞：pygame.sprite.groupcollide(玩家精灵组，地方精灵组，不消除玩家，清除敌方)
        collide_player_enemy = pygame.sprite.groupcollide(group_player, group_enemy, False, True)
        # 输出碰撞结果：
        # print( collide_player_enemy)
        # 如果碰撞了：此处判断的是bool值，字典非空即为True。
        
        if collide_player_enemy:
            # 被碰撞的敌机对象调用爆炸方法：
            a = list(collide_player_enemy.values())[0] 
            a[0].bomb()
            # print(list( collide_player_enemy.values() ))

            a[0].hp = 0
            player.hp -= a[0].hp
            player.score += a[0].hp

        """
        取值分析：
            # 1.碰撞时返回一个字典
                collide_player_enemy = {<PlayerSprite Sprite(in 1 groups)>: [<EnemySprite Sprite(in 0 groups)>]}
            # 2.取出字典的值  【注意】dict_values() 里面是两层列表--列表嵌套，类型是：<class 'dict_values'>
                collide_player_enemy.values()  >>>   dict_values([[<EnemySprite Sprite(in 0 groups)>]])
            # 3.使用list转化为列表类型   【注意】是两层列表--列表嵌套，
                list( collide_player_enemy.values() )  >>>  [[<EnemySprite Sprite(in 0 groups)>]]
                list( collide_player_enemy.values() )[0]  >>>  [<EnemySprite Sprite(in 0 groups)>]
                list( collide_player_enemy.values() )[0][0]  >>>  <EnemySprite Sprite(in 0 groups)>
        """

        """检测碰撞之_玩家子弹_敌人小飞机"""
        collide_playerBullet_enemy = pygame.sprite.groupcollide(player.bulletgroup, group_enemy, True, False)       
        if collide_playerBullet_enemy:
            # list(collide_playerBullet_enemy.values())[0][0].bomb()
            values = list(collide_playerBullet_enemy.values())[0][0]
            values.hp -= 1
            if values.hp <= 0:
                values.bomb()
                player.score += 2

        """检测碰撞之_玩家_敌人BOSS"""
        collide_player_BOSS = pygame.sprite.groupcollide(group_player, group_boss, False, True)       
        if collide_player_BOSS:
            values = list(collide_player_BOSS.values())[0][0]
            values.hp == 0
            values.bomb()
            player.hp -= 10
            player.score += 10

        """检测碰撞之_玩家子弹_敌人BOSS"""
        collide_playerBullet_BOSS = pygame.sprite.groupcollide(player.bulletgroup, group_boss, True, False)       
        if collide_playerBullet_BOSS:
            values = list(collide_playerBullet_BOSS.values())[0][0]
            values.hp -= 1
            if values.hp <= 0:
                values.bomb()
                player.score += 10


        """检测碰撞之_玩家飞机_补给小星星"""
        collide_player_bullethelp = pygame.sprite.groupcollide(group_player, group_bullethelp, False, True)
        if collide_player_bullethelp:                            
            player.bullettype += 1
            if player.bullettype > 2:
                player.bullettype = 2
                player.bulletnum = 10

        # <<< =========================== 
        screen.blit(font.render("Score:"+str(player.score) , True,(255, 0, 0)),(20,20))
        screen.blit(font.render("HP:" + str(player.hp), True, (255, 0, 0)), (20, 60))

        # 屏幕显示刷新
        pygame.display.update()

if __name__ == "__main__":        
    main()




"""
添加生命值和分数，并实现多重检测碰撞：
            给己方飞机添加 score 和 hp，并实现显示刷新
            给敌方飞机添加 hp
            多种检测碰撞，并实现分数和生命值的计算刷新
            结合for循环实现检测碰撞
"""