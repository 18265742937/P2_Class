import random


class player():
    def attribute(self, name, blood, attack, defence):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.defence = defence
        print(self.name + '的血量为%d，攻击力为%d，防御力为%d。' %
              (self.blood, self.attack, self.defence))

    def hit(self, player2):
        num = self.attack - player2.defence
        player2.blood = player2.blood - num
        print(self.name + '对' + player2.name + '造成了%d点伤害，' % num +
              player2.name + '剩余的血量为%d。' % player2.blood)


    def equip_gun(self, gun):
        if gun == "DP28":
            self.attack = 50
        elif gun == "GROZA":
            self.attack = 45
        elif gun == "AWM":
            self.attack = 40
        print(self.name + "装备了%s,当前攻击力为%d" % (gun, self.attack))
    
    def equip_vest(self, vest):
        if vest == 3:
            self.defence = 30
        elif vest == 2:
            self.defence = 25
        elif vest == 1:
            self.defence = 20
        print(self.name + "装备了%d级头, 当前防御力为%d" % (vest, self.defence)) 
        
    def firstaid(self):
        self.blood += 20
        if self.blood > 100:
            self.blood = 100
        print(self.name + "使用了急救药, 当前血量为%d" % self.blood)


a = player()
a.attribute("小明", 100, 5, 0)
a.equip_gun("AWM")
a.equip_vest(3)
b = player()
b.attribute("小光", 100, 5, 0)
a.hit(b)


 
# a = player()
# a.attribute("小明", 100, 5, 0)
# b = player()
# b.attribute("小光", 100, 5, 0)
# a.hit(b)
