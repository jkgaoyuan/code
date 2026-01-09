import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print('游戏初始化')

        # 1 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3 调用私有方法，精灵和精灵组的创建
        self.__create_spritea()

    def __create_spritea(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        # bg2.rect.y = -bg2.rect.height   # 定义初始位置

        self.back_group = pygame.sprite.Group(bg1, bg2)

    def start_game(self):
        print('游戏开始...')

        while True:
            # 1 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2 事件监听
            self.__event_handler()
            # 3 碰撞检测
            self.__check_collide()
            # 4 更新/绘制精灵组
            self.__update_sprites()
            # 5 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()

plane_sprites.py部分

import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量(USEREVENT  是pygame提供的用户事件)
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):  # 第一个是模块的名称 第二个是类的名称
    """ 飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """ 游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1 调用父类方法实现精灵组的创建（image/rect/speed）
        super().__init__('./images/background.png')

        # 2 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1 调用父类的方法实现
        super().update()

        # 2 判断是否移出屏幕，如果移出屏幕， 将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height