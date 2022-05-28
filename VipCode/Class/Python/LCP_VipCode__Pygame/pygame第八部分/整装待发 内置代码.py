
import pygame
from pygame.locals import *
from pygame import locals

def getEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

if __name__ == "__main__":

    SCREEN_SIZE = 640, 480
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    FPSclock = pygame.time.Clock()

    while True:
        FPSclock.tick(240) 
        getEvent()
        pygame.display.update()  
     