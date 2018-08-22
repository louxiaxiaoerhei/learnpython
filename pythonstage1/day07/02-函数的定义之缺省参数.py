# 定义一个函数负责输出名字和年龄(服务于python16期人员)
# python16期一共75人 (年龄分布 18岁 60人 19~35 15人)
# 如果在定义函数的时候 有形参(而且形参设置了默认值 这个形参成为缺省参数)
# def print_info(name, age=18):
#     print("------信息------")
#     print("姓名:%s" % name)
#     print("年龄:%d" % age)

# 在函数的调用的时候 如果缺省参数位置没有传入对应的实参 那么形参会使用自己的默认值
# print_info("小明")
# print_info("小红")
# 在函数的调用的时候 如果缺省参数的位置传入了对应的实参 那么形参会使用实参的数值
# (实参的数值会对默认值进行覆盖操作)
# print_info("小刚", 19)

# 特例: 如果某个形参为缺省参数 那么后面的形参必须也是缺省参数
def print_info(name, no, age=18):
    print("------信息------")
    print("姓名:%s" % name)
    print("年龄:%d" % age)
    print("学号:%s" % no)
