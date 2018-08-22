# 访问-> 取值 和 赋值
# 自定义人类 名字 年龄
class Person(object):

    def __init__(self):
        self.name = "小明"
        self.__age = 22

    # 获取age
    def get_age(self):
        return self.__age

    # 赋值
    def set_age(self, new_age):
        self.__age = new_age

# 需求: 想在类的外部 可以访问私有属性
# 直接访问一个私有属性 不可能
# 间接访问 -> 在类的内部定义一个公有方法
xm = Person()
# print(xm.name)
# 获取私有属性的值
print(xm.get_age())
# 对私有属性进行重新赋值
xm.set_age(33)
print(xm.get_age())

