import pygame, plane_bullet
from hm_common import *

# 自定义一个英雄飞机类
class HeroPlane(object):

    def __init__(self):
        # 图片
        self.img = pygame.image.load("res/hero2.png")
        # 获取图片矩形
        self.img_rect = self.img.get_rect()
        # 速度
        self.speed = 2
        # 设置飞机的初始位置
        self.img_rect[0] = (WINDOW_WIDTH - self.img_rect[2]) / 2
        self.img_rect[1] = WINDOW_HEIGHT - self.img_rect[3] - 20
        # 子弹弹夹
        self.bullet_list = [plane_bullet.PlaneBullet() for _ in range(6)]

    # 上下左右
    def move_up(self):
        # 边缘检测
        if self.img_rect[1] > 0:
            self.img_rect.move_ip(0, -self.speed)

    def move_down(self):
        # 边缘检测
        if self.img_rect[1] < WINDOW_HEIGHT - self.img_rect[3]:
            self.img_rect.move_ip(0, self.speed)

    def move_left(self):
        # 边缘检测
        if self.img_rect[0] > 0:
            self.img_rect.move_ip(-self.speed, 0)

    def move_right(self):
        # 边缘检测
        if self.img_rect[0] < WINDOW_WIDTH - self.img_rect[2]:
            self.img_rect.move_ip(self.speed, 0)

    # 发射子弹
    def shoot(self):
        # 循环遍历所有子弹
        for bullet in self.bullet_list:
            # 判断状态
            if not bullet.is_shot:
                # 设置为发射
                bullet.is_shot = True
                # 设置子弹的坐标 x y
                bullet.img_rect[0] = self.img_rect[0] + (self.img_rect[2] - bullet.img_rect[2]) / 2
                bullet.img_rect[1] = self.img_rect[1] - bullet.img_rect[3]
                break