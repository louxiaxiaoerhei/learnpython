# 自定义类
class Person(object):

    # 私有的类属性
    __country = "中国"

    def __init__(self):
        self.__age = 10

    # 实例方法(对象)
    # 取值
    def get_age(self):
        return self.__age

    # 赋值
    def set_age(self, new_age):
        self.__age = new_age

    # 类方法
    # 取值
    @classmethod
    def get_country(cls):
        return cls.__country

    # 赋值
    @classmethod
    def set_country(cls, new_country):
        cls.__country = new_country

    # 静态方法
    @staticmethod
    def hello():
        print("你好")

# 调用一个静态方法方式:
# 01:对象名.静态方法名
# xm = Person()
# xm.hello()
# 02:类名.对象名
# Person.hello()


