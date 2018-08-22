from hm_common import *
import pygame
# 创建一个游戏窗口类 管理整个游戏
class GameWindow(object):

    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 创建游戏窗口
        # set_mode([窗口的宽度, 窗口的高度]) 单位均是像素
        window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        # 加载本地图片
        ico_img = pygame.image.load("res/app.ico")

        # 设置游戏窗口的icon
        pygame.display.set_icon(ico_img)

        # 设置游戏窗口的文字
        pygame.display.set_caption("飞机大战")

    # 1.处理各种矩形坐标移动
    def __action(self):
        pass

    # 2.根据矩形坐标，重新对元素进行绘制
    def __draw(self):
        pass

    # 3.处理窗口中的监听事件
    def __event(self):
        pass

    # 4.刷新窗口
    def __update(self):
        pygame.display.update()

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
