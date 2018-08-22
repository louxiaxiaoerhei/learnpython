
# 自定义师傅类
class Master(object):

    def __init__(self):
        # 配方
        self.kongfu = "中国古法配方"

    def make_cake(self):
        print("制作古法煎饼果子")

# # 李师傅
# lsf = Master()
# print(lsf.kongfu)
# lsf.make_cake()

# 自定义一个徒弟类
# 格式: class 子类名(父类名):
class Prentice(Master):
    pass


# 子类继承类父类 子类就继承了父类的属性和方法
dm = Prentice()
print(dm.kongfu)
dm.make_cake()

