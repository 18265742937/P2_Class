# -*- coding: utf-8 -*-
import random
import pygame, sys
from pygame.locals import *
# 加鸟
# 调用显示
# 选鸟

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(3):
            img = pygame.image.load("./img/bird0_%s.png" % i).convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.rect = img.get_rect()
            self.images.append(img)
        self.frame = 0  # 初始帧数
        self.rect.x = 50
        self.rect.y = 10
        self.distance = 0

    def update(self):
        self.distance += 0.5
        self.rect.y += self.distance
        self.frame += 1
        if self.frame > 2:
            self.frame = 0
        self.image = self.images[self.frame]

        if self.rect.top < -20 or self.rect.bottom > app.height+20:
            app.flag = False
            app.music.stop()
            musicList = ["audio/呃.mp3", "audio/搞错了再来.wav"]
            app.playMusic(random.choice(musicList))
            pygame.time.wait(1000)

    def reset(self):
        self.rect.y = 10
        self.distance = 0
        app.flag = True

class Pipe(pygame.sprite.Sprite):
    def __init__(self, image, top):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = app.width
        self.rect.y = top

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()
        if self.rect.x == 30:
            app.score += 0.5

class APP():
    def __init__(self):
        # 初始化
        pygame.init()
        self.width, self.height = 700, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('飞翔的小鸟')
        self.bg = pygame.image.load("img/bg_day.png").convert()  # 背景图片导入并缩放为窗口大小
        self.bg = pygame.transform.smoothscale(self.bg, (self.width, self.height))
        self.FPSclock = pygame.time.Clock()
        self.pipe_down_image = pygame.image.load("img/pipe_down.png").convert_alpha()  # 口冲下的管道
        self.pipe_up_image = pygame.image.load("img/pipe_up.png").convert_alpha()  # 口冲上的管道
        self.pipes = pygame.sprite.Group()
        self.flag = False
        self.font36 = pygame.font.SysFont('Arial', 36)  # 字体对象
        self.msg = self.font36.render('Press SPACE to Start', True, (255, 255, 255))  # 屏幕上的文本
        self.score = 0
        pygame.time.set_timer(USEREVENT, 1500)
        self.addBird()                           # --------------------------

    def addBird(self):                # -----------------------------------
        imglist = ['bird0_0.png','bird1_0.png','bird2_0.png']  # -----------------
        self.rolelist = []  # -----------------
        for x in imglist:  # -----------------
            img = pygame.image.load("img/%s"%x)  # -----------------
            rect = img.get_rect()  # -----------------
            rect.x,rect.y = 70+imglist.index(x)*100, 400  # -----------------
            self.rolelist.append([img,rect])  # -----------------
        self.rolelist[0][1].y = 370  # -----------------


    def playMusic(self,name,x=1):
        self.music = pygame.mixer.music   #  创建音乐播放器
        self.music.load(name)   # 加载音乐
        self.music.play(loops=x)   # 播放音乐

    def main(self):
        while True:
            self.screen.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN and event.key == K_SPACE:
                    print(self.flag)
                    if self.flag == True:
                        bird.distance = -8
                    else:
                        self.playMusic("audio/bgm1.mp3",-1)
                        bird.reset()
                        self.pipes.empty()  # 删除编组中所有的精灵。
                        self.score = 0

                if event.type == USEREVENT:
                    y = random.randint(-120, 120)
                    pipe_up = Pipe(self.pipe_up_image, 260 + 80 + y)
                    pipe_down = Pipe(self.pipe_down_image, -60 - 80 + y)
                    self.pipes.add(pipe_up, pipe_down)

            if self.flag:
                self.pipes.update()
                self.pipes.draw(self.screen)
                bird.update()
                self.screen.blit(bird.image, bird.rect)

                if pygame.sprite.spritecollide(bird, self.pipes, False, pygame.sprite.collide_mask):  # 碰撞检测
                    self.flag = False
                    self.music.stop()
                    musicList = ["audio/呃.mp3", "audio/搞错了再来.wav"]
                    self.playMusic(random.choice(musicList))
                    pygame.time.wait(1000)

                self.screen.blit(self.font36.render('Score : %d' % self.score, True, (255, 255, 255)), (0, 0))

            else:
                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(self.msg, (50, 50))
                self.screen.blit(self.font36.render('Score : %d' % self.score, True, (255, 255, 255)), (100, 100))

            pygame.display.update()
            self.FPSclock.tick(60)


if __name__ == '__main__':
    app = APP()
    bird = Bird()
    app.main()


