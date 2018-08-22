
# # 自定义人类
# class Person(object):
#
#     # 类属性(方法的外部 类的内部) -> 描述一个类的特征(通过这个类创建出来的对象的特征)
#     country = "中国"
#
#     def __init__(self):
#         # 实例属性(对象属性) -> 描述通过这个类创建出来的对象的特征
#         self.name = "小明"

# 访问(取值, 赋值)

# 取值
# 01: 类名.类属性名***
# print(Person.country)

# 02: 对象名.类属性名
# xm = Person()
# print(xm.country)

# 赋值
# 01: 类名.类属性名 = 数值***
# Person.country = "荷兰"
# print(Person.country)

# 02: 不存在
# 给这个对象添加了一个和类属性名字相同的实例属性
# Person().country = "荷兰"
# print(Person.country)


# 案例:
# 有名字 有国籍 -> 中国
class Person(object):

    # def __init__(self, name, country="中国"):
    #     self.name = name
    #     # self.country = country
    #     self.country = "中国"

    def __init__(self, name):
        self.name = name
        self.country = "中国"

# 类属性
class Person(object):

    # 类属性
    country = "中国"
    def __init__(self, name):
        self.name = name
