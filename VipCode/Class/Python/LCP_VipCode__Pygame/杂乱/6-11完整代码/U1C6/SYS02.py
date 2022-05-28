import pygame,sys
from pygame.locals import*

pygame.init()

screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])

# 思路详解：
# 红圆
# 黑六边形
# 白圆
# 黑三角
# 黑三角

pygame.draw.circle(screen,[255,0,0],[150,185],100,2)
my_polygon=[(100,100),(200,100),(250,185),(200,270),(100,270),(50,185)]
pygame.draw.polygon(screen,[0,0,0],my_polygon)
pygame.draw.circle(screen,[255,255,255],[150,185],87)
pygame.draw.polygon(screen,[0,0,0],[(150,100),(80,230),(220,230)])
pygame.draw.polygon(screen,[0,0,0],[(75,145),(225,145),(150,270)])
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()