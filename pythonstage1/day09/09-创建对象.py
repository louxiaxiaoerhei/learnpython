
# # 自定义一个英雄类
# class Hero(object):
#     # 自定一个(实例或者对象)方法
#     def move(self):
#         print("人会行走...")
#
#
# # 自定义对象 -> 通过类创建对象
# lb = Hero()
# # <__main__.Hero object at 0x0000000000D90048> 16进制地址
# # print(id(lb))
# lb.move()


# 自定义一个犬类
class Dog(object):

    def eat(self):
        print("啃骨头")

# 狗 -> 旺财
wc = Dog()
wc.eat()