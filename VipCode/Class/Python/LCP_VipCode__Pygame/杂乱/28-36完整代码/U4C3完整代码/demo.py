import pygame, sys
from pygame import locals
'''
玩家战机类
1.初始化玩家飞机，继承父类初始化属性
2.实现的功能有玩家飞机移动的过程（键盘事件）
3.重写父类方法
'''
class PlayerSprite(pygame.sprite.Sprite):
    #初始化方法，继承父类初始化属性，创建子类属性
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = 500/2 - 61
        self.rect.y = 500
        self.speed = 1     # --- 移动偏移量

    #实现玩家飞机的移动
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[locals.K_d] or keys[locals.K_RIGHT]:
            self.rect.x += self.speed       #--- 重新设置飞机坐标
            if self.rect.x > 378:         #--- 飞机不得超边界
                self.rect.x = 378
        if keys[locals.K_a] or keys[locals.K_LEFT]:
            self.rect.x -= self.speed   # --
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[locals.K_w] or keys[locals.K_UP]:
            self.rect.y -= self.speed  # --
            if self.rect.y < 0:
                self.rect.y = 0
        if keys[locals.K_s] or keys[locals.K_DOWN]:
            self.rect.y += self.speed # --
            if self.rect.y > 595:
                self.rect.y = 595

    #重写父类方法，实现位置更新
    def update(self):  # --定义更新的函数
        self.move()

'''
主要游戏逻辑
1.基本窗口的实现
2.页面的加载
3.创建精灵组，并将对象添加进精灵组，进行精灵组的更新，绘制
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
    while True:
        screen.blit(image_bg, (0,0))
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()
        group_player.update()  # --调用精灵组所有精灵update
        group_player.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()