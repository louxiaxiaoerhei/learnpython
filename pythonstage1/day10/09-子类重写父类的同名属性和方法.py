# 古法师傅类
class Master(object):

    def __init__(self):
        # 配方
        self.kongfu = "古法配方"

    def make_cake(self):
        print("制作古法煎饼果子")

    def dayandai(self):
        print("dayandai")

# 现代师傅类
class School(object):

    def __init__(self):
        # 配方
        self.kongfu = "现代配方"

    def make_cake(self):
        print("制作现代煎饼果子")

    def xiaoyandai(self):
        print("xiaoyandai")

# 自定义徒弟类
class Prentice(Master, School):

    # 重写: 子类继承了父类 重写了父类的已有同名方法 做自己特有的事情 称之为重写
    def __init__(self):
        self.kongfu = "猫式配方"

    def make_cake(self):
        print("制作猫式煎饼果子")

"""
如果子类继承了父类
    - 如果子类有 就调用子类的
    - 如果子类没有 就调用父类的
    - 如果多个父类都没有 就会调用object
    - 如果object没有 就会报错
"""
#查看 继承链
print(Prentice.__mro__)
dm = Prentice()
print(dm.kongfu)
dm.make_cake()
dm.dayandai()
dm.xiaoyandai()
