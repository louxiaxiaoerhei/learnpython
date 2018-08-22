class Person(object):

    def __init__(self, name, age, no):
        # 添加实例属性并赋值
        self.name = name
        self.age = age
        self.no = no

    # def info(self):
    #     print(self.name)
    #     print(self.age)
    #     print(self.no)

    # 追踪对象的属性变化
    # 有返回值(必须返回一个字符串类型)
    def __str__(self):
        return "姓名:%s 年龄:%d 学号:%s" % (self.name, self.age, self.no)




# 小明  18  006
xm = Person("小明", 18, "006")
# xm.info()
# 如果没有实现str方法的时候 输出是16进制地址
# 如果实现了str方法的时候 输出的是str方法的字符串返回值
print(xm)