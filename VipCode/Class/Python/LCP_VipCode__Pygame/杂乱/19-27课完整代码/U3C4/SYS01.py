# ----------------------类  继承------------------------------
#某个类直接具备另一个类的能力（属性和方法)   和现实生活的继承一样
class People():
    def eat(self):
        print("吃饭")

class Chinese(People):
    pass

w = Chinese()
w.eat()

#  ---------------- 重写 ------------------------------
# 当子类实现一个和父类同名的方法时，叫做 重写父类方法
# 子类重写了父类方法，子类再调用该方法将不会执行父类的处理

class People():
    def eat(self):
        print("吃饭")

    def play(self):
        print("球")

class Chinese(People):
    def play(self):
        print("乒乓球")

bc = Chinese()
bc.eat()
bc.play()




