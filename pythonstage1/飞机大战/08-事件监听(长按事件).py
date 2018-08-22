# 导入模块
import pygame, sys
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

# 加载本地图片
plane_img = pygame.image.load("res/hero2.png")
# 获取图片矩形
plane_img_rect = plane_img.get_rect()
# <rect(0, 0, 120, 78)>
# x, y, w, h
# 获取图片矩形各个值  -> 通过下标索引plane_img_rect[2]
print(plane_img_rect)

while True:
    # 监听所有的事件
    event_list = pygame.event.get()
    # 循环遍历所有事件
    for event in event_list:
        # 判断是否是鼠标点击关闭窗口
        if event.type == pygame.QUIT:
            # 停止pygame
            pygame.quit()
            # 退出游戏
            sys.exit()

        # 监听键盘点击事件
        if event.type == pygame.KEYDOWN:
            # 判断具体的按键按下
            if event.key == pygame.K_ESCAPE:
                # 停止pygame
                pygame.quit()
                # 退出游戏
                sys.exit()
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

    # 添加图片到游戏窗口中
    window.blit(bg_img, (0, 0))
    # 添加图片到游戏窗口中
    window.blit(plane_img, (plane_img_rect[0], plane_img_rect[1]))
    # 刷新游戏窗口
    pygame.display.update()

    #修改 x坐标和y坐标
    # move_ip(每次增加 或者减小的像素, 每次增加 或者减小的像素)
    plane_img_rect.move_ip(1, 1)