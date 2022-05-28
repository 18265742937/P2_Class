import pygame, sys, time, random
from pygame.locals import *

class Snake():
    def __init__(self):
        """初始化方法"""
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.playSurface = pygame.display.set_mode((640, 480))     #    设置界面
        pygame.display.set_caption("贪吃蛇游戏")                   # 设置标题
        self.redColor = pygame.Color(255, 0, 0)                  # 红色 方块
        self.blackColor = pygame.Color(0, 0, 0)                   # 背景颜色
        self.whiteColor = pygame.Color(255, 255, 255)               # 蛇本体颜色
        self.greyColor = pygame.Color(150, 150, 150)
        self.snakePosition = [100, 100]                               #   蛇头坐标
        self.snakeSegments = [[100, 100], [80, 100], [60, 100]]                  #   蛇身体
        self.foodPosition = [300, 300]                        #    食物坐标   食物是 20*20 小方块
        self.food = 1                          # 有1个食物
        self.direction = 'right'                           # 默认方向
        self.changeDirection = self.direction                    # 记录改变的方向
        self.speed = 5     # 速度
        self.score = 0
        self.flag = True   # 循环标志位
        self.btn1 = [100, 400, 100, 50]     #  按钮坐标x ,y, w,h
        self.btn2 = [440, 400, 100, 50]

    def addButton(self, txt, pos, ic, ac):
        self.mouse = pygame.mouse.get_pos()
        #     if x + w > self.mouse[0] > x and y + h > self.mouse[1] > y:
        if pos[0] + pos[2] > self.mouse[0] > pos[0] and pos[1] + pos[3] > self.mouse[1] > pos[1]:
            pygame.draw.rect(self.playSurface, ac, pos)
        else:
            pygame.draw.rect(self.playSurface, ic, pos)
        smallText = pygame.font.Font(r'C:\CODE\P2_CLASS\Python\LCP_VipCode__Pygame\U3\第17课-U2C8\STXINGKA.TTF', 20)
        textSurf = smallText.render(txt, True, [0, 0, 0])
        textRect = textSurf.get_rect()
        #     textRect.center = ((x+(w/2)), (y+(h/2)))
        textRect.center = ((pos[0] + (pos[2] / 2)), (pos[1] + (pos[3] / 2)))
        self.playSurface.blit(textSurf, textRect)

    def writeFont(self,type,size,txt,color,x,y):
        """写文字"""
        font = pygame.font.Font(type, size)   #  字体
        font =font.render(txt, True, color)   # 显示字体
        rect = font.get_rect()      # 获得矩形对象

        rect.x,rect.y = x,y  # 设置位置
        self.playSurface.blit(font,rect)         # 刷新添加

    def fraction(self):
        """管理分数"""
        self.writeFont(r"C:\CODE\P2_CLASS\Python\LCP_VipCode__Pygame\U3\第17课-U2C8\STXINGKA.TTF",25,"分数:"+str(self.score),self.greyColor,0,0)

    def keyPressEvent(self,event):
        """键盘事件"""
        if event.key == K_RIGHT or event.key == K_d:        # 小键盘 或者键盘上下左右键进行操作移动
            self.changeDirection = 'right'
        if event.key == K_LEFT or event.key == K_a:
            self.changeDirection = 'left'
        if event.key == K_UP or event.key == K_w:
            self.changeDirection = 'up'
        if event.key == K_DOWN or event.key == K_s:
            self.changeDirection = 'down'

    def gameOver(self):
        """ 游戏结束函数   """
        self.wscore()     #   写分数
        self.flag = False   # 循环标志位

    def wscore(self):
        """写文件"""
        with open("top5.conf", "a", encoding="utf8") as f:
            f.write(str(self.score) + "\n")

    def rscore(self):
        """读文件"""
        with open("top5.conf", "r", encoding="utf8") as f:
            slist = f.readlines()
        nslist = [0,0,0,0,0]
        for x in slist:
            x = x[:-1]  # 去掉\n
            x = int(x)
            nslist.append(x)
        self.writeFont(r"C:\CODE\P2_CLASS\Python\LCP_VipCode__Pygame\U3\第17课-U2C8\STXINGKA.TTF",72,"排行榜","red",220,0)
        nslist.sort(reverse=True)
        print(nslist)
        for x in range(5):
            self.writeFont(r"C:\CODE\P2_CLASS\Python\LCP_VipCode__Pygame\U3\第17课-U2C8\STXINGKA.TTF", 45, "第%s名:%s分"%(x+1,nslist[x]), "orange", 180, 100+x*55)

    def move(self):
        """确定键盘 移动事件"""
        if self.changeDirection == 'right' and self.direction != 'left':      #   移动   防止 上下调转方向   左右调转方向
            self.direction = self.changeDirection
        if self.changeDirection == 'left' and self.direction != 'right':
            self.direction = self.changeDirection
        if self.changeDirection == 'up' and self.direction != 'down':
            self.direction = self.changeDirection
        if self.changeDirection == 'down' and self.direction != 'up':
            self.direction = self.changeDirection
        if self.direction == 'right':                          #        控制蛇头移动
            self.snakePosition[0] += 20                    #  每次20
        if self.direction == 'left':
            self.snakePosition[0] -= 20
        if self.direction == 'up':
            self.snakePosition[1] -= 20
        if self.direction == 'down':
            self.snakePosition[1] += 20

    def playMusic(self):
        """ 播放音乐"""
        music = pygame.mixer.music   #  创建音乐播放器
        music.load("./success.mp3")   # 加载音乐
        music.play()   # 播放音乐

    def main(self):
        """主程序"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:       # 退出
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    self.keyPressEvent(event)     #键盘事件
                if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按下
                    x, y = pygame.mouse.get_pos()
                    if self.btn1[0] + self.btn1[2] > x > self.btn1[0]:  # 继续游戏
                        if self.btn1[1] + self.btn1[3] > y > self.btn1[1]:
                            game = Snake()
                            game.main()

                    if self.btn2[0] + self.btn2[2] > x > self.btn2[0]:   #   按退出
                        if self.btn2[1] + self.btn2[3] > y > self.btn2[1]:
                            pygame.quit()
                            sys.exit()

            if self.flag:
                self.move()    #确定方向 移动

                self.snakeSegments.insert(0, list(self.snakePosition))    #   蛇身体  在前边插入坐标  蛇头坐标为了前进
                # 蛇头横坐标  等于食物 纵坐标          并且           蛇头纵坐标等于 食物纵坐标
                if self.snakePosition[0] == self.foodPosition[0] and self.snakePosition[1] == self.foodPosition[1]:
                    self.score += 5
                    self.playMusic()    # 音效
                    self.food = 0    #  删除食物     记录界面没有食物了
                    self.speed += 1
                else:
                    self.snakeSegments.pop()      # 蛇身体删除最后1个          没吃到往前走
                if self.food == 0:     # 没有食物   随机生成   食物
                    while True:
                        x = random.randint(1, 31)  # 界面640宽     界面大小决定的
                        y = random.randint(1, 23)  # 界面480高
                        self.foodPosition = [int(x * 20), int(y * 20)]
                        if self.foodPosition not in self.snakeSegments:
                            break
                self.food = 1                #  食物+1   代表有食物了

                self.playSurface.fill(self.blackColor)                  # 界面刷新

                for position in self.snakeSegments:            #  从身体列表里找出身体的小坐标
                    #  矩形对象设置位置    界面，颜色，（x,y,w,h）
                    pygame.draw.rect(self.playSurface, self.whiteColor, Rect(position[0], position[1], 20, 20))
                pygame.draw.rect(self.playSurface, self.redColor, Rect(self.foodPosition[0], self.foodPosition[1], 20, 20))      #  界面添加 食物

                if self.snakePosition[0] > 620 or self.snakePosition[0] < 0:   #   碰到左右边距就退出
                    self.gameOver()
                if self.snakePosition[1] > 460 or self.snakePosition[1] < 0:   # 碰到上下边距也退出
                    self.gameOver()
                #   循环 判断是不是 头撞到了身体
                # for snakeBody in self.snakeSegments[1:]:
                #     if self.snakePosition[0] == snakeBody[0] and self.snakePosition[1] == snakeBody[1]:
                #         self.gameOver()
                if self.snakePosition in self.snakeSegments[1:]:  # 判断头列表 在 除头以外身体大列表中代表撞到了身体
                    self.gameOver()

                self.fraction()    #   调用分数
            else:
                self.playSurface.fill([255, 255, 255])
                self.addButton("继续游戏", self.btn1, "LightBLue", "cyan")
                self.addButton("退出游戏", self.btn2, "LightBLue", "cyan")
                self.rscore()

            pygame.display.update()               #   刷新
            self.fpsClock.tick(self.speed)             # 控制帧数    速度

if __name__ == '__main__':
    game = Snake()
    game.main()