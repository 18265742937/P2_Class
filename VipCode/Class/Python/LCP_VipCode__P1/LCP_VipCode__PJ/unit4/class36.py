import time


class Crops:
    def __init__(self, name, cost, price):
        self.name = name
        self.cost = cost
        self.price = price
        print("我是%s，本金%d，卖出%d金币" % (self.name, self.cost, self.price))

    def grow(self):
        print("%s正在生长……" % self.name)
        time.sleep(1)
        print("%s已经成熟，可卖出赚取%d金币" % (self.name, self.price))


class Farmer:
    def __init__(self, name, money):
        self.name = name
        self.money = money    #修改代码-----------------------------
        self.crop = 20  #修改代码--------------------------

    def plant(self):
        print("%s种下了蔬菜" % self.name)

    def sell(self):
        print("%s卖出了蔬菜" % self.name)

#开始------------------------------------------------------
    #添加买菜的方法
    def get_seeds(self):
        if self.money >= self.crop:
            self.money -= self.crop
            print("购买蔬菜成功!")
        else:
            print("金币不足购买失败!")
#结束-------------------------------------------------------


c1 = Crops("banana", 5, 10)
c1.grow()
f1 = Farmer("Bob", 100)
f1.plant()
f1.sell()
f1.get_seeds()  #添加代码---------------------------------------
