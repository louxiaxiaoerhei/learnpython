import pygame, random
from hm_common import *
# 自定义敌机类
class EnemyPlane(object):

    def __init__(self):
        # 随机数
        self.num = random.randint(1, 7)
        # 图片
        self.img = pygame.image.load("res/img-plane_%d.png" % self.num)
        # 获取图片矩形
        self.img_rect = self.img.get_rect()
        self.reset()

    # 向下移动
    def move_down(self):
        self.img_rect.move_ip(0, self.speed)
        # 临界值判断
        if self.img_rect[1] >= WINDOW_HEIGHT:
            self.reset()

    def reset(self):
        # 设置初始位置
        self.img_rect[0] = random.randint(0, WINDOW_WIDTH - self.img_rect[2])
        self.img_rect[1] = -self.img_rect[3]
        # 设置速度
        self.speed = random.randint(2, 3)

