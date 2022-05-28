import pygame, sys
from pygame.locals import *

class App():
    def __init__(self):
        """初始化方法"""
        pygame.init()
        self.playSurface = pygame.display.set_mode((600, 600))     #    设置界面
        pygame.display.set_caption("Vipcode")                   # 设置标题
        self.imglist = ["奥特曼.jpg","斗罗大陆.jpg","漫威.jpg","神奇宝贝.jpg","精灵球.jpg"]
        self.index = 0       # 图片索引

    def keyPressEvent(self,event):
        """键盘事件"""
        # 按下字母d键 或者 键盘右键
        if event.key == K_RIGHT or event.key == K_d:
            self.index += 1
        # 按下字母a键 或者 键盘左键
        if event.key == K_LEFT or event.key == K_a:
            self.index -= 1

    def main(self):
        """主程序"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:       # 退出
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    #调用键盘事件
                    self.keyPressEvent(event)  # 键盘事件

            # 获取图片名字
            imgname = self.imglist[self.index%5]
            #加载图片
            self.img = pygame.image.load("img/"+imgname)
            # 绘制图像，并且规定位置
            self.playSurface.blit(self.img, [0,0])

            pygame.display.update()    #   刷新

if __name__ == '__main__':
    game = App()
    game.main()

