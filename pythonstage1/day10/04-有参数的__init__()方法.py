
"""
旺财 3 白色
藏獒 4 黑色
金毛 5 黄色
"""

# # 自定义类
# class Dog(object):
#
#     # 有参数的init方法 提高init方法的复用性
#     def __init__(self, new_name, new_age, new_color):
#         # 添加属性并赋值
#         self.name = new_name
#         self.age = new_age
#         self.color = new_color
#
#     def info(self):
#         print(self.name)
#         print(self.age)
#         print(self.color)
#         print("="*30)

# # 旺财 3 白色
# wc = Dog("旺财", 3, "白色")
# wc.info()
#
# # 藏獒 4 黑色
# za = Dog("藏獒", 4, "黑色")
# za.info()
#
# # 金毛 5 黄色
# jm = Dog("金毛", 5, "黄色")
# jm.info()

# 共100只狗 有88只都为5岁

# 自定义类
class Dog(object):

    # 有参数的init方法 提高init方法的复用性
    def __init__(self, name, color, age=5):
        # 添加属性并赋值
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print(self.name)
        print(self.age)
        print(self.color)
        print("="*30)