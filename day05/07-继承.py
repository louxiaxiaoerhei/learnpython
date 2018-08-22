class B(object):
    def __init__(self):
        print("B")

    def show(self):
        print("BBBB")


class C(object):
    def __init__(self):
        print("C")

    def show(self):
        print("CCCC")


class D(B, C):
    def __init__(self):
        print("D")
        # super().__init__()
        # 表示：根据指定类在类继承链找下一个类，调用下一个类的init的方法
        super(D, self).__init__()

        #super(B, self).__init__()

    def show(self):
        # 提示：如果是单继承可以直接理解成父类，如果是多继承需要指定类在类继承链的下一个类
        super(B, self).show()



print(D.mro())
d = D()
d.show()