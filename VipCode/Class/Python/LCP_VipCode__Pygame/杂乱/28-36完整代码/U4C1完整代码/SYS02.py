import pygame, sys
from pygame import locals

'''
优化窗口
'''


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("雷霆战机")  # ---- 设置标题
    image_bg = pygame.image.load("images/bg/bg1.jpg")  # ----加载背景
    image_bg = pygame.transform.smoothscale(image_bg, (500, 700)) # ---- 调整大小

    while True:
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(image_bg, (0, 0))   # ---- 绘制背景
        pygame.display.update()         #----- 更新


if __name__ == "__main__":
    main()