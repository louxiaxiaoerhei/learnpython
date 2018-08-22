# 自定义一个人类
class Person(object):

    # 国籍
    # 私有类属性
    __country = "中国"

    # 取值
    # 定义一个类方法
    # 定义类方法或者静态方法需要加修饰器
    # cls -> class -> Person
    @classmethod
    def get_country(cls):
        return cls.__country

    # 赋值
    @classmethod
    def set_country(cls, new_country):
        cls.__country = new_country

# 因为是私有的
# print(Person.__country)

# 类方法的调用方式:
# 01: 类名.类方法名() ***
# 02: 对象名.类方法名()
# 01: 取值
print(Person.get_country())
# 02: 赋值
Person().set_country("荷兰")
print(Person.get_country())