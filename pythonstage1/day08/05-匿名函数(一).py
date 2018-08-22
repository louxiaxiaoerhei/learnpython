# 01: 函数的另一种表现形式
# 02: 作为函数调用的实参
# 03: 应用于自定义排序中

# 01: 函数的另一种表现形式
# 匿名函数: 藏匿名字
# 把一个比较简单的函数 翻译成 匿名函数书写
# # 01: 无参无返回值
# def my_print():
#     print("hello world")
#
# # my_print()
# # 转化
# f = lambda :print("hello world")
# f()

# # 02: 无参数有返回值
# def get_pi():
#     return 3.14
#
# # print(get_pi())
# # 转化
# f = lambda :3.14
# print(f())

# # 03: 有参数无返回值
# def print_info(name, age):
#     print("你好%s%d" % (name, age))
#
# # print_info("中国")
# f = lambda name, age :print("你好%s%d" % (name, age))
# f("中国", 22)

# # 04: 有参数有返回值
# def add2num(a, b):
#     return a + b
# # print(add2num(10, 20))
#
# f = lambda a, b:a + b
# print(f(10, 20))

# 02: 作为函数调用的实参
# # 变量
# num = 10
# def func(a):
#     print(a)
#
# func(num)

# 定义一个函数(求和 3个数)
# def add3num(a, b, c):
#     return a + b + c
# 转化
f = lambda a, b, c: a + b + c
# aaaa = add3num
# print(aaaa(10, 20, 30))
def average3num(num1, num2, num3, a):
    ret = a(num1, num2, num3)
    return ret / 3

print(average3num(10, 20, 30, f))