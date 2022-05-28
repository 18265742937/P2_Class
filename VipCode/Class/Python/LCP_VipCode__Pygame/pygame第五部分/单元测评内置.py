import pygame
from pygame import locals
import random, time, math, sys
class Plant(pygame.sprite.Sprite): #植物类
    #初始化方法，继承父类初始化属性，创建子类属性     
  
    def __init__(self, image,screen):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 280
        self.screen=screen
        self.f =0
   
       
       
    #植物动起来
    def move(self):
        bombimages = ["./images/Hey/Peashooter_0.png",
                    "./images/Hey/Peashooter_1.png",
                    "./images/Hey/Peashooter_2.png",
                    "./images/Hey/Peashooter_3.png",
                    "./images/Hey/Peashooter_4.png",
                    "./images/Hey/Peashooter_5.png",
                    "./images/Hey/Peashooter_6.png",
                    "./images/Hey/Peashooter_7.png",
                    "./images/Hey/Peashooter_8.png",
                    "./images/Hey/Peashooter_9.png",
                    "./images/Hey/Peashooter_10.png",
                    "./images/Hey/Peashooter_11.png",
                    "./images/Hey/Peashooter_12.png",]
                      
          
        for i in bombimages :
            self.f+=1                              
            if self.f==12:
                self.f=0
                self.screen.blit(pygame.image.load(i),(self.rect.x,self.rect.y))
                #self.screen.blit
                pygame.time.delay(80)
    # 豌豆射手开火
    def fire(self):
        # =================== start ====================== 
        pass
        # =================== end ======================     

    
    #重写父类方法，实现位置更新
    def update(self):
        # =================== start ====================== 
        pass
        # =================== end ======================     

      
       

class Zombie(pygame.sprite.Sprite): #僵尸类
    #初始化方法，继承父类初始化属性，创建子类属性     
    def __init__(self, image,screen):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 200
        self.screen=screen
        self.f =0



"""生成子弹"""
class PlantSprite(pygame.sprite.Sprite):  #子弹精灵租

    def __init__(self,imagepath,pos,xspeed):
        super().__init__()
        self.image = pygame.image.load(imagepath)#加载绘制图片
        # self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = xspeed

    """更新子弹"""
    def update(self):
        # =================== start ====================== 
        pass
        # =================== end ======================     

      


def main():
    pygame.init()
    pygame.display.set_caption("植物大战僵尸")
    screen = pygame.display.set_mode((1000,600))
    image_bg = pygame.image.load("images/background1.jpg")
    image_bg = pygame.transform.smoothscale(image_bg, (1000, 600))
    FPSclock = pygame.time.Clock()
    # 生成豌豆
    player =Plant("./images/Hey/Peashooter_0.png",screen)
    # 生成僵尸
    zombie = Zombie("./images/corpse/Zombie_0.png", screen)
    group_zombie = pygame.sprite.Group()
    group_zombie.add(zombie)

    while True:
        FPSclock.tick(240)
        screen.blit(image_bg, (0,0))
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()
        player.update()
        player.move() 
        group_zombie.draw(screen)
        pygame.display.update()



if __name__ == "__main__":        
    main()




