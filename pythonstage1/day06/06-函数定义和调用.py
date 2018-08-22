
# 变量的定义
num = 10
num = 20
# 调用
print(num)

# 一次定义 多次使用
# 函数的定义
"""
格式: 
def 函数名():
    代码部分
"""
def my_func():
    print("你好中国")

# 如果函数名一样的话 后面的函数会把前面的函数进行一个覆盖
def my_func():
    print("你好中国1")

# 函数的调用
# 格式: 函数名()
my_func()
my_func()