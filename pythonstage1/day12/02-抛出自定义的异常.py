
# 自定义异常类
class AgeError(Exception):

    def __init__(self, age):
        self.__age = age

    def __str__(self):
        return "您输入的年龄不符合业务需求age=%d" % self.__age


# 小明 年龄(age > 0 and age < 150)
class Person(object):

    def __init__(self, name, age):
        if age > 0 and age < 150:
            self.name = name
            self.age = age
        else:
            # 抛出自定义异常
            raise AgeError(age)

xm = Person("小明", 311)
