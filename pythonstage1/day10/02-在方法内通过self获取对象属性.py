
# 自定义一个犬类
class Dog(object):

    # 吃骨头
    def eat(self):
        print(self)

    # 打印对象的属性值
    # 使用了哪个对象调用这个方法 self就是哪个对象
    def info(self):
        # 在类的内部方法中 使用的是 self.属性名
        # 打印
        print(self.name)
        print(self.age)
        print(self.color)

# 旺财 3 黄色
wc = Dog()
# print(wc)
# wc.eat(wc)
# 添加属性
wc.name = "旺财"
wc.age = 3
wc.color = "黄色"

# 打印
# 在类的外面 使用的 对象名.属性名
# print(wc.name)
# print(wc.age)
# print(wc.color)
wc.info()
print("="*20)
# 藏獒 4  黑色
za = Dog()
# print(za)
# za.eat()
# 添加属性
za.name = "藏獒"
za.age = 4
za.color = "黑色"

# 打印
# print(za.name)
# print(za.age)
# print(za.color)
za.info()
