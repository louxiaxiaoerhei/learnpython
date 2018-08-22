# 古法师傅类
class Master(object):

    def make_cake(self):
        print("制作古法煎饼果子")


# 现代师傅类
class School(object):

    def make_cake(self):
        print("制作现代煎饼果子")

# 自定义徒弟类
class Prentice(Master, School):

    def make_cake(self):
        print("制作猫式煎饼果子")
    # 需求:因为子类继承了 子类而且重写了父类的同名方法 -> 子类无法调用父类的同名方法
    # 就想调用父类的同名方法
    def make_old_cake(self):
        # 父类名.父类的同名方法(self)
        Master.make_cake(self)

    def make_new_cake(self):
        School.make_cake(self)


dm = Prentice()
dm.make_cake()
dm.make_old_cake()
dm.make_new_cake()

