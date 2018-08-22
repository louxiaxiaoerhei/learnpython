# 自定义犬类
class Dog(object):
    """
    魔法方法:以两个_开头, 且以两个_结尾的方法 称之为魔法方法
    魔法方法 不需要程序员手动调用 他会在特殊的情况下 被python调用
    一般情况下 我们程序员子类继承父类后 实现__init__ 在init方法完成给其对象添加属性并赋值
    python已经定义好 我们直接使用即可(实现)
    """
    def __init__(self):
        # 添加属性并赋值
        self.name = "旺财"
        self.age = 3
        self.color = "黄色"

    # 啃骨头
    def eat(self):
        print("啃骨头")

    # 打印属性值
    def info(self):
        print(self.name)
        print(self.age)
        print(self.color)
        print("="*30)


# 旺财 3  黄色
wc1 = Dog()
# wc1.set_info()
# # 添加属性
# wc1.name = "旺财"
# wc1.age = 3
# wc1.color = "黄色"
#
wc1.info()

# 旺财 3  黄色
wc2 = Dog()
# wc2.set_info()
# 添加属性
# wc2.name = "旺财"
# wc2.age = 3
# wc2.color = "黄色"
#
wc2.info()

# 如果相同名字的 年龄 肤色 有20只
