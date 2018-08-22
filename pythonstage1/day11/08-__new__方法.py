
# 自定义类
class Person(object):

    # 监听创建对象并返回
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return object.__new__(cls)

    # 监听对象创建成功后 给对象添加属性并赋值
    def __init__(self):
        print("__init__")
        self.name = "小明"

    # 监听对象属性值变化
    def __str__(self):
        print("__str__")
        return "姓名:%s" % self.name

    # 监听对象销毁(内存地址的引用计数为0)
    def __del__(self):
        print("__del__")
        print("再见")


xm = Person()
print(xm)