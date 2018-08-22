# 古法师傅类
class Master(object):

    def __init__(self):
        # 配方
        self.kongfu = "古法配方"

    def make_cake(self):
        print("制作古法煎饼果子")

    def dayandai(self):
        print("大烟袋")


# # 现代师傅类
# class School(object):
#
#     def __init__(self):
#         # 配方
#         self.kongfu = "现代配方"
#
#     def make_cake(self):
#         print("制作现代煎饼果子")
#
#     def xiaoyandai(self):
#         print("大烟袋")
#
#  # 自定义徒弟类
# # 格式: class 子类名(父类1, 父类2, ...):
# class Prentice(Master, School):
#     pass
#
#
# """
# 如果子类继承了多个父类 -> 多继承
#     - (方法)如果多个父类的名字相同(__init__ 和 make_cake)
#         - 会继承第一个父类的
#     - (方法)如果多个父类的名字不相同
#         - 那么会全部继承
#
# 为什么子类会继承第一个父类的属性?
#     - 如果多个父类的名字相同(__init__)
#     - 因为继承了第一个父类的init方法导致继承了第一个父类的属性
#
#
# """
# dm = Prentice()
# print(dm.kongfu)
# dm.make_cake()
# dm.dayandai()
# dm.xiaoyandai()