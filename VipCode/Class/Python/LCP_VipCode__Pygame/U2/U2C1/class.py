import pygame
import sys
import random
from pygame.locals import *
class draw():
    def __init__(self):
        self.x = random.randint(50, 590)
        self.y = random.randint(50, 430)
        pygame.draw.circle(screen, [255, 0, 0], [self.x, self.y], 50)
    def move(self):
        self.x += 1
        self.y += 1
        pygame.draw.circle(screen, [255, 0, 0], [self.x, self.y], 50)
circle = draw()
while True:
    circle.move()
    pygame.display.update()
       




