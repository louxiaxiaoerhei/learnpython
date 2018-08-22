# 私有的属性和私有方法 只能在类的内部使用  不能再类的外部访问
# 私有方法和私有属性 都是以__开头的
# 这个属性或者方法 不会在类的外面进行访问 就可以设置为私有的
# 自定义一个人类
class Person(object):

    def __init__(self, name,  money):
        # 公有属性(无论在类的外面和类的内部都可以进行访问)
        self.name = name
        self.__money = money

    # 公有方法(无论在类的外面和类的内部都可以进行访问)
    def eat(self):
        print(self.__money)
        print("人会吃饭...")
        self.__hello()

    # 私有方法
    def __hello(self):
        print("你好")


xm = Person("小明", 10000)
print(xm.name)
# print(xm.__money)
xm.eat()
