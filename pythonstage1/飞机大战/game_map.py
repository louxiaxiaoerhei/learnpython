import random, pygame
from hm_common import *

# 自定义游戏地图类
class GameMap(object):

    def __init__(self):
        # 随机数
        self.num = random.randint(1, 5)
        # 图片 * 2
        self.img_1 = pygame.image.load("res/img_bg_level_%d.jpg" % self.num)
        self.img_2 = pygame.image.load("res/img_bg_level_%d.jpg" % self.num)
        self._reset()
        # 速度
        self.speed = 1

    # 向下
    def move_down(self):
        # 判断临界点
        if self.img1_y >= 0:
            # 设置y轴坐标
            self._reset()

        self.img1_y += self.speed
        self.img2_y += self.speed

    # 抽取
    def _reset(self):
        # 设置y轴坐标
        self.img1_y = -WINDOW_HEIGHT
        self.img2_y = 0