# 自定义一个人类
class Person(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("肯德基")


# 自定义一个犬类
class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("啃骨头")

# 多行代码  -> 无参数的函数 -> 提高代码的复用性
# 无参数函数 -> 有参数函数  -> 提高无参数的函数的复用性
# 有参数(定义时候设定的的某个类型)的函数 -> 有参数(运行时候的类型和定义不同)的函数 -> 多态

# 定义时候的类型 和运行时类型不同
# # 设计模式  -> 多态(多种形态)
# def func(obj):
#     # 传入的对象必须有这个属性和这个方法
#     print(obj.name)
#     obj.eat()
#
# # # 定义一个
# # def person_func(obj):
# #     print(obj.name)
# #     obj.eat()
#
# # 人类
# xm = Person("小明")
# # person_func(xm)
# func(xm)
# print("="*20)
# # 犬类
# # # 定义一个
# # def dog_func(obj):
# #     print(obj.name)
# #     obj.eat()
#
# wc = Dog("旺财")
# # dog_func(wc)
# func(wc)


# 方法中的多态
class HMTool(object):

    def func(self, obj):
        print(obj.name)
        obj.eat()

# 人类
xm = Person("小明")
# 犬类
wc = Dog("旺财")

t1 = HMTool()
t1.func(xm)
# t2 = HMTool()
t1.func(wc)
