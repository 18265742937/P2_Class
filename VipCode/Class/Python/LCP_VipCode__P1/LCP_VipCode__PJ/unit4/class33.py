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

a = player()
a.attribute("小明", 100, 5, 0)
b = player()
b.attribute("小光", 100, 5, 0)
a.hit(b)
