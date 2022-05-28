
#----------------------- 重写 super----------------
#子类重写了父类方法，仍然想执行父类中的方法，则可以在类中使用super（）来调用方
class People():
    def __init__(self):
        self.name = "大头"

    def eat(self):
        print("吃饭")

    def play(self):
        print("球")

class Chinese(People):
    def __init__(self):  # 重写了父类的init方法
        super().__init__()     # 不写super就用不了a

    def play(self):
        #People.play(self)  # 调用已经被重写的方法       1
        #super(Chinese, self).play()  # 调用已经被重写的方法       2
        #super().play()  # 调用已经被重写的方法      3
        print("乒乓球")

        print(self.name)

bc = Chinese()
bc.eat()
bc.play()
