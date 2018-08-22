# 4种函数的类型
# 01: 无参数无返回值
# 02: 无参数有返回值
# 03: 有参数无返回值
# 04: 有参数有返回值

# 01: 无参数无返回值
"""
def 函数名():
    代码逻辑
"""
def my_func():
    print("你好")

"""
函数名()
"""
# my_func()

# 02: 无参数有返回值
"""
def 函数名():
    return 返回值
"""
def get_pi():
    return 3.1415926

"""
变量名 = 函数名()
"""
# print(get_pi())

# 03: 有参数无返回值
"""
def 函数名(形参1, 形参2, ...):
    代码逻辑
"""
def my_print(name):
    print("您好:%s" % name)

# 函数名(实参1, 实参2, ...)
# my_print("龟叔")


# 04: 有参数有返回值
"""
def 函数名(形参1, 形参2, ...):
    代码逻辑
    return 返回值
"""
def average2num(num1, num2):
    return (num1 + num2) / 2

"""
变量名 = 函数名(实参1, 实参2, ...)
"""
result = average2num(10, 20)
print(result)