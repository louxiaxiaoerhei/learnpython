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

    # 重写
    def make_cake(self):
        print("制作猫式煎饼果子")
    # 子类调用父类的同名方法总结
    # 三种解决方案:
    # 父类名.父类的同名方法(self)
    # super(子类名, self).父类的同名方法()
    # 自定义
    def make_old_cake(self):
        # 01:父类名.父类的同名方法(self) 多继承(单继承)
        # Master.make_cake(self)
        # 02:super(子类名, self).父类的同名方法() 单继承(多继承 调用第一个父类的同名方法)
        # super(Prentice, self).make_cake()
        # 03:super().父类的同名方法() 单继承(多继承 调用第一个父类的同名方法)
        super().make_cake()
    # 自定义
    def make_new_cake(self):
        super().make_cake()


dm = Prentice()
# dm.make_cake()
dm.make_old_cake()
dm.make_new_cake()

