from hm_common import *
import pygame, sys, random

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


# 创建一个游戏窗口类 管理整个游戏
class GameWindow(object):

    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 创建游戏窗口
        # set_mode([窗口的宽度, 窗口的高度]) 单位均是像素
        self.window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        # 加载本地图片
        ico_img = pygame.image.load("res/app.ico")

        # 设置游戏窗口的icon
        pygame.display.set_icon(ico_img)

        # 设置游戏窗口的文字
        pygame.display.set_caption("飞机大战")

        # 创建地图对象
        self.map = GameMap()

    # 1.处理各种矩形坐标移动
    def __action(self):
        self.map.move_down()

    # 2.根据矩形坐标，重新对元素进行绘制
    def __draw(self):
        # 添加图片
        self.window.blit(self.map.img_1, (0, self.map.img1_y))
        self.window.blit(self.map.img_2, (0, self.map.img2_y))

    # 3.处理窗口中的监听事件
    def __event(self):
        # 监听所有的事件
        event_list = pygame.event.get()
        # 循环遍历所有事件
        for event in event_list:
            # 判断是否是鼠标点击关闭窗口
            if event.type == pygame.QUIT:
                self.__game_over()

            # 监听键盘点击事件
            if event.type == pygame.KEYDOWN:
                # 判断具体的按键按下
                if event.key == pygame.K_ESCAPE:
                    self.__game_over()
                # 空格
                if event.key == pygame.K_SPACE:
                    print("biubiubiu~~~")
        # 监听键盘长按事件(每个位置代表的是一个按键的状态 0 整除 1 按下)
        # 返回一个元组(0, 0, 0, 0)
        keys_pressed = pygame.key.get_pressed()
        # 上
        if keys_pressed[pygame.K_UP]:
            print("上")
        # 下
        elif keys_pressed[pygame.K_DOWN]:
            print("下")
        # 左
        if keys_pressed[pygame.K_LEFT]:
            print("左")
        # 右
        elif keys_pressed[pygame.K_RIGHT]:
            print("右")

    # 4.刷新窗口
    def __update(self):
        pygame.display.update()

    # 停止游戏
    def __game_over(self):
        # 停止pygame
        pygame.quit()
        # 退出游戏
        sys.exit()

    # 启动程序
    def run(self):
        while True:
            self.__action()
            self.__draw()
            self.__event()
            self.__update()

# 主函数
def main():
    # 创建对象
    game_window = GameWindow()
    game_window.run()


if __name__ == '__main__':
    main()
