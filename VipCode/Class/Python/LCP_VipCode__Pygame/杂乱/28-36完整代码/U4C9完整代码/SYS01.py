import pygame, sys, random
from pygame.locals import *
class Digimon():
    def __init__(self):
        """初始化方法"""
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.playSurface = pygame.display.set_mode((600, 600)) #    设置界面
        self.background = pygame.image.load("./img/douluo.jpg")
        pygame.display.set_caption("choice") # 设置标题
        self.redColor = pygame.Color(255,0,0)  # 移动框框颜色
        self.listXY = [[32, 10], [165, 10], [298, 10], [431, 10], [32, 202], [165, 202], [298, 202], [431, 202], [32, 394], [165, 394], [298, 394], [431, 394]]
        self.index = 0      # 图片索引
        self.flag = False  # 标记位  没有开始游戏

    def playMusic(self):
        """ 播放音乐"""
        music = pygame.mixer.music   #  创建音乐播放器
        music.load("./img/music.wav")   # 加载音乐
        music.play()   # 播放音乐

    def keyPressEvent(self,event):
        """键盘事件"""
        if event.key == K_SPACE:        # 判断按下空格
            self.flag = True   # 开始游戏
            self.index = 0
            self.winning = random.randint(24,35)    # 随机范围

    def move(self):
        """抽奖"""
        pygame.draw.rect(self.playSurface, self.redColor,Rect(self.listXY[self.index % 12][0], self.listXY[self.index % 12][1], 135, 195), width=5)
        if self.index == self.winning:
            # 标记位不能继续游戏
            self.flag = False
        else:
            # 索引+1 卡片往后走
            self.index += 1

    def main(self):
        """主程序"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:       # 退出
                    pygame.quit()
                    sys.exit()
                #            键盘按下事件
                elif event.type == KEYDOWN and self.flag == False:    # 游戏没开始时候
                    self.keyPressEvent(event)     #键盘事件
            self.playSurface.blit(self.background, (0, 0))    # 背景图
            # 标记位
            if self.flag:
                # 调用播放音乐
                self.playMusic()
                # 调用移动方法
                self.move()
            else:
                pygame.draw.rect(self.playSurface, self.redColor, Rect(self.listXY[self.index % 12][0], self.listXY[self.index % 12][1], 135, 195), width=5)
            self.fpsClock.tick(20)             # 控制帧数    速度
            pygame.display.update()               #   刷新

if __name__ == '__main__':
    game = Digimon()
    game.main()

