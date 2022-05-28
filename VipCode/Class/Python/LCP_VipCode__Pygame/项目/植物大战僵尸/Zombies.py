import pygame
from random import *


class ZombiesImages():
    def __init__(self):
        self.oz1_images = []  # 原始僵尸1图片
        self.oz1_images.extend([ \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_0.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_11.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_12.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_13.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_14.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_15.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_16.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_17.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_18.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_19.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_20.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie_21.png").convert_alpha() \
            ])

        self.oz2_images = []  # 原始僵尸2图片
        self.oz2_images.extend([ \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_11.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_12.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_13.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_14.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_15.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_16.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_17.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_18.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_19.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_20.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_21.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_22.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_23.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_24.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_25.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_26.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_27.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_28.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_29.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_30.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/Zombie2_31.png").convert_alpha() \
            ])

        self.oza_images = []  # 原始僵尸攻击图片
        self.oza_images.extend([ \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_0.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_11.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_12.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_13.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_14.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_15.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_16.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_17.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_18.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_19.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieAttack_20.png").convert_alpha() \
            ])

        self.cz_images = []  # 帽子僵尸图片
        self.cz_images.extend([ \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie11.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie12.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie13.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie14.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie15.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie16.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie17.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie18.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie19.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie20.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombie21.png").convert_alpha() \
            ])

        self.cza_images = []  # 帽子僵尸攻击图片
        self.cza_images.extend([ \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/ConeheadZombie/ConeheadZombieAttack11.png").convert_alpha() \
            ])

        self.bz_images = []  # 铁桶僵尸图片
        self.bz_images.extend([ \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie11.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie12.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie13.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie14.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombie15.png").convert_alpha() \
            ])

        self.bza_images = []  # 铁桶僵尸攻击图片
        self.bza_images.extend([ \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/BucketheadZombie/BucketheadZombieAttack11.png").convert_alpha() \
            ])

        self.fz_images = []  # 举旗僵尸图片
        self.fz_images.extend([ \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie11.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombie12.png").convert_alpha() \
            ])

        self.fza_images = []  # 举旗僵尸攻击图片
        self.fza_images.extend([ \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieAttack11.png").convert_alpha() \
            ])

        self.fzlh_images = []  # 举旗僵尸没有头图片
        self.fzlh_images.extend([ \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead11.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHead12.png").convert_alpha() \
            ])

        self.zlh_images = []  # 原始僵尸没有头图片
        self.zlh_images.extend([ \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead11.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead12.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead13.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead14.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead15.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead16.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead17.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHead18.png").convert_alpha() \
            ])

        self.zh_images = []  # 僵尸的头图片
        self.zh_images.extend([ \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead11.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieHead12.png").convert_alpha() \
            ])

        self.zlha_images = []  # 原始僵尸没有头攻击图片
        self.zlha_images.extend([ \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieLostHeadAttack11.png").convert_alpha() \
            ])

        self.fzlha_images = []  # 举旗僵尸没有头攻击图片
        self.fzlha_images.extend([ \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack10.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/FlagZombie/FlagZombieLostHeadAttack11.png").convert_alpha() \
            ])

        self.zd_images = []  # 僵尸死亡图片
        self.zd_images.extend([ \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie1.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie2.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie3.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie4.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie5.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie6.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie7.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie8.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie9.png").convert_alpha(), \
            pygame.image.load("photo/Zombies/OrdinaryZombie/ZombieDie10.png").convert_alpha() \
            ])


class OrdinaryZombie(pygame.sprite.Sprite):
    def __init__(self,x,Y,images):
        pygame.sprite.Sprite.__init__(self)

        self.x,self.Y = x,Y

        self.oz_images = images.oz1_images  # 原始僵尸1图片
        self.index_oz_image = 0
        self.num_oz_image = 22
        self.oz_mask = pygame.mask.from_surface(self.oz_images[11])

        self.za_images = images.oza_images  # 原始僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 21
        self.za_mask = pygame.mask.from_surface(self.za_images[10])

        self.zlh_images = images.zlh_images  # 原始僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 18
        self.zlh_mask = pygame.mask.from_surface(self.zlh_images[9])

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = self.zh_images[0].get_rect()

        self.zlha_images = images.zlha_images  # 僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11
        self.zlha_mask = pygame.mask.from_surface(self.zlha_images[5])

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.zd_rect = self.zd_images[0].get_rect()

        self.rect = self.oz_images[0].get_rect()
        self.rect.left, self.rect.centery = randint(self.x, 2 * self.x), self.Y[randint(0, 4)] - 25
        self.index = 1
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 1
        self.blood = 10
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        self.mask = self.oz_mask

    def move(self):
        self.rect.left -= self.speed

    def reset(self):
        self.rect.left,self.rect.centery = randint(self.x, 2 * self.x), self.Y[randint(0, 4)] - 25
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.blood = 10
        self.attack = False
        self.willdie = False
        self.die = False
        self.mask = self.oz_mask


class ConeheadZombie(pygame.sprite.Sprite):
    def __init__(self,x,Y,images):
        pygame.sprite.Sprite.__init__(self)

        self.x,self.Y = x,Y

        self.oz_images = images.cz_images  # 帽子僵尸图片
        self.index_oz_image = 0
        self.num_oz_image = 21
        self.oz_mask = pygame.mask.from_surface(self.oz_images[10])

        self.hoz_images = images.oz1_images  # 原始僵尸1图片
        self.index_hoz_image = 0
        self.num_hoz_image = 22
        self.hoz_mask = pygame.mask.from_surface(self.hoz_images[11])

        self.za_images = images.cza_images  # 帽子僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 11
        self.za_mask = pygame.mask.from_surface(self.za_images[5])

        self.hza_images = images.oza_images  # 原始僵尸攻击图片
        self.index_hza_image = 0
        self.num_hza_image = 21
        self.hza_mask = pygame.mask.from_surface(self.hza_images[10])

        self.zlh_images = images.zlh_images  # 原始僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 18
        self.zlh_mask = pygame.mask.from_surface(self.zlh_images[9])

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = self.zh_images[0].get_rect()

        self.zlha_images = images.zlha_images  # 僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11
        self.zlha_mask = pygame.mask.from_surface(self.zlha_images[5])

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.zd_rect = self.zd_images[0].get_rect()

        self.rect = self.oz_images[0].get_rect()
        self.rect.left,self.rect.centery = randint(2 * self.x, 3 * self.x), self.Y[randint(0, 4)] - 25
        self.index = 2
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 1
        self.blood = 28
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        self.mask = self.oz_mask

    def move(self):
        self.rect.left -= self.speed

    def reset(self):
        self.rect.left, self.rect.centery = randint(2 * self.x, 3 * self.x), self.Y[randint(0, 4)] - 25
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.blood = 28
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        self.mask = self.oz_mask


class BucketheadZombie(pygame.sprite.Sprite):
    def __init__(self,x,Y,images):
        pygame.sprite.Sprite.__init__(self)

        self.x, self.Y = x, Y

        self.oz_images = images.bz_images  # 铁桶僵尸图片
        self.index_oz_image = 0
        self.num_oz_image = 15
        self.oz_mask = pygame.mask.from_surface(self.oz_images[7])

        self.hoz_images = images.oz2_images  # 原始僵尸2图片
        self.index_hoz_image = 0
        self.num_hoz_image = 31
        self.hoz_mask = pygame.mask.from_surface(self.hoz_images[15])

        self.za_images = images.bza_images  # 铁桶僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 11
        self.za_mask = pygame.mask.from_surface(self.za_images[5])

        self.hza_images = images.oza_images  # 原始僵尸攻击图片
        self.index_hza_image = 0
        self.num_hza_image = 21
        self.hza_mask = pygame.mask.from_surface(self.hza_images[10])

        self.zlh_images = images.zlh_images  # 原始僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 18
        self.zlh_mask = pygame.mask.from_surface(self.zlh_images[9])

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = self.zh_images[0].get_rect()

        self.zlha_images = images.zlha_images  # 僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11
        self.zlha_mask = pygame.mask.from_surface(self.zlha_images[5])

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.zd_rect = self.zd_images[0].get_rect()

        self.rect = self.oz_images[0].get_rect()
        self.rect.left,self.rect.centery = randint(3 * self.x, 4 * self.x), self.Y[randint(0, 4)] - 25
        self.index = 3
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 1
        self.blood = 64
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        self.mask = self.oz_mask

    def move(self):
        self.rect.left -= self.speed

    def reset(self):
        self.rect.left, self.rect.centery = randint(3 * self.x, 4 * self.x), self.Y[randint(0, 4)] - 25
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.blood = 64
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        self.mask = self.oz_mask


class FlagZombie(pygame.sprite.Sprite):
    def __init__(self,x,Y,images):
        pygame.sprite.Sprite.__init__(self)

        self.x,self.Y = x,Y

        self.oz_images = images.fz_images  # 举旗僵尸图片
        self.index_oz_image = 0
        self.num_oz_image = 12
        self.oz_mask = pygame.mask.from_surface(self.oz_images[6])

        self.za_images = images.fza_images  # 举旗僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 11
        self.za_mask = pygame.mask.from_surface(self.za_images[5])

        self.zlh_images = images.fzlh_images  # 举旗僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 12
        self.zlh_mask = pygame.mask.from_surface(self.zlh_images[6])

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = self.zh_images[0].get_rect()

        self.zlha_images = images.fzlha_images  # 举旗僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11
        self.zlha_mask = pygame.mask.from_surface(self.zlha_images[5])

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.zd_rect = self.zd_images[0].get_rect()

        self.rect = self.oz_images[0].get_rect()
        self.rect.left, self.rect.centery = self.x, self.Y[randint(0, 4)] - 25
        self.index = 4
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 1
        self.blood = 11
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        self.mask = self.oz_mask

    def move(self):
        self.rect.left -= self.speed