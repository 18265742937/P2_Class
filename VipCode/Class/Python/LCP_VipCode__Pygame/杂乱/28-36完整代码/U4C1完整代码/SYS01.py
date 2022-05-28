import pygame, sys
from pygame import locals
'''
实现窗口
'''
def main():
    pygame.init()
    screen = pygame.display.set_mode((500,700))

    while True:
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":        
    main()




