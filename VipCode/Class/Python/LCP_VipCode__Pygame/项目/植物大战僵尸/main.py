import pygame
from pygame.locals import *
from random import *
import sys
import traceback
import Plants
import Products
import SeedBank
import LawnMower
import Zombies


# pygame初始化
pygame.init()
pygame.mixer.init()

# 创建窗口大小
bg_size = width,height = 800,600
screen = pygame.display.set_mode(bg_size)

pygame.display.set_caption("植物大战僵尸--freedom")
clock = pygame.time.Clock()

# 颜色
BLACK = (0,0,0)
RED = (255,0,0)
BAR_COLOR = (189,223,89)

# 植物种植范围
borderx = L, R = 30, 780
bordery = T, B = 90, 570
X = [75, 155, 235, 322, 406, 480, 562, 641, 720]
Y = [135, 225, 325, 427, 523]

# 载入游戏音乐与音效
pygame.mixer.music.load("music/game.mp3")
pygame.mixer.music.set_volume(1)
chew_sound = pygame.mixer.Sound("music/chew.wav")
chew_sound.set_volume(0.3)
sungather_sound = pygame.mixer.Sound("music/sungather.wav")
sungather_sound.set_volume(0.7)
hit_sound = pygame.mixer.Sound("music/hit.wav")
hit_sound.set_volume(2)
gameover_sound = pygame.mixer.Sound("music/gameover.wav")
gameover_sound.set_volume(0.5)

# 载入图片
zombies_images = Zombies.ZombiesImages()
plants_images = Plants.PlantsImages()
products_images = Products.ProductsImages()
car_image = LawnMower.CarImage()

def add_ordinaryzombies(group,num):
    for i in range(num):
        oz = Zombies.OrdinaryZombie(width, Y, zombies_images)
        group.add(oz)

def add_coneheadzombies(group,num):
    for i in range(num):
        cz = Zombies.ConeheadZombie(width, Y, zombies_images)
        group.add(cz)

def add_bucketheadzombies(group,num):
    for i in range(num):
        bz = Zombies.BucketheadZombie(width, Y, zombies_images)
        group.add(bz)

def add_flagzombies(group,num):
    for i in range(num):
        fz = Zombies.FlagZombie((width + 50), Y, zombies_images)
        group.add(fz)

def main():
    # 音频播放
    open_music = True
    open_sound = True
    play_gameover_sound = False
    pygame.mixer.music.play(-1)

    # 准备植物组合
    plantx = pygame.sprite.Group()
    # 种植的植物组合
    plants = pygame.sprite.Group()
    # 产物集合
    products = pygame.sprite.Group()

    # 准备生成向日葵
    sunflowerx = Plants.SunFlower(plants_images)
    plantx.add(sunflowerx)
    # 准备生成豌豆射手
    peashooterx = Plants.Peashooter(plants_images)
    plantx.add(peashooterx)
    # 准备生成坚果
    wallnutx = Plants.WallNut(plants_images)
    plantx.add(wallnutx)
    # 准备生成火炬
    torchwoodx = Plants.Torchwood(plants_images)
    plantx.add(torchwoodx)
    torchwoods = pygame.sprite.Group()  # 用于与弹丸做碰撞检测
    # 生成铲子
    shovel = Plants.Shovel(plants_images)
    plantx.add(shovel)

    # 判断拖拽的图像是否出界
    outborder = False

    # 僵尸大波袭来
    large_come = False
    large_coming = False
    large_time = 60
    large_warn_time = 3

    # 生成5辆小车
    cars = pygame.sprite.Group()
    cars_temp = []
    for i in range(5):
        cars_temp.append(LawnMower.Car(L,car_image))
    i = 0
    for y in Y:
        cars_temp[i].rect.centery = y + 25
        i += 1
    for c in cars_temp:
        cars.add(c)

    # 僵尸组合
    zombies = pygame.sprite.Group()

    # 生成僵尸
    add_ordinaryzombies(zombies, 5)
    add_coneheadzombies(zombies, 3)
    add_bucketheadzombies(zombies, 2)

    # 游戏界面
    bg_image = pygame.image.load("photo/others/background.png").convert_alpha()
    bg_rect = bg_image.get_rect()
    bg_rect.left, bg_rect.top = -200, 0
    bar_image = pygame.image.load("photo/others/FlagMeterEmpty.png").convert_alpha()
    bar_parts1_image = pygame.image.load("photo/others/FlagMeterParts1.png").convert_alpha()
    bar_parts2_image = pygame.image.load("photo/others/FlagMeterParts2.png").convert_alpha()
    largewave_image = pygame.image.load("photo/others/LargeWave.gif").convert_alpha()
    largewave_rect = largewave_image.get_rect()
    largewave_rect.centerx, largewave_rect.centery = width // 2, height // 2
    seedbank = SeedBank.SeedBank()

    # 菜单界面
    open_menu = False
    menu_image = pygame.image.load("photo/others/menu.png").convert_alpha()
    menu_rect = menu_image.get_rect()
    menu_rect.centerx, menu_rect.centery = width // 2, height // 2
    button_nor_image = pygame.image.load("photo/others/button_nor.png").convert_alpha()
    button_pressed_image = pygame.image.load("photo/others/button_pressed.png").convert_alpha()
    button_image = button_nor_image
    button_rect = button_image.get_rect()
    button_rect.right, button_rect.top = width, 0
    resume_nor_image = pygame.image.load("photo/others/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("photo/others/resume_pressed.png").convert_alpha()
    resume_image = resume_nor_image
    resume_rect = resume_image.get_rect()
    resume_rect.left, resume_rect.top = 298, 408
    check_box_image = pygame.image.load("photo/others/check_box.png").convert_alpha()
    check_box_rect1 = check_box_image.get_rect()
    check_box_rect2 = check_box_image.get_rect()
    check_box_rect1.centerx, check_box_rect1.centery = 450, 260
    check_box_rect2.centerx, check_box_rect2.centery = 450, 297
    tick_image = pygame.image.load("photo/others/tick.png").convert_alpha()
    tick_rect1 = tick_image.get_rect()
    tick_rect2 = tick_image.get_rect()
    tick_rect1.centerx, tick_rect1.centery = check_box_rect1.centerx, check_box_rect1.centery
    tick_rect2.centerx, tick_rect2.centery = check_box_rect2.centerx, check_box_rect2.centery
    quitgame_nor_image = pygame.image.load("photo/others/quitgame_nor.png").convert_alpha()
    quitgame_pressed_image = pygame.image.load("photo/others/quitgame_pressed.png").convert_alpha()
    quitgame_image = quitgame_nor_image
    quitgame_rect = quitgame_image.get_rect()
    quitgame_rect.left, quitgame_rect.top = 318, 352

    # 游戏结束界面
    gameover = False
    open_quit_window = False
    zombiewon_display_time = 7
    zombiewon_image = pygame.image.load("photo/others/ZombiesWon.png").convert_alpha()
    zombiewon_rect = zombiewon_image.get_rect()
    zombiewon_rect.centerx, zombiewon_rect.centery = width // 2, height // 2
    quit_window_image = pygame.image.load("photo/others/exit_window.png").convert_alpha()
    quit_window_rect = quit_window_image.get_rect()
    quit_window_rect.centerx, quit_window_rect.centery = width // 2, height // 2
    quit_nor_image = pygame.image.load("photo/others/quit_nor.png").convert_alpha()
    quit_pressed_image = pygame.image.load("photo/others/quit_pressed.png").convert_alpha()
    quit_image = quit_nor_image
    quit_rect = quit_image.get_rect()
    quit_rect.centerx, quit_rect.centery = width // 2 ,380

    # 游戏开始界面
    start = False
    start_ready = False
    open_help = False
    start_bg_image = pygame.image.load("photo/others/start_background.png").convert_alpha()
    start_nor_image = pygame.image.load("photo/others/start_nor.png").convert_alpha()
    start_pressed_image = pygame.image.load("photo/others/start_pressed.png").convert_alpha()
    start_image = start_nor_image
    start_rect = start_image.get_rect()
    start_rect.left, start_rect.top = 467,86
    game_logo_image = pygame.image.load("photo/others/game_logo.png").convert_alpha()
    game_logo_rect = game_logo_image.get_rect()
    game_logo_rect.left, game_logo_rect.top = 13, -game_logo_rect.height
    exit_nor_image = pygame.image.load("photo/others/exit_nor.png").convert_alpha()
    exit_pressed_image = pygame.image.load("photo/others/exit_pressed.png").convert_alpha()
    exit_image = exit_nor_image
    exit_rect = exit_image.get_rect()
    exit_rect.left, exit_rect.top = 730, 515
    help_nor_image = pygame.image.load("photo/others/help_nor.png").convert_alpha()
    help_pressed_image = pygame.image.load("photo/others/help_pressed.png").convert_alpha()
    help_image = help_nor_image
    help_rect = help_image.get_rect()
    help_rect.left, help_rect.top = 667, 526
    option_nor_image = pygame.image.load("photo/others/option_nor.png").convert_alpha()
    option_pressed_image = pygame.image.load("photo/others/option_pressed.png").convert_alpha()
    option_image = option_nor_image
    option_rect = option_image.get_rect()
    option_rect.left, option_rect.top = 607, 489
    help_doc_image = pygame.image.load("photo/others/Help.png").convert_alpha()
    help_doc_rect = help_doc_image.get_rect()
    help_doc_rect.centerx, help_doc_rect.centery = width // 2, height // 2
    off_help_image = pygame.image.load("photo/others/off_help.png").convert_alpha()
    off_help__rect = off_help_image.get_rect()
    off_help__rect.left, off_help__rect.top = 615, 120
    prepare_tip_images = []
    prepare_tip_images.extend([\
        pygame.image.load("photo/others/PrepareGrowPlants1.png").convert_alpha(), \
        pygame.image.load("photo/others/PrepareGrowPlants2.png").convert_alpha(), \
        pygame.image.load("photo/others/PrepareGrowPlants3.png").convert_alpha() \
        ])
    prepare_tip_rect = prepare_tip_images[0].get_rect()
    prepare_tip_rect.centerx, prepare_tip_rect.centery = width // 2, height // 2
    index_prepare_tip_image = -1
    num_prepare_tip_image = 3

    # 植物影子图片
    plantshadow = pygame.image.load("photo/others/plantshadow.png").convert_alpha()

    # 阳光数量
    sun_num = 50
    sun_num_font = pygame.font.Font("font/corisandebold.otf",19)
    COLOR = BLACK

    # 阳光集合
    suns = pygame.sprite.Group()

    # 阳光补给和消失时间
    supply_time = 6
    disappear_time1 = 12
    disappear_time2 = 8

    # 计时器
    count_time = 0
    COUNT_TIME = USEREVENT
    pygame.time.set_timer(COUNT_TIME,1 * 1000)

    # 弹丸集合
    bullets = pygame.sprite.Group()

    # 用于切换图片
    delay_1 = 5
    delay_2 = 8
    delay_3 = 50

    # 是否选中植物
    select = 0

    # 游戏进度条长度
    bar_length = 1

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 玩家操作
            elif event.type == MOUSEBUTTONDOWN:
                # 选择植物卡片
                if not open_menu and not gameover and start_ready:
                    for px in plantx:
                        if event.button == 1 and px.card_rect.collidepoint(event.pos):
                            plant_index = px.index
                            pos_image = px.images[0]
                            pos_rect = px.rect
                            pos_price = px.price
                            if sun_num < pos_price:
                                COLOR = RED
                            select = 1
                        if select == 1:
                            if event.button == 3 and pos_rect.collidepoint(event.pos):
                                select = 0
                # 收集阳光
                if not open_menu and not gameover and start_ready:
                    for s in suns:
                        if s.is_supply:
                            if event.button == 1 and s.rect1.collidepoint(event.pos):
                                s.gather = True
                                if open_sound:
                                    sungather_sound.play()
                        else:
                            if event.button == 1 and s.rect2.collidepoint(event.pos):
                                s.gather = True
                                if open_sound:
                                    sungather_sound.play()
                # 菜单操作
                if not gameover and start_ready:
                    if event.button == 1 and button_rect.collidepoint(event.pos):
                        open_menu = True
                    if event.button == 1 and quitgame_rect.collidepoint(event.pos) and open_menu:
                        pygame.quit()
                        sys.exit()
                if not gameover:
                    if event.button == 1 and resume_rect.collidepoint(event.pos):
                        open_menu = False
                    if event.button == 1 and check_box_rect1.collidepoint(event.pos) and open_menu:
                        if open_sound:
                            open_sound = False
                        else:
                            open_sound = True
                    if event.button == 1 and check_box_rect2.collidepoint(event.pos) and open_menu:
                        if open_music:
                            open_music = False
                            pygame.mixer.music.pause()
                        else:
                            open_music = True
                            pygame.mixer.music.unpause()
                # 游戏初始界面操作
                if not start:
                    if event.button == 1 and start_rect.collidepoint(event.pos) and not open_menu and not open_help:
                        start = True
                    if event.button == 1 and exit_rect.collidepoint(event.pos) and not open_menu and not open_help:
                        pygame.quit()
                        sys.exit()
                    if event.button == 1 and help_rect.collidepoint(event.pos) and not open_menu:
                        open_help = True
                    if event.button == 1 and off_help__rect.collidepoint(event.pos) and open_help:
                        open_help = False
                    if event.button == 1 and option_rect.collidepoint(event.pos) and not open_help:
                        open_menu = True
                # 游戏结束窗口操作
                if gameover:
                    if event.button == 1 and quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            elif event.type == MOUSEBUTTONUP and not open_menu and not gameover and start_ready:
                if event.button == 1:
                    if select == 1:
                        if not outborder:
                            # 生成植物
                            if plant_index == 1:
                                plant = Plants.SunFlower(plants_images)
                            if plant_index == 2:
                                plant = Plants.Peashooter(plants_images)
                            if plant_index == 3:
                                plant = Plants.WallNut(plants_images)
                            if plant_index == 4:
                                plant = Plants.Torchwood(plants_images)
                            if plant_index == 5:
                                plant = Plants.Shovel(plants_images)
                            plant.rect.center = event.pos
                            # 位置调整
                            minx = X[0]
                            miny =Y[0]
                            for x in X:
                                if abs(plant.rect.centerx - x) < abs(plant.rect.centerx - minx):
                                    minx = x
                            plant.rect.centerx = minx
                            for y in Y:
                                if abs(plant.rect.centery - y) < abs(plant.rect.centery - miny):
                                    miny = y
                            plant.rect.centery = miny
                            # 检查位置是否已有植物
                            have_plant = False
                            for p in plants:
                                if (plant.rect.centerx == p.rect.centerx) and \
                                        (plant.rect.centery == p.rect.centery):
                                    have_plant = True
                                    if plant_index == 5:
                                        plants.remove(p)
                                        if p.index == 4:
                                            torchwoods.remove(p)
                                        if p.index == 2:
                                            for b in bullets:
                                                if (b.left == p.rect.centerx + 20) and (b.top == p.rect.centery - 28):
                                                    bullets.remove(b)
                                                    products.remove(b)
                            if not have_plant and (plant_index != 5) and (sun_num >= plant.price):
                                plants.add(plant)
                                sun_num -= plant.price
                                if plant.index == 4:
                                    torchwoods.add(plant)
                                # 豌豆射手生成弹丸
                                if plant.index == 2:
                                    bullet = Products.Bullet(bg_size, plant.rect.center,products_images)
                                    bullets.add(bullet)
                                    products.add(bullet)
                        select = 0
                        COLOR = BLACK

            elif event.type == MOUSEMOTION:
                # 所以button的按压样式
                if button_rect.collidepoint(event.pos) and not open_menu:
                    button_image = button_pressed_image
                else:
                    button_image = button_nor_image
                if resume_rect.collidepoint(event.pos) and open_menu:
                    resume_image = resume_pressed_image
                else:
                    resume_image = resume_nor_image
                if quitgame_rect.collidepoint(event.pos) and start_ready:
                    quitgame_image = quitgame_pressed_image
                else:
                    quitgame_image = quitgame_nor_image
                if quit_rect.collidepoint(event.pos) and gameover:
                    quit_image = quit_pressed_image
                else:
                    quit_image = quit_nor_image
                if start_rect.collidepoint(event.pos) and not start and not open_menu and not open_help:
                    start_image = start_pressed_image
                else:
                    start_image = start_nor_image
                if exit_rect.collidepoint(event.pos) and not start and not open_menu and not open_help:
                    exit_image = exit_pressed_image
                else:
                    exit_image = exit_nor_image
                if help_rect.collidepoint(event.pos) and not start and not open_menu and not open_help:
                    help_image = help_pressed_image
                else:
                    help_image = help_nor_image
                if option_rect.collidepoint(event.pos) and not start and not open_menu and not open_help:
                    option_image = option_pressed_image
                else:
                    option_image = option_nor_image

            elif event.type == COUNT_TIME and not open_menu and start_ready:
                if not gameover:
                    count_time += 1
                    # 游戏进度条
                    if not large_coming:
                        bar_length += 1
                        if bar_length == 128:
                            large_coming = True
                            if not large_come:
                                large_come = True
                                # 生成举旗僵尸
                                add_flagzombies(zombies, 2)
                                # 僵尸大波袭来位置改变
                                i = 0
                                for z in zombies:
                                    if z.rect.left > width:
                                        z.rect.left = width + 50 + (i * 20)
                                        i += 1
                                        if i > 5:
                                            i = 0
                        else:
                            large_coming = False
                        if bar_length > 128:
                            bar_length = 1
                    # 僵尸大波袭来时间
                    if large_coming:
                        large_time -= 1
                        large_warn_time -= 1
                        if large_time == 0:
                            large_coming = False
                            large_come = False
                            large_time = 60
                            large_warn_time = 3
                            # 增加僵尸数量
                            add_ordinaryzombies(zombies,5)
                            add_coneheadzombies(zombies,3)
                            add_bucketheadzombies(zombies,2)
                    # 弹丸发射
                    for p in plants:
                        for z in zombies:
                            if (z.rect.right > p.rect.right) and (z.rect.centerx < width) \
                                    and (z.rect.centery == p.rect.centery - 25) and not z.die:
                                for b in bullets:
                                    if (b.left == p.rect.centerx + 20) and (b.top == p.rect.centery - 28):
                                        b.shoot = True
                    # 生成阳光
                    if (count_time % supply_time == 0):
                        sun = Products.Sun(T, L,products_images)
                        suns.add(sun)
                        products.add(sun)
                    for s in suns:
                        s.count_time += 1
                    for p in plants:
                        if p.index == 1:
                            p.count_time += 1
                            if (p.count_time % p.create_time == 0):
                                sun = Products.Sun(p.rect.top, p.rect.centerx,products_images)
                                sun.is_supply = False
                                sun.count_time = 1
                                suns.add(sun)
                                products.add(sun)
                    for s in suns:
                        if (s.count_time % disappear_time1 == 0) and s.is_supply:
                            suns.remove(s)
                            products.remove(s)
                        if (s.count_time % disappear_time2 == 0) and not s.is_supply:
                            suns.remove(s)
                            products.remove(s)
                    # 植物被攻击
                    for p in plants:
                        if p.attacked:
                            for i in range(p.num_az):
                                p.blood -= 1
                                if open_sound:
                                    chew_sound.play()
                                if p.blood == 26 and p.index == 3:
                                    p.images = p.c1_images
                                    p.index_image = p.index_c1_image
                                    p.num_image = p.num_c1_image
                                    p.mask = p.c1_mask
                                if p.blood == 13 and p.index == 3:
                                    p.images = p.c2_images
                                    p.index_image = p.index_c2_image
                                    p.num_image = p.num_c2_image
                                    p.mask = p.c2_mask
                                if p.blood == 0:
                                    plants.remove(p)
                                    if p.index == 2:
                                        for b in bullets:
                                            if (b.left == p.rect.centerx + 20) and (b.top == p.rect.centery - 28):
                                                bullets.remove(b)
                                                products.remove(b)
                                    if p.index == 4:
                                        torchwoods.remove(p)
                else:
                    zombiewon_display_time -= 1
                    if zombiewon_display_time == 0:
                        open_quit_window = True


        if not start:
            # 绘制游戏初始界面
            pygame.mixer.music.pause()
            screen.blit(start_bg_image,(0,0))
            screen.blit(game_logo_image, game_logo_rect)
            game_logo_rect.top += 10
            if game_logo_rect.top > 8:
                game_logo_rect.top = 8
            screen.blit(start_image, start_rect)
            screen.blit(exit_image, exit_rect)
            screen.blit(help_image, help_rect)
            screen.blit(option_image, option_rect)
            if open_help:
                screen.blit(help_doc_image, help_doc_rect)
                screen.blit(off_help_image, off_help__rect)
        else:
            # 绘制游戏背景
            if gameover:
                speed = 5
                bg_rect.left += speed
                if bg_rect.left > 0:
                    bg_rect.left = 0
                else:
                    # 调整所有对象位置
                    for p in plants:
                        p.rect.left += speed
                    for z in zombies:
                        z.rect.left += speed
                        z.zh_rect.left += speed
                    for s in suns:
                        if s.is_supply:
                            s.rect1.left += speed
                        else:
                            s.rect2.left += speed
                    for b in bullets:
                        b.rect.left += speed
                    for c in cars:
                        c.rect.left += speed
            screen.blit(bg_image,bg_rect)

            if not gameover:
                # 绘制游戏进度条
                if start_ready:
                    screen.blit(bar_image, (width - 200, height - 27))
                    screen.blit(bar_parts2_image, (width - 195, height - 30))
                    pygame.draw.line(screen,BAR_COLOR,(width - 51 - bar_length, height - 17),(width - 51,height - 17), 7)
                    screen.blit(bar_parts1_image,(width - 68 - bar_length, height - 32))

                # 绘制卡片栏
                if not open_menu and not gameover:
                    seedbank.move()
                screen.blit(seedbank.image,seedbank.rect)
                # 绘制卡片栏里的卡片
                if seedbank.position:
                    for px in plantx:
                        screen.blit(px.card_image,px.card_rect)

            # 绘制5辆小车
            if seedbank.position:
                for c in cars:
                    if not open_menu and not gameover:
                        if not c.active:
                            c.move1()
                        else:
                            c.move2()
                    screen.blit(c.image,c.rect)
                    if c.rect.left > width:
                        cars.remove(c)

            if not start_ready:
                # 绘制准备种植植物提示
                if -1 < index_prepare_tip_image < 3 and cars_temp[0].rect.right == L + 4:
                    screen.blit(prepare_tip_images[index_prepare_tip_image], prepare_tip_rect)
                if index_prepare_tip_image >= 3:
                    start_ready = True
                    if open_music:
                        pygame.mixer.music.unpause()
            else:
                if not open_menu and not gameover:
                    # 检测植物是否被僵尸攻击
                    for p in plants:
                        attack_zombies = pygame.sprite.Group()
                        for z in zombies:
                           if (z.rect.centery == p.rect.centery - 25) and not z.die:
                               attack_zombies.add(z)
                        num_attack = pygame.sprite.spritecollide(p,attack_zombies,False,pygame.sprite.collide_mask)
                        for i in attack_zombies:
                            attack_zombies.remove(i)
                        if num_attack:
                            p.attacked = True
                            p.num_az = len(num_attack)
                        else:
                            p.attacked = False
                            p.num_az = 0

                    # 检测僵尸是否攻击植物
                    for z in zombies:
                        attacked_plants = pygame.sprite.Group()
                        for p in plants:
                            if (z.rect.centery == p.rect.centery - 25):
                                attacked_plants.add(p)
                        attack = pygame.sprite.spritecollide(z,attacked_plants,False,pygame.sprite.collide_mask)
                        for i in attacked_plants:
                            attacked_plants.remove(i)
                        if attack:
                            if not z.attack and not z.willdie:
                                z.attack = True
                                z.rect.left -= 10
                                if z.index == 1 or z.index == 4:
                                    z.images = z.za_images
                                    z.index_image = z.index_za_image
                                    z.num_image = z.num_za_image
                                    z.mask = z.za_mask
                                if (z.index == 2 or z.index == 3) and z.hat:
                                    z.images = z.za_images
                                    z.index_image = z.index_za_image
                                    z.num_image = z.num_za_image
                                    z.mask = z.za_mask
                                if (z.index == 2 or z.index == 3) and not z.hat:
                                    z.images = z.hza_images
                                    z.index_image = z.index_hza_image
                                    z.num_image = z.num_hza_image
                                    z.mask = z.hza_mask
                            if not z.attack and z.willdie:
                                z.attack = True
                                z.rect.left -= 10
                                z.images = z.zlha_images
                                z.index_image = z.index_zlha_image
                                z.num_image = z.num_zlha_image
                                z.mask = z.zlha_mask
                        else:
                            if z.attack and not z.willdie:
                                z.attack = False
                                if z.index == 1 or z.index == 4:
                                    z.images = z.oz_images
                                    z.index_image = z.index_oz_image
                                    z.num_image = z.num_oz_image
                                    z.mask = z.oz_mask
                                if (z.index == 2 or z.index == 3) and z.hat:
                                    z.images = z.oz_images
                                    z.index_image = z.index_oz_image
                                    z.num_image = z.num_oz_image
                                    z.mask = z.oz_mask
                                if (z.index == 2 or z.index == 3) and not z.hat:
                                    z.images = z.hoz_images
                                    z.index_image = z.index_hoz_image
                                    z.num_image = z.num_hoz_image
                                    z.mask = z.hoz_mask
                            if z.attack and z.willdie:
                                z.attack = False
                                z.images = z.zlh_images
                                z.index_image = z.index_zlh_image
                                z.num_image = z.num_zlh_image
                                z.mask = z.zlh_mask

                    # 检测僵尸是否被弹丸攻击
                    for z in zombies:
                        shoot_bullets = pygame.sprite.Group()
                        for b in bullets:
                            if b.shoot:
                                shoot_bullets.add(b)
                        attack_bullets = []
                        if not z.die:
                            attack_bullets = pygame.sprite.spritecollide(z, shoot_bullets, False, pygame.sprite.collide_mask)
                        for i in shoot_bullets:
                            shoot_bullets.remove(i)
                        for ab in attack_bullets:
                            if open_sound:
                                hit_sound.play()
                            if ab.is_bullet:
                                z.blood -= 1
                            else:
                                z.blood -= 2
                            ab.reset()
                            if (z.blood == 11 or z.blood == 10) and (z.index == 2 or z.index == 3):
                                if z.hat:
                                    z.hat = False
                                    if z.attack:
                                        z.images = z.hza_images
                                        z.index_image = z.index_hza_image
                                        z.num_image = z.num_hza_image
                                        z.mask = z.hza_mask
                                    else:
                                        z.images = z.hoz_images
                                        z.index_image = z.index_hoz_image
                                        z.num_image = z.num_hoz_image
                                        z.mask = z.hoz_mask

                            if (z.blood == 2 or z.blood == 1) and not z.willdie:
                                z.willdie = True
                                z.zh_rect.centerx,z.zh_rect.centery = z.rect.centerx + 50,z.rect.centery - 20
                                if z.attack:
                                    z.images = z.zlha_images
                                    z.index_image = z.index_zlha_image
                                    z.num_image = z.num_zlha_image
                                    z.mask = z.zlha_mask
                                if not z.attack:
                                    z.images = z.zlh_images
                                    z.index_image = z.index_zlh_image
                                    z.num_image = z.num_zlh_image
                                    z.mask = z.zlh_mask
                            if z.blood <= 0:
                                z.die = True
                                z.zd_rect = z.rect

                    # 检测僵尸是否与小车碰撞
                    for z in zombies:
                        check_cars = pygame.sprite.Group()
                        for c in cars:
                            if c.rect.right <= width and (c.rect.centery - 25 == z.rect.centery + 25):
                                check_cars.add(c)
                        if not z.die:
                            collide_cars = pygame.sprite.spritecollide(z,check_cars,False,pygame.sprite.collide_mask)
                        for i in check_cars:
                            check_cars.remove(i)
                        for cc in collide_cars:
                            cc.active = True
                        if collide_cars:
                            z.die = True
                            z.zd_rect = z.rect

                    # 将僵尸从上往下排序
                    order_zombies = []
                    for z in zombies:
                        order_zombies.append(z)
                    num = len(order_zombies)
                    for i in range(num):
                        index_top = i
                        zombie_top = order_zombies[i]
                        for j in range(i+1,num):
                            if zombie_top.rect.centery > order_zombies[j].rect.centery:
                                index_top = j
                                zombie_top = order_zombies[j]
                        order_zombies[index_top] = order_zombies[i]
                        order_zombies[i] = zombie_top

                    # 检测弹丸是否穿过火炬
                    for b in bullets:
                        if b.shoot:
                            if b.is_bullet:
                                through = pygame.sprite.spritecollide(b, torchwoods, False, pygame.sprite.collide_mask)
                            else:
                                through = True
                            if through:
                                b.is_bullet = False
                                b.mask = b.firebullet_mask
                            else:
                                b.is_bullet = True
                                b.mask = b.bullet_mask

                    # 检测僵尸是否进入房子（游戏结束）
                    for z in zombies:
                        if z.rect.right < 0 and not z.die:
                            gameover = True
                            z.rect.bottom = 400
                            z.get_win = True
                    if gameover:
                        for z in zombies:
                            if z.rect.left < 0 and not z.get_win:
                                z.rect.centerx = L

                # 绘制植物
                for p in plants:
                    screen.blit(plantshadow, (p.rect.left + p.shadow_rectx, p.rect.top + p.shadow_recty))
                    screen.blit(p.images[p.index_image], p.rect)

                # 绘制僵尸
                for z in order_zombies:
                    if not z.die:
                        if delay_1 == 5 and not z.attack:
                            if not open_menu and not gameover:
                                z.move()
                        screen.blit(z.images[z.index_image], z.rect)
                    else:
                        if (z.index_zd_image < z.num_zd_image + 8):
                            index2 = z.index_zd_image
                            if z.index_zd_image >= z.num_zd_image:
                                index2 = z.num_zd_image - 1
                            screen.blit(z.zd_images[index2], z.zd_rect)
                        else:
                            if z.index == 4:
                                zombies.remove(z)
                            else:
                                z.reset()
                    if z.willdie and (z.index_zh_image < z.num_zh_image + 10):
                        index1 = z.index_zh_image
                        if z.index_zh_image >= z.num_zh_image:
                            index1 = z.num_zh_image - 1
                        screen.blit(z.zh_images[index1], z.zh_rect)

                # 绘制弹丸
                for b in bullets:
                    if b.shoot:
                        if not open_menu and not gameover:
                            b.move()
                        if b.is_bullet:
                            screen.blit(b.bullet_image, b.rect)
                        else:
                            screen.blit(b.firebullet_images[b.index_image], b.rect)

                # 绘制拖拽的植物图像
                if not gameover:
                    if select == 1 and (sun_num >= pos_price):
                        mouse_pos = pygame.mouse.get_pos()
                        pos_rect.center = mouse_pos
                        screen.blit(pos_image, pos_rect)
                        if (pos_rect.centerx < L or pos_rect.centerx > R or pos_rect.centery < T or pos_rect.centery > B):
                            outborder = True
                        else:
                            outborder = False

                # 绘制阳光
                for s in suns:
                    if s.is_supply:
                        if not open_menu and not gameover:
                            if s.gather:
                                s.move3()
                            else:
                                s.move1()
                        screen.blit(s.images[s.index_image], s.rect1)
                    else:
                        if not open_menu and not gameover:
                            if s.gather:
                                s.move3()
                            else:
                                s.move2()
                        screen.blit(s.images[s.index_image], s.rect2)
                    if s.get_position:
                        suns.remove(s)
                        sun_num += 25

                # 绘制僵尸大波袭来warn
                if large_warn_time >= 0 and large_coming:
                    screen.blit(largewave_image, largewave_rect)

                # 绘制游戏结束画面
                if open_quit_window:
                    screen.blit(quit_window_image, quit_window_rect)
                    screen.blit(quit_image, quit_rect)
                elif bg_rect.left == 0:
                    pygame.mixer.music.stop()
                    screen.blit(zombiewon_image, zombiewon_rect)
                    if open_sound and not play_gameover_sound:
                        gameover_sound.play()
                        play_gameover_sound = True

            # 绘制阳光数量
            if not gameover:
                sun_num_text = sun_num_font.render(str(sun_num), True, COLOR)
                sun_num_rect = sun_num_text.get_rect()
                sun_num_rect.centerx, sun_num_rect.centery = 79, 73
                if seedbank.position:
                    screen.blit(sun_num_text, sun_num_rect)

        # 绘制菜单界面
        if not gameover:
            if start_ready:
                screen.blit(button_image, button_rect)
            if open_menu:
                screen.blit(menu_image, menu_rect)
                if start_ready:
                    screen.blit(quitgame_image, quitgame_rect)
                screen.blit(resume_image, resume_rect)
                screen.blit(check_box_image, check_box_rect1)
                screen.blit(check_box_image, check_box_rect2)
                if open_sound:
                    screen.blit(tick_image, tick_rect1)
                if open_music:
                    screen.blit(tick_image, tick_rect2)


        # 图片索引值、摆动帧率
        if not open_menu and start:
            if not gameover:
                for p in plants:
                    if delay_1 == 5:
                        p.index_image += 1
                    if p.index_image == p.num_image:
                        p.index_image = 0
                for pr in products:
                    if delay_1 == 5:
                        pr.index_image += 1
                    if pr.index_image == pr.num_image:
                        pr.index_image = 0
            for z in zombies:
                if not gameover or z.get_win:
                    if z.willdie:
                        if delay_1 == 5 and (z.index_zh_image < z.num_zh_image + 10):
                            z.index_zh_image += 1
                    if z.die:
                        if delay_2 == 8 and (z.index_zd_image < z.num_zd_image + 8):
                            z.index_zd_image += 1
                    if delay_1 == 5:
                        z.index_image += 1
                    if z.index_image == z.num_image:
                        z.index_image = 0
            delay_1 -= 1
            delay_2 -= 1
            if delay_1 == 0:
                delay_1 = 5
            if delay_2 == 0:
                delay_2 = 8

        if not start_ready and start and cars_temp[0].rect.right == L + 4:
            delay_3 -= 1
            if delay_3 == 0:
                delay_3 = 50
            if delay_3 == 50:
                index_prepare_tip_image += 1


        pygame.display.flip()
        clock.tick(60)   # 游戏帧率


if  __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()