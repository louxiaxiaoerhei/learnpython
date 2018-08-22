import pygame

# 自定义一个子弹类
class PlaneBullet(object):

    def __init__(self):
        # 图片
        self.img = pygame.image.load("res/bullet_10.png")
        # 获取图片矩形
        self.img_rect = self.img.get_rect()
        # 设置速度
        self.speed = 3
        # 是否发射
        self.is_shot = False

    # 向上移动
    def move_up(self):
        self.img_rect.move_ip(0, -self.speed)
        # 判断临界值 设置状态
        if self.img_rect[1] <= -self.img_rect[3]:
            self.is_shot = False