# 变量 -> 函数 -> 类 -> 模块 -> 包

# 定义一个全局变量
name = "制作模块"

# 定义一个函数
def add2num(a, b):
    return a + b

# 定义一个类
class Person(object):
    pass

# 测试(自测)
# 定义一个函数 测试函数
def main():
    print(name)
    print(add2num(10, 22))
    print(Person())

main()

