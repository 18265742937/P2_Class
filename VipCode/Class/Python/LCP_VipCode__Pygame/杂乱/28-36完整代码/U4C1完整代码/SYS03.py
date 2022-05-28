import pygame, sys
from pygame import locals

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

    image = pygame.image.load("images/hero/hero_b_03.png")   # --加载飞机背景
    rect = image.get_rect()
    rect.x = 500 / 2 - 61
    rect.y = 500                 # --设置坐标

    while True:
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(image_bg, (0,0))
        screen.blit(image,rect)       # --绘制飞机
        pygame.display.update()

if __name__ == "__main__":
    main()