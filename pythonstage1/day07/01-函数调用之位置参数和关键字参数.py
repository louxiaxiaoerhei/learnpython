
# 定义一个函数(有参数)
def print_info(name, age):
    print("姓名:%s" % name)
    print("年龄:%d" % age)


# 函数的调用
# 01:位置参数(实参和形参的个数要一样, 而且位置要一一对应)
# print_info("小明", 22)
# 02:关键字参数(只要再调用的时候书写形参名正确即可)
# print_info(name="小明", age=20)


# 定义一个函数(有参数) -> 只能使用关键字参数调用
# def print_info(*, name, age):
#     print("姓名:%s" % name)
#     print("年龄:%d" % age)

