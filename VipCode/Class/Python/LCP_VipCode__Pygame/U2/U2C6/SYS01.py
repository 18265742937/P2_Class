import pygame,sys
from pygame.locals import *

pygame.init()

playSurface = pygame.display.set_mode((640,480))     # 设置界面
pygame.display.set_caption("宇航员")              # 设置标题


while True:
    for event in pygame.event.get():                 # 退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                                                    
    

    pygame.display.update()                          # 刷新
