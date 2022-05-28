import pygame
from pygame import locals
import random, time, math, sys

class BulletSprite(pygame.sprite.Sprite):  
    #敌机子弹初始化
    def __init__(self,imagepath,pos,screen,target):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        self.image = pygame.transform.smoothscale(self.image, (10,10))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        #============== start ================
        # 设置相关属性
        #============== start ================

    def move(self):
        #============== start ================
        # 子弹移动方法
        #============== start ================

    def update(self):   
        self.move()

def main():
    pygame.init()
    FPSclock = pygame.time.Clock()
    screen = pygame.display.set_mode((640,480))

    image_bg = pygame.image.load("./images/地图.png")

    mouse_cursor = pygame.image.load("./images/准星.png")
    mouse_cursor = pygame.transform.smoothscale(mouse_cursor, (25, 25))
    pygame.mouse.set_visible(False)

    group_bullet = pygame.sprite.Group()

    while True:
        FPSclock.tick(200)
        screen.blit(image_bg, (0, 0))

        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            isPressed = pygame.mouse.get_pressed()   

            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()

            #============== start ================
            # 当点击鼠标，从两个位置朝鼠标坐标点发射两颗子弹

            #==============  end  ================
                       
                music = pygame.mixer.music  
                music.load("./music/射击.mp3")   # 加载音乐
                music.play(1)  
  
        group_bullet.update()
        group_bullet.draw(screen)
        screen.blit(mouse_cursor, position)
        pygame.display.update()

if __name__ == "__main__":        
    main()

