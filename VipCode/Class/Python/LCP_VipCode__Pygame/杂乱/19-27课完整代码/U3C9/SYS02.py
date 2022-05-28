import pygame,sys,random
from pygame.locals import *

class APP():
    def __init__(self):
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200,600))
        self.addmissile()
        self.addplane()

    def addmissile(self):
        self.missile = pygame.image.load("导弹.png")
        self.missileRect = self.missile.get_rect()
        self.missileRect.x,self.missileRect.y = random.randint(0,1000),600

    def addplane(self):
        self.plane = pygame.image.load("飞机.png")
        self.planeRect = self.plane.get_rect()
        self.planeRect.x, self.planeRect.y = -300,random.randint(0, 200)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            self.screen.fill([255,255,255])

            if self.missileRect.bottom <=0 or self.missileRect.x>=1200:
                self.missileRect.x,self.missileRect.y = random.randint(0,1000),600
            if self.planeRect.x >= 1400:
                self.planeRect.right = 0

            self.planeRect.move_ip(1,0)
            self.missileRect.move_ip(3, -3)
            self.screen.blit(self.missile, self.missileRect)
            self.screen.blit(self.plane, self.planeRect)

            if self.planeRect.x<= self.missileRect.center[0] <= self.planeRect.right:
                if self.planeRect.y<= self.missileRect.center[1] <= self.planeRect.bottom:
                    # sys.exit()
                    app = APP()
                    app.main()

            pygame.display.update()
            self.fpsClock.tick(120)             # 控制帧数    速度

if __name__ == '__main__':
    app = APP()
    app.main()
