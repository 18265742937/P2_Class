import pygame
from pygame.locals import *
import math  
import random
from pygame.math import *

class Rabbit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/rabbit.png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.hp = 100
        self.rect.x = 100
        self.rect.y = 100

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_d] or keys[K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > 600:
                self.rect.x = 600
        if keys[K_a] or keys[K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[K_w] or keys[K_UP]:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0
        if keys[K_s] or keys[K_DOWN]:
            self.rect.y += self.speed
            if self.rect.y > 450:
                self.rect.y = 450

    def update(self, position): 
        angle = math.atan2(position[1]-self.rect.y + 60, position[0]- self.rect.x)
        playerrot = pygame.transform.rotate(self.image, 360-angle*57.29)
        screen.blit(playerrot, (self.rect.x, self.rect.y))

        screen.fill((0,255,0), (self.rect.x+10,self.rect.y+70,self.hp/2, 4))
        self.move()

class EnemyRabbit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/rabbit.png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.hp = 100
        self.rect.x = 100
        self.rect.y = 100
        self.angle = 0
        self.shadow = self.image

        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)

        self.brain = Brain()

        # 添加敌人搜索状态
        exploring_state = EnemyRabbitExploring(self)
        self.brain.add_state(exploring_state)

        # 添加敌人的警戒状态
        guarding_state = EnemyRabbitGuarding(self)
        self.brain.add_state(guarding_state)

    def update(self, time_passed):
        self.brain.think()

        if self.hp < 0:
            self.kill()

        if self.speed > 0 and self.location != self.destination:
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.length()
            heading = vec_to_destination.normalize()
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            self.location += travel_distance * heading  

        self.rect.x, self.rect.y = self.location    
        screen.fill((255,255,0), (self.rect.x+10,self.rect.y+70,self.hp/2, 4)) 
        screen.blit(self.shadow, (self.rect.x, self.rect.y)) 

class Light(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.rect = pygame.Rect(x, y, 1, 1)
        self.rect.x = x
        self.rect.y = y
        self.dx = math.cos(angle)*50
        self.dy = math.sin(angle)*50

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        screen.fill((255,255,0), (self.rect.x, self.rect.y, 10,10)) 
        if self.rect.x >= 600 or self.rect.x < 0 or self.rect.y < 0 or self.rect.y >= 450:
            self.kill()

class State(object):
    def __init__(self, name):
        self.name = name
    def do_actions(self):
        pass
    def check_conditions(self):
        pass
    def entry_actions(self):
        pass
    def exit_actions(self):
        pass 

class EnemyRabbitExploring(State):
    def __init__(self, enemyRabbit):
        State.__init__(self, "Exploring")
        self.enemyRabbit = enemyRabbit
        self.random_destination()

        self.finish = False

    def random_destination(self):
        w, h = SCREEN_SIZE
        self.enemyRabbit.destination = Vector2(random.randint(0, w), random.randint(0, h))

    def random_heading(self):
        self.enemyRabbit.angle += random.uniform(-0.5,0.5)
        self.enemyRabbit.shadow = pygame.transform.rotate(self.enemyRabbit.image, 360-self.enemyRabbit.angle*57.29)        
   
    def do_actions(self):
        print("正在执行搜索")
        if random.randint(1, 20) == 1:
            self.random_destination()
        if random.randint(1,30) == 1:
            self.random_heading()

        if random.randint(1, 500) == 1:
            self.finish = True

    def check_conditions(self):
        print("正在检查所作状态条件")
        if self.finish:
            return "Guarding"
    def entry_actions(self):
        print("进入搜索状态")
        self.finish = False
    def exit_actions(self):
        print("退出搜索状态")

class Brain(object):
    def __init__(self):
        self.states = {}
        self.active_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def think(self):
        if self.active_state is None:
            return
        self.active_state.do_actions()    
        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)

    def set_state(self, new_state_name):
        if self.active_state is not None:
            self.active_state.exit_actions()
        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()     

class Arrow(pygame.sprite.Sprite):
    def __init__(self, player, position):
        super().__init__()
        self.image = pygame.image.load('resources/images/bullet.png')
        angle = math.atan2(position[1]-player.rect.y, position[0] - player.rect.x)        
        self.playerrot = pygame.transform.rotate(self.image, 360-angle*57.29)
        self.rect = self.playerrot.get_rect()  
        self.rect.x, self.rect.y = player.rect.x, player.rect.y
        self.speed = 10
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed

    def update(self):
        self.rect.x += self.dx 
        self.rect.y += self.dy

        screen.blit(self.playerrot, (self.rect.x, self.rect.y))
        if self.rect.x < 0 or self.rect.x > 600 or self.rect.y < 0 or self.rect.y > 480:
            self.kill() 

class Barrier(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = pygame.image.load('resources/images/砖块.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))     

class EnemyRabbitGuarding(State):
    def __init__(self, enemyRabbit):
        State.__init__(self, "Guarding")
        self.enemyRabbit = enemyRabbit
        self.enemyRabbit.destination = Vector2(0, 0)
        self.finish = 0

        self.dir = 1

    def do_actions(self):
        if abs(self.enemyRabbit.angle) < 6:
            enemyRabbit.angle += 0.03*self.dir
            self.enemyRabbit.shadow = pygame.transform.rotate(self.enemyRabbit.image, 360-self.enemyRabbit.angle*57.29)
            light = Light(self.enemyRabbit.rect.x, self.enemyRabbit.rect.y, self.enemyRabbit.angle)
            group_light.add(light)
        else:
            self.finish = 1   

    def check_conditions(self):
        print("检查执行条件")
        if self.finish == 1:
            return "Exploring"

    def entry_actions(self):
        print("进入警戒状态")
        self.finish = False
        self.enemyRabbit.angle = 0
        self.dir = random.choice([-1, 1])

    def exit_actions(self):
        print("退出警戒状态")


def setBarrier():
    for x in range(2):
        a = Barrier(50*x+100,120)
        group_barrier.add(a) 

    for x in range(2):
        a = Barrier(50*x+370,120)
        group_barrier.add(a) 

    for x in range(2):
        a = Barrier(50*x+100,350)
        group_barrier.add(a)

    for x in range(2):
        a = Barrier(50*x+370,350)
        group_barrier.add(a)                      

def updateBackground():
    screen.fill((0, 0, 0))
    for x in range(SCREEN_SIZE[0]//grass_img.get_width()+1):
        for y in range(SCREEN_SIZE[1]//grass_img.get_height()+1):
            screen.blit(grass_img, (x*100, y*100))

def getEvent(player, position):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            arrow = Arrow(player, position) 
            group_arrow.add(arrow)

def checkCollision():
    collide_player_enemy = pygame.sprite.groupcollide( group_enemy,group_arrow, False, True)
    if collide_player_enemy:
        for enemy in list(collide_player_enemy):
            enemy.hp -= 21

    collide_barrier_arrow = pygame.sprite.groupcollide( group_barrier,group_arrow, False, True)
    collide_barrier_enemy = pygame.sprite.groupcollide(group_enemy,group_barrier, False, False)

    collide_barrier_light = pygame.sprite.groupcollide(group_barrier, group_light, False, True)
    collide_rabbit_light = pygame.sprite.groupcollide(group_rabbit,group_light,False, False)
    if collide_rabbit_light:
        print("糟糕，被发现了")


if __name__ == "__main__":
    pygame.init()
    SCREEN_SIZE = 640, 480
    screen = pygame.display.set_mode(SCREEN_SIZE)
    FPSclock = pygame.time.Clock()
    grass_img = pygame.image.load("resources/images/grass.png")

    group_rabbit = pygame.sprite.Group()
    group_arrow = pygame.sprite.Group()
    group_enemy = pygame.sprite.Group()
    group_barrier = pygame.sprite.Group()
    group_light = pygame.sprite.Group()

    setBarrier()

    rabbit = Rabbit()
    group_rabbit.add(rabbit)

    enemyRabbit = EnemyRabbit()
    enemyRabbit.brain.set_state("Guarding") 
    group_enemy.add(enemyRabbit)

    while True:
        time_passed = FPSclock.tick(240)
        updateBackground()
        checkCollision()   
        position = pygame.mouse.get_pos()
        getEvent(rabbit, position)
        group_rabbit.update(position)  
        group_arrow.update()
        group_enemy.update(time_passed/8)
        group_barrier.update()
        group_light.update()
        pygame.display.update()        