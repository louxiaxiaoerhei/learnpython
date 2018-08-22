# 导入模块
import pygame
# 初始化pygame
pygame.init()
# 创建游戏窗口
# set_mode([窗口的宽度, 窗口的高度]) 单位均是像素
window = pygame.display.set_mode([512, 768])
# 加载本地图片
ico_img = pygame.image.load("res/app.ico")

# 设置游戏窗口的icon
pygame.display.set_icon(ico_img)

# 设置游戏窗口的文字
pygame.display.set_caption("飞机大战")

# 加载本地图片
bg_img = pygame.image.load("res/img_bg_level_1.jpg")
# 添加图片到游戏窗口中
window.blit(bg_img, (0, 0))
# 刷新游戏窗口
pygame.display.update()

input()