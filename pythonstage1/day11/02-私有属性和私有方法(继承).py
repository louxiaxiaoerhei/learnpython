
# 师傅类
class Master(object):

    def __init__(self):
        self.kongfu = "古法配方"
        self.__money = 100000

    def make_cake(self):
        print("煎饼果子")

    def __hello_python(self):
        print("会python")

# 自定义徒弟类
class Prentice(Master):
    pass
    # def my_func(self):
    #     print(self.__money)
    #     self.__hello_python()


# 子类继承了父类: 子类就继承了父类的属性和方法(私有的不会被继承)
dm = Prentice()
print(dm.kongfu)
# print(dm.__money)
dm.make_cake()
# dm.hello_python()
dm.my_func()


