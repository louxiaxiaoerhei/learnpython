
# # 自定义英雄类
# class Hero(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __del__(self):
#         print("再见")
#         # # 惨叫一声
#         # # 屏幕变成灰色
#         # # 开启秒数
#         # wk = Hero()
#
# # 对象
# wk1 = Hero('悟空')
# del wk1
#
# input()


# 自定义英雄类
class Hero(object):

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("再见")


# 对象
wk1 = Hero('悟空')
wk2 = wk1
wk3 = wk1

del wk1
# del wk2
# del wk3
#
# input()

"""
是否只要执行了 del 对象名 就会执行其类中的del方法?
待内存地址的引用计数为0的时候才会执行
"""
